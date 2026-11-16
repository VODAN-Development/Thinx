"""D-A1 authorization tests. Run from the real backend directory with pytest."""
import os
os.environ.setdefault('SECRET_KEY', 'test-only-secret-not-for-production-123456789012345')

import pytest
import app as backend
from models import UserManager, ConnectionManager, Connection


@pytest.fixture
def env(tmp_path, monkeypatch):
    users = UserManager(tmp_path / 'users.json')
    connections = ConnectionManager(tmp_path / 'connections.json')
    monkeypatch.setattr(backend, 'user_manager', users)
    monkeypatch.setattr(backend, 'connection_manager', connections)
    admin = users.create_user('administrator', 'password-strong-123', is_admin=True)
    alice = users.create_user('alice', 'password-strong-123')
    bob = users.create_user('bob', 'password-strong-123')
    conn = connections.add_connection(Connection(name='Alice', user_id=alice['id']))
    with backend.app.test_client() as client:
        yield client, users, connections, admin, alice, bob, conn


def auth(client, username):
    response = client.post('/api/login', json={'username': username, 'password': 'password-strong-123'})
    assert response.status_code == 200, response.get_json()
    token = response.get_json()['access_token']
    return {'Authorization': f'Bearer {token}'}


def test_unauthenticated_blocked(env):
    client, *_ = env
    assert client.get('/api/admin/users').status_code == 401
    assert client.get('/api/connections').status_code == 401
    assert client.post('/api/query', json={'query': 'SELECT * WHERE {?s ?p ?o}'}).status_code == 401


def test_researcher_blocked_from_admin_and_workspace(env):
    client, *_ = env
    headers = auth(client, 'alice')
    assert client.get('/api/admin/users', headers=headers).status_code == 403
    assert client.post('/api/upload', headers=headers).status_code == 403


def test_admin_allowed(env):
    client, *_ = env
    response = client.get('/api/admin/users', headers=auth(client, 'administrator'))
    assert response.status_code == 200
    assert len(response.get_json()['users']) == 3


def test_researcher_connection_isolation(env):
    client, _, connections, _, alice, bob, conn = env
    bob_connection = connections.add_connection(Connection(name='Bob', user_id=bob['id']))
    headers = auth(client, 'alice')
    response = client.get('/api/connections', headers=headers)
    assert response.status_code == 200
    assert [c['id'] for c in response.get_json()['connections']] == [conn['id']]
    assert client.get(f"/api/connections/{bob_connection['id']}", headers=headers).status_code == 404
    assert client.delete(f"/api/connections/{bob_connection['id']}", headers=headers).status_code == 404
    assert client.post('/api/query', json={'query': 'SELECT * WHERE {?s ?p ?o}', 'connection_id': bob_connection['id']}, headers=headers).status_code == 404


def test_cannot_change_connection_owner(env):
    client, _, connections, _, alice, bob, conn = env
    result = client.put(f"/api/connections/{conn['id']}", json={'user_id': bob['id'], 'is_active': False, 'name': 'Changed'}, headers=auth(client, 'alice'))
    assert result.status_code == 200
    assert connections.get_connection(conn['id'])['user_id'] == alice['id']
    assert 'password' not in result.get_json()['connection']


def test_invalid_token(env):
    client, *_ = env
    assert client.get('/api/connections', headers={'Authorization': 'Bearer invalid'}).status_code == 401


def test_token_invalid_after_password_change(env):
    client, users, _, _, alice, *_ = env
    headers = auth(client, 'alice')
    users.update_user(alice['id'], {'password': 'updated-password-strong-123'})
    assert client.get('/api/connections', headers=headers).status_code == 401


def test_public_health(env):
    client, *_ = env
    assert client.get('/api/health').status_code == 200

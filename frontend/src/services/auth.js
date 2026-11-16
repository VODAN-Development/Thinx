
import { reactive } from 'vue'

const SESSION_KEY = 'thinx.auth.session.v1'

function readStoredSession() {
  try {
    const value = sessionStorage.getItem(SESSION_KEY)
    if (!value) return null

    const stored = JSON.parse(value)

    if (
      !stored?.user ||
      !stored?.accessToken ||
      !Number.isFinite(stored.expiresAt) ||
      Date.now() >= stored.expiresAt
    ) {
      sessionStorage.removeItem(SESSION_KEY)
      return null
    }

    return stored
  } catch (_error) {
    try {
      sessionStorage.removeItem(SESSION_KEY)
    } catch (_ignored) {}
    return null
  }
}

const restored = readStoredSession()

export const authState = reactive({
  user: restored?.user ?? null,
  accessToken: restored?.accessToken ?? null,
  expiresAt: restored?.expiresAt ?? null
})

export function setSession(user, token, expiresIn = 1800) {
  if (!user || !token) {
    throw new Error('Invalid login response')
  }

  const seconds = Number(expiresIn)

  if (!Number.isFinite(seconds) || seconds <= 0) {
    throw new Error('Invalid token lifetime')
  }

  const expiresAt = Date.now() + seconds * 1000

  const safeUser = {
    id: user.id,
    username: user.username,
    is_admin: user.is_admin === true,
    full_name: user.full_name ?? null,
    email: user.email ?? null
  }

  sessionStorage.setItem(
    SESSION_KEY,
    JSON.stringify({
      user: safeUser,
      accessToken: token,
      expiresAt
    })
  )

  authState.user = safeUser
  authState.accessToken = token
  authState.expiresAt = expiresAt
}

export function clearSession() {
  authState.user = null
  authState.accessToken = null
  authState.expiresAt = null

  try {
    sessionStorage.removeItem(SESSION_KEY)
  } catch (_ignored) {}
}

export function hasValidSession() {
  if (!authState.accessToken) return false

  if (!authState.expiresAt || Date.now() >= authState.expiresAt) {
    clearSession()
    return false
  }

  return true
}

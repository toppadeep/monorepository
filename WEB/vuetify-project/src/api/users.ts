import type { UserRead } from '@/types/user'
import api from './client'

export const getUsers = () => api.get<UserRead[]>('/users')
export const getUser = (username: string) => api.get<UserRead>(`/users/${username}`)

export const getStatusServer = () => api.get<boolean | null>('/health')

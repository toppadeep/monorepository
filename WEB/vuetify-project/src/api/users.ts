import api from './client'
import type { UserRead } from "@/types/user";

export const getUsers = () => api.get<UserRead[]>('/users')
export const getUser = (id: number) => api.get<UserRead>(`/users/${id}`)
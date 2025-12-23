<template>
  <v-container class="pa-6">
    <!-- Заголовок и проверка сервера -->
    <v-row align="center" class="mb-6" justify="space-between">
      <h1 class="text-h4 font-weight-bold ma-0">List of Users</h1>

      <v-snackbar
        v-model="snackbar"
        :color="health ? 'success' : 'error'"
        timeout="2000"
        variant="outlined"
      >
        {{ health ? "It's working successfully" : 'Internal Server Error - not connected' }}
      </v-snackbar>

      <v-btn color="primary" variant="outlined" @click="checkHealthServer">
        Check server health
      </v-btn>
    </v-row>

    <!-- Таблица пользователей -->
    <v-data-table
      class="elevation-2"
      :headers="headers"
      hover
      item-value="id"
      :items="users"
      :loading="loading"
      @click:row="handleRowClick"
    >
      <!-- Скелетоны для загрузки -->
      <template #loading>
        <v-skeleton-loader v-for="n in 5" :key="n" class="mb-2" type="table" />
      </template>

      <template #item.name="{ item }">
        <span class="font-weight-medium">{{ item.name }}</span>
      </template>

      <template #item.username="{ item }">
        {{ item.username }}
      </template>

      <template #item.email="{ item }">
        {{ item.email }}
      </template>
    </v-data-table>
  </v-container>
</template>

<script setup lang="ts">
  import type { UserRead } from '@/types/user'
  import { onMounted, ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { getStatusServer, getUsers } from '@/api/users'

  const users = ref<UserRead[]>([])
  const health = ref<boolean | null>(null)
  const snackbar = ref(false)
  const loading = ref(true)
  const router = useRouter()

  const headers = [
    { title: 'Name', key: 'name' },
    { title: 'Username', key: 'username' },
    { title: 'Email', key: 'email' },
  ]

  async function loadUsers () {
    try {
      const response = await getUsers()
      users.value = response.data
    } catch (error) {
      console.error('Error loading users', error)
    } finally {
      loading.value = false
    }
  }

  async function checkHealthServer () {
    try {
      const response = await getStatusServer()
      health.value = response.data.status
    } catch {
      health.value = false
    } finally {
      snackbar.value = true
    }
  }

  function handleRowClick (event: Event, { item }: { item: UserRead }) {
    router.push({ name: 'user-detail', params: { username: item.username } })
  }

  onMounted(() => {
    loadUsers()
    checkHealthServer()
  })
</script>

<style scoped>
.v-data-table tbody tr {
  cursor: pointer;
  transition: background-color 0.2s;
}

.v-data-table tbody tr:hover {
  background-color: #f5f5f5;
}

h1 {
  letter-spacing: 0.5px;
}
</style>

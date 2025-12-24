<template>
    <v-container>
        <h1>Cписок пользователей</h1>

        <v-data-table :headers="headers" :items="users" :loading="loading" item-value="id"
            class="evevation-2">
            <template v-slot:item.name="{ item }">
                <router-link :to="{ name: 'user-detail', params: { id: item.id } }">
                    {{ item.name }}
                </router-link>
            </template>
        </v-data-table>

    </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getUsers } from '@/api/users'
import type { UserRead } from '@/types/user';
import { tr } from 'vuetify/locale';

const users = ref<UserRead[]>([])
const loading = ref(true)

const headers = [
    { title: 'Name', key: 'name' },
    { title: 'Username', key: 'username' },
    { title: 'Email', key: 'email' },
]

async function loadUsers() {
    try {
        const response = await getUsers()
        users.value = response.data
    } catch (err) {
        console.error('Возникла ошибка при загрузке пользователей', err)
    } finally {
        loading.value = false
    }
}

onMounted(loadUsers)

</script>
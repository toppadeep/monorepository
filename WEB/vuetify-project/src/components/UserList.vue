<template>
    <v-container>
        <h1>Cписок пользователей</h1>

        <v-data-table :headers="headers" :items="users" :loading="loading" item-value="id" @click:row="handleRowClick"
            class="evevation-2">

        </v-data-table>

        <v-dialog v-model="dialog" max-width="600">
            <v-card v-if="selectedUser">
                <v-card-title class="text-h5">
                    {{ selectedUser.name }}
                </v-card-title>

                <v-card-text>
                    <v-list density="compact">
                        <v-list-item>
                            <v-list-item-title>Username</v-list-item-title>
                            <v-list-item-subtitle>{{ selectedUser?.username }}</v-list-item-subtitle>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-title>Email</v-list-item-title>
                            <v-list-item-subtitle>{{ selectedUser?.email }}</v-list-item-subtitle>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-title>Website</v-list-item-title>
                            <v-list-item-subtitle>{{ selectedUser?.website }}</v-list-item-subtitle>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-title>Company</v-list-item-title>
                            <v-list-item-subtitle>{{ selectedUser?.company_name }}</v-list-item-subtitle>
                        </v-list-item>
                    </v-list>
                </v-card-text>

                <v-card-actions>
                    <v-spacer />
                    <v-btn class="primary" variant="text" @click="dialog = false">
                        Закрыть
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

    </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getUsers } from '@/api/users'
import type { UserRead } from '@/types/user';
import { tr } from 'vuetify/locale';

const users = ref<UserRead[]>([])
const selectedUser = ref<UserRead | null>(null)
const dialog = ref(false)
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

function handleRowClick(_event: any, { item }: { item: UserRead }) {
    selectedUser.value = item
    dialog.value = true
}

onMounted(loadUsers)

</script>
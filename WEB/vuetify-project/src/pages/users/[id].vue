<template>
    <v-container>
        <v-btn @click="router.back()" class="mb-4">
            Вернуться
        </v-btn>
        <v-card v-if="user" class="pa-4">
            <v-card-title class="text-h4">{{ user.name }}</v-card-title>
            <v-card-subtitle>{{ user.username }}</v-card-subtitle>

            <v-list density="compact">
                <v-list-item>
                    <v-list-item-title>Username</v-list-item-title>
                    <v-list-item-subtitle>{{ user?.username }}</v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                    <v-list-item-title>Email</v-list-item-title>
                    <v-list-item-subtitle>{{ user?.email }}</v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                    <v-list-item-title>Website</v-list-item-title>
                    <v-list-item-subtitle>{{ user?.website }}</v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                    <v-list-item-title>Company</v-list-item-title>
                    <v-list-item-subtitle>{{ user?.company_name }}</v-list-item-subtitle>
                </v-list-item>
            </v-list>
        </v-card>
        <v-alert v-else type="error">Пользовтель не найден</v-alert>
    </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import { getUser } from '@/api/users';
import type { UserRead } from '@/types/user';

const route = useRoute()
const router = useRouter()
const user = ref<UserRead | null>(null)
const loading = ref(true)

async function loadUser() {
    try {
        const id = Number(route.params.id)
        const res = await getUser(id)
        user.value = res.data
    } catch (err) {
        console.error(err)
        user.value = null
    } finally {
        loading.value = false
    }
}

onMounted(loadUser)

</script>
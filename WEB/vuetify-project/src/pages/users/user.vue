<template>
  <v-container class="pa-8">
    <v-btn class="mb-6" @click="router.back()"> Back </v-btn>

    <v-card class="pa-6 mx-auto" elevation="8" max-width="900" style="position: relative">
      <!-- CONFIDENTIAL штамп -->
      <div class="confidential-stamp">CONFIDENTIAL</div>

      <!-- Заголовок досье -->
      <v-card-title class="text-h3 font-weight-bold mb-6">
        {{ user?.name || 'Неизвестный пользователь' }}
      </v-card-title>

      <v-row>
        <!-- Фото / Скелетон -->
        <v-col class="d-flex justify-center mb-4 md:mb-0" cols="12" md="4">
          <v-skeleton-loader class="rounded" style="width: 250px; height: 400px" />
        </v-col>

        <!-- Основные данные -->
        <v-col cols="12" md="8">
          <v-list dense>
            <v-list-item v-for="(value, key) in mainFields" :key="key">
              <v-list-item-title class="font-weight-bold">{{ key }}</v-list-item-title>
              <v-list-item-subtitle>
                <template v-if="!loading">{{ value }}</template>
                <v-skeleton-loader v-else type="text" />
              </v-list-item-subtitle>
            </v-list-item>

            <!-- Конфиденциальные поля -->
            <v-divider class="my-4" />
            <div class="text-subtitle-2 font-weight-bold mb-2">Confidential information</div>

            <v-list-item v-for="field in confidentialFields" :key="field">
              <v-list-item-title class="font-weight-bold">{{ field }}</v-list-item-title>
              <v-list-item-subtitle>
                <v-skeleton-loader type="text" />
              </v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
    </v-card>

    <v-alert v-if="!user && !loading" class="mt-6" type="error"> User not found </v-alert>
  </v-container>
</template>

<script setup lang="ts">
  import type { UserRead } from '@/types/user'
  import { computed, onMounted, ref } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { getUser } from '@/api/users'
  const confidentialFields = ['Secret code', 'Last access date', 'Access level']

  const route = useRoute()
  const router = useRouter()
  const user = ref<UserRead | null>(null)
  const loading = ref(true)

  const mainFields = computed(() => ({
    Username: user.value?.username || '',
    Email: user.value?.email || '',
    Website: user.value?.website || '',
    Company: user.value?.company_name || '',
  }))

  async function loadUser () {
    try {
      const username = route.params.username as string
      const res = await getUser(username)
      user.value = res.data
    } catch (error) {
      console.error(error)
      user.value = null
    } finally {
      loading.value = false
    }
  }

  onMounted(loadUser)
</script>

<style scoped>
.v-card-title {
  letter-spacing: 1px;
}

/* CONFIDENTIAL штамп */
.confidential-stamp {
  position: absolute;
  top: 16px;
  right: -20px;
  transform: rotate(45deg);
  font-size: 48px;
  font-weight: bold;
  color: rgba(255, 0, 0, 0.25);
  pointer-events: none;
  z-index: 0;
}
</style>

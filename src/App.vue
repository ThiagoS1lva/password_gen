<script>
import Generator from './components/Generator.vue';
import TikTakToe from './components/TikTakToe.vue';

export default {
  name: 'App',
  components: {
    Generator,
    TikTakToe,
  }
}
</script>

<template>
  <main>
    <Generator />
    <TikTakToe />
  </main>
</template>



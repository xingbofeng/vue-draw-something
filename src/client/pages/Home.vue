<template>
  <div class="Home">
    <layout>
      <p
        slot="content"
      >Home</p>
    </layout>
  </div>
</template>

<script>
import Layout from '../components/Layout';

export default {
  name: 'Home',

  components: {
    Layout,
  },
}
</script>

<style scoped>

</style>

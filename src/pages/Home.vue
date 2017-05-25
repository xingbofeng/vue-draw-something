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
import ExplainCard from '../components/ExplainCard';

export default {
  name: 'Home',

  components: {
    Layout,
    ExplainCard,
  },
}
</script>

<style scoped>

</style>

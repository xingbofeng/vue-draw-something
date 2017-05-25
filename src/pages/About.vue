<template>
  <div class="About">
    <layout>
      <explain-card
        slot="content"
      />
    </layout>
  </div>
</template>

<script>
import Layout from '../components/Layout';
import ExplainCard from '../components/ExplainCard';

export default {
  name: 'About',

  components: {
    Layout,
    ExplainCard,
  },
}
</script>

<style scoped>

</style>

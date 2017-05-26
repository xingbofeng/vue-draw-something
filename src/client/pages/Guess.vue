<template>
  <div class="Guess">
    <layout>
      <guess-content
        slot="content"
      />
    </layout>
  </div>
</template>

<script>
import Layout from '../components/Layout';
import GuessContent from '../components/p_guess/GuessContent';

export default {
  name: 'Guess',

  components: {
    Layout,
    GuessContent,
  },
}
</script>

<style scoped>

</style>

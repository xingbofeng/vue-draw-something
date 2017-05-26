<template>
  <div class="Guess">
    <layout>
      <div
        slot="content"
        class="content"
      >
        <div>
          <guess-answer />
          <board />
        </div>
        <chatting
          :person="$store.state.login.text.slice(5)"
        />
      </div>
    </layout>
  </div>
</template>

<script>
import Layout from '../components/Layout';
import GuessAnswer from '../components/p_guess/GuessAnswer';
import Board from '../components/p_guess/Board';
import Chatting from '../components/Chatting';

export default {
  name: 'Guess',

  components: {
    Layout,
    GuessAnswer,
    Board,
    Chatting,
  },
}
</script>

<style scoped>
.content {
  padding: 30px 50px 0 30px;
  display: flex;
}
</style>

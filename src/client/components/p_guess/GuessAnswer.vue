<template>
  <div class="GuessAnswer">
    <mu-text-field
      type="text"
      v-model.trim="userAnswer"
      label="我猜答案是……"
      @change="checkAnswer"
    />
    <mu-raised-button
      @click="checkAnswer"
      label="确定"
      icon="input"
      :disabled="!userAnswer"
      primary
    />
    <mu-dialog :open="isDialogShow">
      {{ correctAnswer === userAnswer ? '恭喜你答对了！' : '回答错啦~再仔细思考思考呗~' }}
    <mu-flat-button
      label="确定"
      slot="actions"
      primary
      @click="closeDialog"
    />
    </mu-dialog>
  </div>
</template>

<script>
import socketClient from 'socket.io-client';

export default {
  name: 'GuessAnswer',

  data() {
    return {
      socket: socketClient('http://localhost:2017'),
      correctAnswer: '', // 正确答案
      userAnswer: '', // 用户答案
      isDialogShow: false, // 是否展示对话框
    }
  },

  mounted() {
    this.socket.on('connect', () => this.connet());
  },

  methods: {
    /**
     * 核对正确答案
     */
    checkAnswer() {
      // 如果没有输入答案则啥都不干
      if (!this.userAnswer) {
        return;
      }
      this.isDialogShow = true;
    },

    connet() {
      this.socket.on('givingAnswer', this.givingAnswer);
    },

    givingAnswer(message) {
      this.correctAnswer = message;
    },

    closeDialog() {
      this.userAnswer = '';
      this.isDialogShow = false;
    },
  },
}
</script>

<style scoped>
.GuessAnswer {
  padding-left: 200px;
}
</style>

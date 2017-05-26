<template>
	<div class="chat">
    <div class="chatBroad">
      <h1
        v-for="item in messageArray"
      >{{ item }}</h1>
    </div>
    <input
      type="text"
      v-model="message"
      @keyup.enter="submitChat"
      placeholder="在此输入您的聊天内容"
    >
    <button @click="submitChat">发送</button>
  </div>
</template>
<script>
import socketClient from 'socket.io-client';
const socket = socketClient('http://localhost:2017');

export default {
	name: 'Chatting',

	props: ['sp'],

  data() {
    return {
      message: '',
      messageArray: [],
    }
  },

  created() {
  	socket.on('chatting', (message) => {
      this.messageArray.push(message);
  	});
  },

  methods: {
    submitChat: function () {
      socket.emit('chat', `${this.sp} says: "${this.message}"`);
      this.message = '';
    },
  },
}
</script>

<style scoped>
button {
  background-color: green;
  border-radius: 2px;
  text-align: center;
  width: 50px;
  height: 30px;
  font-size: 16px;
  border: 2px #777 solid;
  box-sizing: content-box;
}
input {
  height: 30px;
  font-size: 16px;
  line-height: 30px;
  outline: none;
  padding: 0;
}
.chatBroad {
  height: 600px;
  overflow-y: scroll;
  width: 350px;
  border: 2px #777 solid;
}
.chat input {
  margin-top: 20px;
  width: 280px;
}
</style>
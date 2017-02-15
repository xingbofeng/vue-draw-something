<template>
	<div class="chat">
      <div class="chatBroad">
      </div>
      <input
        type="text"
        v-model="chat"
        v-on:keyup.enter="submitChat"
        placeholder="在此输入您的聊天内容"
      >
      <button v-on:click="submitChat">确定</button>
    </div>
</template>
<script>
let socket = require('socket.io-client')('http://localhost:2017');
export default {
	name: 'Chatting',
	props: ['sp'],
  data () {
    return {
      chat: '',
    }
  },
  created: function () {
  	socket.on('chatting', (message) => {
  		let broad = document.getElementsByClassName('chatBroad')[0];
  		let myMessage = document.createElement('h1');
  		myMessage.innerText = message;
  		broad.appendChild(myMessage);
  	});
  },
  methods: {
    submitChat: function () {
      var chat = this.chat;
      var sp = this.sp;
      socket.emit('chat', `${sp} says: "${chat}"`);
    }
  }
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
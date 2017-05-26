<template>
  <div class="chatting">
  	<mu-paper class="paper" :zDepth="3">
      <mu-list>
        <mu-sub-header>聊天记录</mu-sub-header>
        <mu-list-item
          v-for="item in messageArray"
          :title="item"
        >
          <mu-icon value="chat_bubble" slot="right"/>
        </mu-list-item>
      </mu-list>
    </mu-paper>
    <mu-text-field
      type="text"
      v-model="message"
      label="在此输入您的聊天内容"
      @change="submitChat"
    />
    <mu-raised-button
      @click="submitChat"
      label="确定"
      icon="input"
      :disabled="!message"
      primary
    />
  </div>
</template>
<script>
import socketClient from 'socket.io-client';

export default {
	name: 'Chatting',

	props: ['person'],

  data() {
    return {
      socket: socketClient('http://localhost:2017'),
      message: '',
      messageArray: [],
    }
  },

  created() {
  	this.socket.on('chatting', (message) => {
      if (this.messageArray.length >= 10) {
        // 最多只有10条
        this.messageArray.shift();
      }
      this.messageArray.push(message);
  	});
  },

  methods: {
    submitChat() {
      this.socket.emit('chat', `${this.person}: "${this.message}"`);
      this.message = '';
    },
  },
}
</script>

<style scoped>
.chatting {
  margin-left: 50px;
  padding: 20px;
}

.paper {
  height: 535px;
}
</style>
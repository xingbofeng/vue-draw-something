<template>
  <div class="Canvas">
    <div>
      <div class="header">
        <div>
          <input
            type="text"
            v-model.trim="myAnswer"
            v-on:keyup.enter="onEnter"
            placeholder="在这里填写您的答案哟!别忘了Enter或者确定!"
          >
          <button v-on:click="onEnter">确定</button>
        </div>
      </div>
      <canvas
        ref="canvas"
        width="800"
        height="500"
      ></canvas>
    </div>
    <Chatting sp="guesser"></Chatting>
  </div>
</template>

<script>
import Chatting from '../Chatting.vue';
import socketClient from 'socket.io-client';

export default {
  name: 'GuessContent',

  components: {
    'Chatting': Chatting
  },

  mounted() {
    const socket = socketClient('http://localhost:2017');
    const ctx = this.$refs.canvas.getContext('2d');
		socket.on('connect', function () {
		  socket.on('painting', function (message) {
			ctx.lineTo(message.left, message.top);
		    ctx.stroke();
		  });
		  socket.on('began', function (message) {
		  	ctx.strokeStyle = "#000";
		    ctx.beginPath();
		    ctx.moveTo(message.left, message.top);
		  });
		  socket.on('clear', function () {
		  	ctx.clearRect(0, 0, 800, 500);
		  });
      socket.on('givingAnswer', function (message) {
        // 设置答案事件
        this.answer = message;
      });
		});
  },

  data() {
    return {
      answer: '',
      myAnswer: '',
    }
  },

  methods: {
    onEnter() {
      if (this.myAnswer === this.answer) {
        window.alert('恭喜你答对了！');
      } else {
        window.alert('抱歉，回答错误！');
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
canvas {
  border: #999 solid 2px;
}
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
.header {
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 800px;
}
input {
  height: 30px;
  width: 350px;
  font-size: 16px;
  line-height: 30px;
  outline: none;
  padding: 0;
}
.Canvas {
  display: flex;
  justify-content: space-around;
}
</style>

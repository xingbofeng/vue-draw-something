<template>
  <div class="Canvas">
    <div>
      <div class="header">
        <h1><a href="/paintCanvas/index.html#/guess">我来猜</a></h1>
        <div>
          <input
            type="text"
            v-model.trim="answer"
            v-on:keyup.enter="onEnter"
            placeholder="在这里填写您的答案哟!别忘了Enter或者确定!"
          >
          <button v-on:click="onEnter">确定</button>
        </div>
      </div>
      <h1>你的答案是<span style="color: red;">{{ answer }}</span></h1>
      <canvas
        v-on:mousedown="paintBegin"
        v-on:touchstart="paintBegin"
        v-on:mouseup="paintEnd"
        v-on:touchend="paintEnd"
        id="canvas"
        width="800"
        height="500"
      ></canvas>
      <button v-on:click="clearPath">清除</button>
    </div>
  <Chatting person="painter"></Chatting>
  </div>
</template>

<script>
let ctx;
let socket = require('socket.io-client')('http://localhost:2017');
import Chatting from '../Chatting.vue';
export default {
  name: 'Canvas',
  components: {
    'Chatting': Chatting
  },
  mounted: function () {
    ctx = document.getElementById('canvas').getContext('2d');
  },
  data () {
    return {
      answer: '',
    }
  },
  methods: {
    paintBegin: function (e) {
      ctx.strokeStyle = "#000";
      ctx.beginPath();
      ctx.moveTo(e.offsetX, e.offsetY);
      socket.emit('begin', {
        left: e.offsetX,
        top: e.offsetY
      });
      document.onmousemove = this.painting;
      document.ontouchmove = this.painting;
    },
    painting: function (e) {
      ctx.lineTo(e.offsetX, e.offsetY);
      if (e.offsetX >=800 || e.offsetX <=0 || e.offsetY >= 500 || e.offsetY <= 0) {
        this.paintEnd();
        return;
      }
      socket.emit('paint', {
        left: e.offsetX,
        top: e.offsetY
      });
      ctx.stroke();
    },
    paintEnd: function (e) {
      document.onmouseup = null;
      document.ontouchend = null;
      document.onmousemove = null;
      document.ontouchmove = null;
    },
    clearPath: function () {
      ctx.clearRect(0, 0, 800, 500);
      socket.emit('clear');
    },
    onEnter: function () {
      socket.emit('answer', this.answer);
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

<template>
  <div class="Canvas">
    <h1><a href="/#/guess">我来猜</a></h1>
    <canvas
      v-on:mousedown="paintBegin"
      v-on:mouseup="paintEnd"
      id="canvas"
      width="800"
      height="500"
    ></canvas>
  <button v-on:click="clearPath">清除</button>
  </div>
</template>

<script>
let ctx;
let socket = require('socket.io-client')('http://angryzhangzhe.cn:2017');
socket.on('connect', function () {
  console.log('socket successful!');
});
export default {
  name: 'Canvas',
  mounted: function () {
    ctx = document.getElementById('canvas').getContext('2d');
  },
  data () {
    return {
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
    },
    painting: function (e) {
      ctx.lineTo(e.offsetX, e.offsetY);
      socket.emit('paint', {
        left: e.offsetX,
        top: e.offsetY
      });
      ctx.stroke();
    },
    paintEnd: function (e) {
      document.onmouseup = null;
      document.onmousemove = null;
    },
    clearPath: function () {
      ctx.clearRect(0, 0, 800, 500);
      socket.emit('clear');
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
}
</style>

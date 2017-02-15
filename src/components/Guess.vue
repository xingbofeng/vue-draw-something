<template>
  <div class="Canvas">
    <h1><a href="/paintCanvas/index.html#/paint">我来画</a></h1>
    <canvas
      id="canvas"
      width="800"
      height="500"
    ></canvas>
  </div>
</template>

<script>
export default {
  name: 'Guess',
  mounted: function () {
  	let ctx;
    ctx = document.getElementById('canvas').getContext('2d');
    let socket = require('socket.io-client')('http://angryzhangzhe.cn:2017');
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
		});
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
canvas {
  border: #999 solid 2px;
}
</style>

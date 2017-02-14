<template>
  <div class="Canvas">
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
export default {
  name: 'Canvas',
  mounted: function () {
    ctx = document.getElementById('canvas').getContext('2d');
    console.log(ctx);
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    paintBegin: function (e) {
      ctx.strokeStyle = "#000";
      ctx.beginPath();
      ctx.moveTo(e.offsetX, e.offsetY);
      document.onmousemove = this.painting;
    },
    painting: function (e) {
      ctx.lineTo(e.offsetX, e.offsetY);
      ctx.stroke();
    },
    paintEnd: function (e) {
      console.log(e);
      document.onmouseup = null;
      document.onmousemove = null;
    },
    clearPath: function () {
      ctx.clearRect(0, 0, 800, 500);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
canvas {
  border: #999 solid 2px;
}
</style>

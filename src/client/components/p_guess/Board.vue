<template>
  <mu-paper class="paper" :zDepth="3">
    <canvas
      ref="canvas"
      width="700"
      height="500"
    ></canvas>
  </mu-paper>
</template>

<script>
import socketClient from 'socket.io-client';

export default {
  name: 'Board',

  data() {
    return {
      socket: socketClient('http://localhost:2017'),
      ctx: {},
    }
  },

  mounted() {
    this.ctx = this.$refs.canvas.getContext('2d');
    this.socket.on('connect', () => this.connet());
  },

  methods: {
    connet() {
      this.socket.on('painting', this.painting);
      this.socket.on('began', this.began);
      this.socket.on('clear', this.clear);
    },

    painting(message) {
      this.ctx.lineTo(message.left, message.top);
      this.ctx.stroke();
    },

    began(message) {
      this.ctx.strokeStyle = "#000";
      this.ctx.beginPath();
      this.ctx.moveTo(message.left, message.top);
    },

    clear(message) {
      this.ctx.clearRect(0, 0, 800, 500);
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.paper {
  width: 700px;
  height: 500px;
}
</style>

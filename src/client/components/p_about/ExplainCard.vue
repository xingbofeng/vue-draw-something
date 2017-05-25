<template>
  <div class="ExplainCard">
    <div class="main">
      <img src="../../assets/draw-something.jpg" />
      <mu-card-title title="《你画我猜》游戏说明" />
      <mu-card-text>
        网页版《你画我猜》一般支持多人游戏，使用鼠标操作画笔画画，使用键盘输入进行作答。通过浏览器在线加载后，玩家登录并选择一个房间，等待其他玩家进入或存在至少2名玩家时可直接开始进行游戏。当提示轮到某位玩家时，需根据发挥自己的想象力绘画，其他玩家根据画面把自己认为的答案写入文本框，发送即可。游戏目标对于绘画玩家为让其他人理解自己描述的提示词，对于猜谜的玩家目标则是在尽可能短的时间获得正确答案。
      </mu-card-text>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ExplainCard',
}
</script>

<style scoped>
.ExplainCard {
  padding: 100px 0 0 0;
}

.main {
  width: 600px;
  margin-top: 50px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.explain {
  padding: 100px;
}
</style>

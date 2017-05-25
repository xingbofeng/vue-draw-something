<template>
  <div class="LoginBox">
    <mu-text-field
      label="请输入用户名"
      hintText="请输入用户名"
      type="text"
      labelFloat
      v-model="username"
    />
    <mu-text-field
      label="请输入密码"
      hintText="请输入密码"
      type="password"
      labelFloat
      v-model="password"
    />
    <mu-raised-button
      class="demo-raised-button"
      label="登录"
      @click.prevent.stop="login"
      primary
    />
  </div>
</template>

<script>
import config from '../../serverConfig';

export default {
  name: 'LoginBox',

  data() {
    return {
      username: '',
      password: '',
    }
  },

  methods: {
    login() {
      this.$store.dispatch('login', {
        data: {
          username: this.username,
          password: this.username,
        },
        next: this.callback,
      });
    },

    callback() {
      const argument = arguments[0];
      const path = (argument ? argument.path : '/');
      this.$router.push(path);
    },
  },
}
</script>

<style scoped>

.LoginBox {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 150px;
}

</style>

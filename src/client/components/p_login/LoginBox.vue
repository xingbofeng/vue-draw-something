<template>
  <mu-paper class="paper" :zDepth="3">
    <div class="LoginBox">
      <mu-dialog :open="isDialogShow">
        用户名或密码错误，请重新尝试登录~
        <mu-flat-button
          label="确定"
          slot="actions"
          primary
          @click="closeDialog"
        />
      </mu-dialog>
      <mu-sub-header>账号密码登录</mu-sub-header>
      <mu-text-field
        label="请输入账号"
        type="text"
        labelFloat
        v-model="username"
      />
      <mu-text-field
        label="请输入密码"
        type="password"
        labelFloat
        v-model="password"
      />
      <div class="buttons">
        <mu-raised-button
          label="登录"
          @click.prevent.stop="login"
          primary
        />
        <mu-raised-button
          label="注册"
          @click.prevent.stop="signup"
        />
      </div>
    </div>
  </mu-paper>
</template>

<script>
import config from '../../serverConfig';

export default {
  name: 'LoginBox',

  data() {
    return {
      username: '',
      password: '',
      isDialogShow: false,
    }
  },

  methods: {
    login() {
      this.$store.dispatch('login', {
        data: {
          username: this.username,
          password: this.password,
        },
        next: this.callback,
      });
    },

    signup() {
      this.$router.push('/signup');
    },

    callback() {
      const argument = arguments[0];
      // 登录失败则有argument
      const path = (argument ? argument.path : '/');
      if (argument) {
        this.isDialogShow = true;
      }
      this.$router.push(path);
    },

    closeDialog() {
      // 关闭提示框
      this.isDialogShow = false;
    },
  },
}
</script>

<style scoped>

.paper {
  position: absolute;
  left: 50%;
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  margin-top: 150px;
  padding: 30px;
}

.LoginBox {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.buttons {
  display: flex;
  margin-top: 20px;
  width: 100%;
  justify-content: space-around;
}

</style>

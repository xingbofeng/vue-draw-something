<template>
  <mu-paper class="paper" :zDepth="3">
    <div class="SignupBox">
      <mu-dialog :open="isDialogShow">
        {{ dialogText }}
        <mu-flat-button
          label="确定"
          slot="actions"
          primary
          @click="closeDialog"
        />
      </mu-dialog>
      <mu-sub-header>你画我猜 - 注册 @Encounter</mu-sub-header>
      <mu-text-field
        label="请输入账号"
        type="text"
        labelFloat
        v-model="username"
      />
      <mu-text-field
        label="请输入邮箱"
        type="email"
        labelFloat
        v-model="email"
      />
      <mu-text-field
        label="请输入昵称"
        type="text"
        labelFloat
        v-model="nickname"
      />
      <mu-text-field
        label="请输入密码"
        type="password"
        labelFloat
        v-model="password"
      />
      <mu-text-field
        label="确认密码"
        type="password"
        labelFloat
        v-model="confirmpassword"
      />
      <div class="sex">
        <span>请输入性别</span>
        <mu-radio
          class="sex-radio"
          label="男"
          name="sex"
          nativeValue="boy"
          v-model="sex"
          uncheckIcon="person"
          checkedIcon="done"
        />
        <mu-radio
          class="sex-radio"
          label="女"
          name="sex"
          nativeValue="girl"
          v-model="sex"
          uncheckIcon="pregnant_woman"
          checkedIcon="done"
        />
      </div>
      <mu-date-picker
        v-model="birthday"
        hintText="请输入生日"
      />
      <mu-raised-button
        label="立即注册"
        @click.prevent.stop="signup"
        primary
      />
    </div>
  </mu-paper>
</template>

<script>
import config from '../../serverConfig';

export default {
  name: 'SignupBox',

  data() {
    return {
      username: '', // 用户名
      password: '', // 密码
      confirmpassword: '', //确认密码
      email: '', //邮箱
      nickname: '', // 昵称
      birthday: '', // 生日
      sex: '', // 性别
      dialogText: '请核对密码是否一致',
      isDialogShow: false,
    }
  },

  methods: {
    signup() {
      if (this.password !== this.confirmpassword) {
        // 密码不一致的展示
        this.dialogText = '请核对密码是否一致';
        this.isDialogShow = true;
        return;
      }
      if (this.username &&
        this.password &&
        this.confirmpassword &&
        this.email &&
        this.nickname &&
        this.birthday &&
        this.sex
      ) {
        // 注册操作
        this.$store.dispatch('signup', {
          data: {
            username: this.username,
            password: this.password,
            email: this.email,
            nickname: this.nickname,
            birthday: this.birthday,
            sex: this.sex,
          },
          callback: this.callback,
        });
        return;
      }
      this.dialogText = '请检查每项信息是否填完';
      this.isDialogShow = true;
    },

    callback() {
      this.dialogText = '注册失败，请检查网络';
      this.isDialogShow = true;
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
  margin-top: 30px;
  padding: 30px;
}

.SignupBox {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sex {
  display: flex;
  align-items: center;
  width: 100%;
  padding: 28px 0 28px;
}

.sex span {
  color: rgba(0,0,0,.54);
  font-size: 16px;
}

.sex-radio {
  margin-left: 15px;
}

</style>

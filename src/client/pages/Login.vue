<template>
  <div class="Login">
    <layout>
      <login-box slot="content" />
    </layout>
  </div>
</template>

<script>
import Layout from '../components/Layout';
import LoginBox from '../components/p_login/LoginBox';

export default {
  name: 'Login',

  components: {
    Layout,
    LoginBox,
  },
}
</script>

<style scoped>

</style>

<template>
  <div class="Login">
    <layout>
      <signup-box slot="content" />
    </layout>
  </div>
</template>

<script>
import Layout from '../components/Layout';
import SignupBox from '../components/p_signup/SignupBox';

export default {
  name: 'Login',

  components: {
    Layout,
    SignupBox,
  },
}
</script>

<style scoped>

</style>

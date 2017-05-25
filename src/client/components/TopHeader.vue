<template>
  <header class="TopHeader">
    <mu-appbar title="vue-draw-something(基于Vue.js和Muse-UI制作的你画我猜小游戏)">
      <mu-icon-button
        icon="menu"
        slot="left"
        @click="toggle()"
      />
      <mu-flat-button
        :to="`${$store.state.login.status === 'success' ? '/' : '/login'}`"
        :label="$store.state.login.text"
        slot="right"
      />
    </mu-appbar>
  </header>
</template>

<script>
import { LEFT_DRAWER } from '../store/mutation-types';

export default {
  name: 'TopHeader',

  methods: {
    toggle (flag) {
      const {
        open,
        docked
      } = this.$store.state.leftDrawer;

      this.$store.commit(LEFT_DRAWER, {
        open: !open,
        docked: !flag,
      });
    },
  },
}
</script>

<style scoped>

</style>

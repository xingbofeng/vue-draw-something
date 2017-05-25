<template>
  <header class="TopHeader">
    <mu-appbar title="你画我猜">
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
      <mu-flat-button
        v-show="$store.state.login.status === 'success'"
        @click="logout"
        label="注销"
        slot="right"
      />
    </mu-appbar>
  </header>
</template>

<script>
import { mapActions } from 'vuex';
import { LEFT_DRAWER } from '../store/mutation-types';

export default {
  name: 'TopHeader',

  methods: {
    ...mapActions(['logout']),
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

<template>
  <div class="LeftDrawer">
    <mu-drawer
      :open="open"
      :docked="docked"
      @close="toggle()"
      width="300"
    >
      <router-link
        to="/"
      >
        <mu-appbar>
          draw-something @
          <img
            src="./../assets/logo.jpeg"
            class="logo"
          />
        </mu-appbar>
      </router-link>
      <mu-list>
        <mu-list-item
          title="我来画"
          to="/paint"
        />
        <mu-list-item
          title="我来猜"
          to="/guess"
        />
        <mu-list-item
          title="关于"
          to="/about"
        />
        <mu-list-item
          title="去GitHub查看源码"
          href="https://github.com/xingbofeng/vue-draw-something"
        />
      </mu-list>
    </mu-drawer>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import { LEFT_DRAWER } from '../store/mutation-types';

export default {
  name: 'LeftDrawer',

  computed: {
    ...mapState({
      open: state => state.leftDrawer.open,
      docked: state => state.leftDrawer.docked,
    }),
  },

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
.logo {
  height: 50px;
  margin: 0 50px -14px 0px;
}

</style>

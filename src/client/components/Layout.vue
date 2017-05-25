<template>
  <div class="Layout">
    <left-drawer />
    <main
      :class="{ active: $store.state.leftDrawer.open }"
    >
      <top-header />
      <slot name="content" />
    </main>
  </div>
</template>

<script>
import TopHeader from './TopHeader';
import LeftDrawer from './LeftDrawer';

export default {
  name: 'Layout',

  components: {
    TopHeader,
    LeftDrawer,
  },
}
</script>

<style scoped>

main.active {
  width: calc(100% - 300px);
  margin-left: 300px;
}

</style>

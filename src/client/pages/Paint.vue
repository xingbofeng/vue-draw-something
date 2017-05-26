<template>
  <div class="Paint">
    <layout>
      <paint-content
        slot="content"
      />
    </layout>
  </div>
</template>

<script>
import Layout from '../components/Layout';
import PaintContent from '../components/p_paint/PaintContent';

export default {
  name: 'Paint',

  components: {
    Layout,
    PaintContent,
  },
}
</script>

<style scoped>

</style>

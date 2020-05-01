<template>
  <div class="head-icon">
    <div class="head-ico">
      <img src="../assets/ico.png"/>
    </div>
    <div class="head-title" v-if="active">
      FunCMS
    </div>
  </div>
</template>

<script>
  export default {
    name: "HeadIcon",
    props: {
      active: {
        type: Boolean,
        default: true
      }
    }
  }
</script>

<style scoped>
  .head-icon {
    display: flex;
    padding: 0 15px;
    height: 60px;
    box-shadow: 0 0 3px #cbcbcb;
    position: relative;
    z-index: 10;
  }

  .head-ico {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    cursor: pointer;
    filter: brightness(97%);
    transition: all .3s;
  }

  .head-ico:hover {
    filter: brightness(100%);
  }

  .head-title {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin-left: 15px;
    font-size: 16pt;
    color: #404040;
  }
</style>
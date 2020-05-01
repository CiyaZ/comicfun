<template>
  <div id="app">
    <main-frame></main-frame>
  </div>
</template>

<script>
import MainFrame from './pages/MainFrame'

export default {
  name: 'app',
  components: {
      MainFrame
  }
}
</script>

<style>
  @import './assets/css/app.css';
</style>
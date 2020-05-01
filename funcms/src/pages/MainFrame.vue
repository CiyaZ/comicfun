<template>
  <div>
    <el-container style="height: 100vh;">
      <el-aside :class="isCollapse?'collapsed':'uncollapsed'" width="201px"
                style="overflow: hidden">
        <head-icon :active="active"></head-icon>
        <div class="menu-container">
          <el-menu class="el-menu-vertical"
                   :collapse="isCollapse">
            <el-menu-item index="1">
              <i class="el-icon-odometer"></i>
              <span slot="title">仪表盘</span>
            </el-menu-item>
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-coin"></i>
                <span slot="title">内容管理</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="2-1">分类标签</el-menu-item>
                <el-menu-item index="2-2">数据标签</el-menu-item>
                <el-menu-item index="2-3">Artifact视图</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="3">
              <template slot="title">
                <i class="el-icon-notebook-2"></i>
                <span slot="title">小说专区</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="3-1">小说管理</el-menu-item>
                <el-menu-item index="3-2">采集器配置</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="4">
              <template slot="title">
                <i class="el-icon-orange"></i>
                <span slot="title">漫画专区</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="4-1">漫画管理</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="5">
              <template slot="title">
                <i class="el-icon-video-camera-solid"></i>
                <span slot="title">动画专区</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="5-1">动画管理</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="6">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span slot="title">广告专区</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="6-1">宣传画</el-menu-item>
                <el-menu-item index="6-2">更新速递</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="7">
              <template slot="title">
                <i class="el-icon-user"></i>
                <span slot="title">用户管理</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="7-1">用户管理</el-menu-item>
                <el-menu-item index="7-2">评论管理</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="8">
              <template slot="title">
                <i class="el-icon-data-line"></i>
                <span slot="title">统计日志</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="8-1">内容统计</el-menu-item>
                <el-menu-item index="8-2">流量统计</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="9">
              <template slot="title">
                <i class="el-icon-setting"></i>
                <span slot="title">站点配置</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="9-1">主题管理</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </div>
      </el-aside>
      <el-container>
        <el-header class="frame-header">
          <aside-collapse-button :active="active" @toggle="toggle"></aside-collapse-button>
        </el-header>
        <el-main>开发中(⊙x⊙;)</el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  import AsideCollapseButton from '../components/AsideCollapseButton'
  import HeadIcon from '../components/HeadIcon'

  export default {
    name: "MainFrame",
    components: {
      AsideCollapseButton,
      HeadIcon
    },
    data: function () {
      return {
        isCollapse: false
      }
    },
    computed: {
      active: function () {
        return !this.isCollapse;
      }
    },
    methods: {
      toggle: function () {
        this.isCollapse = !this.isCollapse;
      }
    }
  }
</script>

<style scoped>
  .el-menu-vertical:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }

  .el-header {
    box-shadow: 0 1px 1px #f2f2f2;
  }

  .el-main {
    overflow-y: auto;
    overflow-x: hidden;
  }

  .collapsed {
    animation: collapse .4s;
    animation-fill-mode: forwards;
  }

  .menu-container {
    overflow-y: auto;
    overflow-x: hidden;
    height: calc(100vh - 60px);
  }

  @keyframes collapse {
    0% {
      width: 201px;
    }
    100% {
      width: 65px;
    }
  }

  .uncollapsed {
    animation: uncollapse .4s;
    animation-fill-mode: forwards;
  }

  @keyframes uncollapse {
    0% {
      width: 65px;
    }
    100% {
      width: 201px;
    }
  }

  .frame-header {
    display: flex;
  }
</style>
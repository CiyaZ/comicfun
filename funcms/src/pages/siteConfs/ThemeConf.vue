<template>
  <div v-loading="loading">
    <el-card shadow="never">
      <div slot="header">
        <span>主题管理</span>
      </div>
      <div>
        <el-form ref="themeForm" :rules="rules" :model="themeForm" label-width="100px">
          <el-form-item label="主颜色值" prop="mainColor">
            <el-color-picker v-model="themeForm.mainColor"></el-color-picker>
          </el-form-item>
          <el-form-item label="背景图链接" prop="bgImageUrl">
            <el-input v-model="themeForm.bgImageUrl"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit" :loading="submitBtnLoading">确认</el-button>
            <el-button type="warning" @click="onReset">重置</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-card>
  </div>
</template>

<script>
  import axios from 'axios'
  import {rspStatusHandler} from "../../consts";

  export default {
    name: 'ThemeConf',
    data() {
      return {
        loading: false,
        submitBtnLoading: false,
        // 表单初始值
        themeFormInit: {
          mainColor: '',
          bgImageUrl: ''
        },
        // 表单绑定模型
        themeForm: {
          mainColor: '',
          bgImageUrl: ''
        },
        // 表单验证规则
        rules: {
          bgImageUrl: [
            {type: 'url', message: '请输入正确的链接格式', trigger: 'change'},
            {max: 255, message: '链接不能超过255个字符', trigger: 'change'}
          ]
        }
      }
    },
    created() {
      this.loading = true;
      axios
          .get('/backend/api/confs')
          .then((resp) => {
            console.log(resp);
            this.loading = false;
            let data = resp.data.data;
            for (let conf of data) {
              let conf_key = conf.conf_key;
              let conf_value = conf.conf_value;

              switch (conf_key) {
                case 'site_theme_color':
                  this.themeFormInit.mainColor = this.themeForm.mainColor = `${ conf_value }`;
                  break;
                case 'site_background':
                  this.themeFormInit.bgImageUrl = this.themeForm.bgImageUrl = conf_value;
                  break;
              }
            }
          })
          .catch((err) => {
            console.error(err);
            this.loading = false;
            let status = err.response.status;
            this.$message.error(rspStatusHandler('NET', status));
            if (status === 403){
              this.$router.push('/login');
            }
          });
    },
    methods: {
      onSubmit() {
        let that = this;
        this.$refs.themeForm.validate((valid) => {
          if (valid) {
            this.submitBtnLoading = true;
            axios
                .post('/backend/api/confs', this.themeForm, {
                  headers: {'X-CSRFToken': that.$cookies.get('csrftoken')}
                })
                .then((resp) => {
                  console.log(resp);
                  this.submitBtnLoading = false;
                  this.$message.success('保存成功');
                })
                .catch((err) => {
                  console.error(err);
                  this.submitBtnLoading = false;
                  let status = err.response.status;
                  this.$message.error(rspStatusHandler('NET', status));
                  if (status === 403){
                    this.$router.push('/login');
                  }
                });
          }
        });
      },
      onReset() {
        this.themeForm.mainColor = this.themeFormInit.mainColor;
        this.themeForm.bgImageUrl = this.themeFormInit.bgImageUrl;
      }
    }
  }
</script>

<style scoped>
  form {
    width: 460px;
  }
</style>
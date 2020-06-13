<template>
  <div class="bg-gray">
    <div class="login-title">
      FunCMS
    </div>
    <div class="login-card-container">
      <div class="login-card">
        <el-card shadow="never">
          <div slot="header">
            <span>管理后台登录</span>
          </div>
          <div>
            <el-form ref="loginForm" :rules="rules" :model="loginForm" label-width="70px">
              <el-form-item label="用户名" prop="username">
                <el-input v-model="loginForm.username"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="loginForm.password"></el-input>
              </el-form-item>
              <el-form-item label="验证码" prop="captcha">
                <el-input v-model="loginForm.captcha" class="captcha-input"></el-input>
                <img :src="captcha.imgUrl" class="captcha" @click="refreshCaptcha"/>
              </el-form-item>
              <el-form-item class="pull-right">
                <el-button type="primary" @click="onSubmit" :loading="submitBtnLoading">登录</el-button>
                <el-button type="warning" @click="onReset">重置</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import {rspStatusHandler} from "../consts";
  import CanvasNest from '../components/CanvasNest';

  export default {
    name: "Login",
    comments: {
      CanvasNest
    },
    created() {
      this.refreshCaptcha();
    },
    mounted() {
      document.addEventListener('keyup', (ev) => {
        if (ev.code === 'Enter') {
          this.onSubmit();
        }
      });
    },
    data() {
      return {
        captcha: {
          captchaKey: '',
          imgUrl: ''
        },
        loginForm: {
          username: '',
          password: '',
          captcha: ''
        },
        rules: {
          username: [
            {required: true, message: '请输入用户名', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ],
          captcha: [
            {required: true, message: '请输入验证码', trigger: 'blur'},
            {min: 4, max: 4, message: '请输入正确的验证码格式', trigger: 'blur'},
          ],
        },
        submitBtnLoading: false
      }
    },
    methods: {
      refreshCaptcha() {
        axios
            .get('/backend/api/captcha')
            .then((resp) => {
              console.log(resp);
              let data = resp.data.data;
              this.captcha.captchaKey = data.captcha_key;
              this.captcha.imgUrl = data.img_url;
            })
            .catch((err) => {
              console.error(err);
              let status = err.response.status;
              this.$message.error(rspStatusHandler('NET', status));
            });
      },
      onSubmit() {
        let that = this;
        this.$refs.loginForm.validate((valid) => {
          if (valid) {
            this.submitBtnLoading = true;
            axios
                .post('/backend/api/login', {
                  username: this.loginForm.username,
                  password: this.loginForm.password,
                  captchaKey: this.captcha.captchaKey,
                  captchaValue: this.loginForm.captcha
                }, {
                  headers: {'X-CSRFToken': that.$cookies.get('csrftoken')}
                })
                .then((resp) => {
                  console.log(resp);
                  this.submitBtnLoading = false;
                  let rsp = resp.data;
                  if (rsp.rspCode !== '0') {
                    this.$message.error(rsp.rspMsg);
                    this.refreshCaptcha();
                  } else {
                    this.$message.success('登陆成功');
                    this.$router.push('/')
                  }
                })
                .catch((err) => {
                  console.error(err);
                  this.submitBtnLoading = false;
                  let status = err.response.status;
                  this.$message.error(rspStatusHandler('NET', status));
                });
          }
        });
      },
      onReset() {
        this.$refs.loginForm.resetFields();
      }
    }
  }
</script>

<style scoped>
  .bg-gray {
    background-color: rgba(233, 234, 235, .4);
    height: 100vh;
    overflow: hidden;
  }

  .login-title {
    text-align: center;
    position: relative;
    font-size: 23pt;
    margin-top: 7rem;
    color: #6a6a6a;
  }

  .login-card-container {
    margin-top: 2rem;
  }

  .login-card {
    width: 370px;
    margin: 0 auto;
  }

  .pull-right {
    float: right;
  }

  .captcha-input {
    width: 10rem;
  }

  .captcha {
    float: right;
    margin-top: .1rem;
    cursor: pointer;
  }
</style>
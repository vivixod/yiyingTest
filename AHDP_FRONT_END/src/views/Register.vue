<template>
    <el-row class="login-container">
      <!-- 左侧放置图片 -->
      <el-col :span="12">
        <img src="../assets/miu.png" alt="Logo" class="login-image">
      </el-col>
      <!-- 右侧登录输入框 -->
      <el-col :span="12">
        <el-card class="login-card" shadow="hover">
            <template #header>
                <h2 class="login-title">Register</h2>
            </template>
            <el-form ref="registerForm" :model="registerForm" :rules="rules" label-width="100px" class="login-form">
                <el-form-item label="Username" prop="username">
                    <el-input v-model="registerForm.user_name" placeholder="Enter your username"></el-input>
                </el-form-item>
                <el-form-item label="Password" prop="password">
                    <el-input type="password" v-model="registerForm.user_password" placeholder="Enter your password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="register">Register</el-button>
                </el-form-item>
            </el-form>
        </el-card>
      </el-col>
    </el-row>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        registerForm: {
          user_name: '',
          user_password: ''
        },
        rules: {
          user_name: [
            { required: true, message: 'Please enter your username', trigger: 'blur' }
          ],
          user_password: [
            { required: true, message: 'Please enter your password', trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      register() {
        this.$refs.registerForm.validate((valid) => {
          if (valid) {
            axios.post('/api/register', this.registerForm).then(res =>{
                if(res.data.status=='success')
                    console.log('success')
            })
            this.$router.push('/');
          } else {
            return false;
          }
        });
      }
    }
  };
  </script>
  
  <style scoped>
  .login-container {
    height: 100vh;
    align-items: center;
    justify-content: center;
  }
  
  .login-image {
    width: 400px;
    max-width: 100%;
    height: 400px;
  }
  
  .login-card {
    height: 400px;
    width: 400px;
  }
  
  .login-title {
    text-align: center;
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .login-form {
    margin-top: 20px;
  }
  </style>
  
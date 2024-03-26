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
                <h2 class="login-title">Login</h2>
            </template>
            <el-form ref="loginForm" :model="loginForm" :rules="rules" label-width="100px" class="login-form">
                <el-form-item label="Username" prop="username">
                    <el-input v-model="loginForm.user_name" placeholder="Enter your username"></el-input>
                </el-form-item>
                <el-form-item label="Password" prop="password">
                    <el-input type="password" v-model="loginForm.user_password" placeholder="Enter your password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="login">Login</el-button>
                </el-form-item>
            </el-form>
            <el-form-item>
                <el-button @click="register">Register</el-button>
            </el-form-item>
        </el-card>
      </el-col>
    </el-row>
</template>
  
<script>
import axios from 'axios'
export default {
    data() {
      return {
        loginForm: {
          user_name: '',
          user_password: ''
        },
        rules: {
          user_name: [
            { required: true, message: 'Please enter your username', trigger: 'blur' },
          ],
          user_password: [
            { required: true, message: 'Please enter your password', trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
        login() {
        this.$refs.loginForm.validate((valid) => {
          if (valid) {
            axios.post('/api/login', this.loginForm).then(res =>{
                if(res.data.status=='success'){
                    console.log('success')
                    this.$router.push('/about');
                }
                if(res.data.code==1){
                    console.log(res)
                    this.$message.error('该用户不存在');
                }
                if(res.data.code==2){
                    this.$message.error('密码错误');
                }
          }) 
        }
      })
      },
      
      register(){
        this.$router.push('/register');
      }
    }
}

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
  
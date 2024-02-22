<template>
    <div>
        <Login></Login>
    </div>
</template>
  
<script>
    import Login from '@/views/Login.vue';
    import {reactive,toRefs} from "vue"
    export default{
        setup(){
            const data = reactive({
            name:"ztt",
            age:20
            })
    
            return{
            ...toRefs(data)//toRefs的数据在template里面不能用data.什么什么，直接用里面的内容(如name)
            }
        },

        components: {
            Login
        }
    }
</script>
  
  
  <style>
  
  .chart {
    height: 400px;
  }
  </style>
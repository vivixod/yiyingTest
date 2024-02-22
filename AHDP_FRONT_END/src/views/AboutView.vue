<template>
  <h1 style="text-align: center">图书管理</h1>
  <el-button type="primary" @click="add_dialog_visbale = true" size="small">添加图书</el-button>
  <el-table :data="books" style="margin: 20px auto;">
    <el-table-column label="编号" prop="book_number"/>
    <el-table-column label="书名" prop="book_name"/>
    <el-table-column label="类型" prop="book_type"/>
    <el-table-column label="价格" prop="book_price"/>
    <el-table-column label="作者" prop="author"/>
    <el-table-column label="出版社" prop="publisher"/>
    <el-table-column align="right" label="操作" width="200px">
      <template #default="scope">
        <el-button size="small" @click="handleEdit(scope.$index, scope.row)">
          编辑
        </el-button>
        <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">
          删除
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script setup>
  import axios from 'axios'
  import { reactive, onMounted } from 'vue';
  // import { ElMessageBox } from 'element-plus';

  const books = reactive([])
  const getstudents = () =>{
    axios.get("/api/books",).then(res =>{
      books.splice(0,books.length)
      books.push(...res.data.results)
      console.log(res)
      console.log('更新数据')
    })
  }

  onMounted(() => {
    getstudents()
  })

  const handleDelete = (index, scope) => {
    axios.delete(`http://localhost:5000/books/${scope.id}`).then(() =>{
      getstudents()
    })
  }

  // const handleEdit = (index, scope) => {
  //   console.log(index, row)
  // }

</script>
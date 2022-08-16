<template>
  <div>
    <h1>项目设置页</h1>
    <el-form ref="form" :model="form_data" label-width="120px" :label-position="'left'">
      <el-form-item label="项目名称">
        <el-input v-model="form_data.name"></el-input>
      </el-form-item>

      <el-form-item label="项目描述">
        <el-input v-model="form_data.des"></el-input>
      </el-form-item>

      <el-form-item label="私密项目">
        <el-switch v-model="form_data.private"></el-switch>
      </el-form-item>

      <el-form-item label="编辑权限">
        <el-switch v-model="form_data.power"></el-switch>
        <el-checkbox label="自己" name="type"></el-checkbox>
        <el-checkbox label="领导" name="type"></el-checkbox>
        <el-checkbox label="同事" name="type"></el-checkbox>
        <el-checkbox label="所有人" name="type"></el-checkbox>
      </el-form-item>

      <el-form-item label="业务线">
        <el-select v-model="form_data.Line" placeholder="请选择项目业务线">
          <el-option label="APP线" value="app"></el-option>
          <el-option label="WEB线" value="web"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="邮箱接收者列表">
        <el-input v-model="form_data.email_to"></el-input>
      </el-form-item>

      <el-form-item label="数据库地址IP">
        <el-input v-model="form_data.sql_host" style="width: 300px"></el-input>
      </el-form-item>

      <el-form-item label="数据库端口号">
        <el-input v-model="form_data.sql_port" style="width: 192.5px"></el-input>
      </el-form-item>

      <el-form-item label="数据库用户名">
        <el-input v-model="form_data.sql_user" style="width: 300px"></el-input>
      </el-form-item>

      <el-form-item label="数据库密码">
        <el-input v-model="form_data.sql_pwd" style="width: 300px"></el-input>
      </el-form-item>

      <el-form-item label="具体库名">
        <el-input v-model="form_data.sql_db" style="width: 300px"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="Save_project">保存生效</el-button>
      </el-form-item>

    </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Project_set",
  data() {
    return {
      form_data: {
        name: '',
        des: '',
        private: '',
        power: '',
        Line: '',
        email_to: '',
        sql_host: '',
        sql_port: '',
        sql_user: '',
        sql_pwd: '',
        sql_db: '',


      }
    }
  },
  methods: {
    Save_project() {
      axios.post('http://localhost:8000/save_project/', this.form_data).then(
          this.$message({
            message: "保存成功",
            type: 'success',
          })
      )
    }
  },
  mounted: function () {
    axios.get('http://localhost:8000/get_project_detail/', {
      params: {
        id: this.project_id
      }
    }).then(res => {
      this.form_data = res.data
    })
  },
  props: ["project_id"]
}
</script>

<style scoped>

</style>
<template>
  <div style="height: 100%">
    <el-container style="height: 100%">
      <el-aside width="200px">
        <Menu></Menu>
      </el-aside>

      <el-container>
        <el-header style="line-height: 60px">
          <el-input
              placeholder="请输入项目名称、描述的关键字，回车搜索"
              prefix-icon="el-icon-search"
              style="width: 333px;"
              v-model="keys"
              @change="change_search"
          >
          </el-input>
        </el-header>

        <el-main>
          <el-table
              :data="project_list_data"
              stripe
              style="min-width: 100%;min-height: 100%;overflow-y: auto"
          >
            <el-table-column
                prop="id"
                label="ID"
                width="100"
            >
            </el-table-column>
            <el-table-column
                prop="name"
                label="名称"
                width="300"
            >
            </el-table-column>
            <el-table-column
                prop="creater_name"
                label="创建者"
                width="200"
            >
            </el-table-column>
            <el-table-column
                prop="des"
                label="描述"
            >
            </el-table-column>

            <el-table-column>

              <template slot="header">
                <el-button style="width: 121px" @click="Add_project()">新增项目</el-button>
              </template>
              <template slot-scope="scope">
                <router-link :to="'/project_detail?project_id='+scope.row.id">
                  <el-button
                      size="mini"
                      type="primary"
                  >进入
                  </el-button>
                </router-link>
                &nbsp;
                <el-button
                    size="mini"
                    type="danger"
                    @click="Delete_project(scope.row.id)"
                >删除
                </el-button>
              </template>

            </el-table-column>

          </el-table>

        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Menu from '../components/Menu.vue'
import axios from "axios"

export default {
  name: "Project_list",
  data() {
    return {
      keys: '',
      project_list_data: []
    }
  },

  methods: {
    change_search() {
      axios.get('http://localhost:8000/get_project_list/', {
        params: this.keys
      }).then(res => {
        this.project_list_data = res.data
      })
    },
    Delete_project(project_id) {
      axios.get('http://localhost:8000/delete_project/', {
        params: {
          project_id: project_id
        }
      }).then(res => {
        this.project_list_data = res.data
      })
    },
    Add_project() {
      axios.get('http://localhost:8000/add_project/').then(res => {
        this.project_list_data = res.data
      })
    },
  },

  mounted() {//进入页面响应，然后进入url配置
    axios.get('http://localhost:8000/get_project_list/').then(res => {
      this.project_list_data = res.data
    })
  },

  components: {
    Menu,
  },
}
</script>

<style scoped>
.el-header {
  background: linear-gradient(to right, #d7f7ff, #ffedfd);
  color: #333;
  text-align: center;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
}

.el-main {
  background-color: white;
  color: #333;
}
</style>
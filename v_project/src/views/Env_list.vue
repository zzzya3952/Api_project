<template>
  <div style="height: 100%">
    <el-container style="height: 100%">
      <el-aside width="200px">
        <Menu></Menu>
      </el-aside>

            <el-main>
                <h1>环境管理 <span style="color: grey;font-size: xx-small">（此页面请不要随意删除环境）</span></h1>

                <el-table
                    :data="env_list_data"
                    stripe
                    border
                    style="min-width: 100%;min-height: 100%;overflow-y: auto"
                >
                    <el-table-column
                        prop="id"
                        label="ID"
                        width="100"
                    >
                    </el-table-column>

                    <el-table-column
                        prop="type"
                        label="标签"
                        width="200"
                    >
                        <template slot-scope="scope">
                            <el-tag>{{ scope.row.type }}</el-tag>
                        </template>
                    </el-table-column>

                    <el-table-column
                        prop="host"
                        label="域名"
                        width="300"
                    >

                    </el-table-column>

                    <el-table-column
                        prop="des"
                        label="描述"
                    >

                    </el-table-column>

                    <el-table-column>
                        <template slot="header">
                            <el-button @click="dialogFormVisible=true">新增环境</el-button>
                        </template>
                        <template slot-scope="scope">
                            <el-button size="mini" type="danger"  @click="Delete_env(scope.row.id)">删除</el-button>
                        </template>
                    </el-table-column>



                </el-table>
            </el-main>
    </el-container>
  </div>
</template>

<script>
import Menu from "../components/Menu";

export default {
  name: "Env_list.vue",
  data() {
    return {
      Env_list_data
    }
  },
  components: {
    Menu
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
<template>
    <div style="height: 100%">
        <el-container style="height: 100%">
            <el-aside  width="200px">
                <Menu></Menu>
            </el-aside>
            <el-main>
                <span style="float: right">项目ID: {{ $route.query.project_id }}</span>
                <el-tabs v-model="tab_name">
                    <el-tab-pane label="项目设置" name="first">
                        <Project_set :project_id="$route.query.project_id"></Project_set>
                    </el-tab-pane>

                     <el-tab-pane label="接口用例" name="second">
                        <Project_case :project_id="$route.query.project_id"></Project_case>
                    </el-tab-pane>

                </el-tabs>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import Menu from '../components/Menu.vue'
    import axios from 'axios'
    import Project_set from '../components/Project_set'
    import Project_case from '../components/Project_case'

    export default {
        name: "Project_list",
        data(){
            return{
                tab_name:'first'
            }
        },
        methods:{

        },
        mounted(){

        },
        components: {
          Menu,
            Project_set,
            Project_case,
       },
    }
</script>

<style scoped>
   .el-header {
    background:linear-gradient(to right, #d7f7ff, #ffedfd);
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
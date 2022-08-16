<template>
  <div id="home" style="height: 100%">
   <el-container style="height: 100%">
      <el-aside width="200px">
            <Menu></Menu>
      </el-aside>
      <el-container>
        <el-header>
            <el-row :gutter="5" style='margin-top: 5px'>
                <el-col :span="6">
                    <div class="staticbanner" style="background-color: #3a8ee6">
                        <div class="title">
                            <p>官方接口: {{ real_time_datas.ApiShop_count }}</p>
                            <el-tag size="mini">实时</el-tag>
                        </div>
                    </div>
                </el-col>

                <el-col :span="6">
                    <div class="staticbanner" style="background-color: #e6a703">
                        <div class="title">
                            <p>未读消息: {{ real_time_datas.UnReadNews_count }}</p>
                            <el-tag size="mini" style="color: #e6a703">实时</el-tag>
                        </div>
                    </div>
                </el-col>

                <el-col :span="6">
                    <div class="staticbanner" style="background-color: #02b426">
                        <div class="title">
                            <p>用例执行次数: {{ real_time_datas.RunCase_count }}</p>
                            <el-tag size="mini" style="color: #02b426">实时</el-tag>
                        </div>
                    </div>
                </el-col>

                <el-col :span="6">
                    <div class="staticbanner" style="background-color: #747474">
                        <div class="title">
                            <p>导入接口次数: {{ real_time_datas.Import_count }}</p>
                            <el-tag size="mini" style="color: #747474">实时</el-tag>
                        </div>
                    </div>
                </el-col>
            </el-row>

        </el-header>
        <el-main>
            <el-card class="box-card" style=";width: 30%;float: left;margin-right: 1px">
              <div slot="header" class="clearfix">
                <span>项目总览</span>
              </div>
                <p>项目总数：{{tj_datas.overview.project_count}}</p>
                <p>接口总数：{{tj_datas.overview.api_count}}</p>
                <p>用例总数：{{tj_datas.overview.case_count}}</p>
                <p>环境总数：{{tj_datas.overview.env_count}}</p>
                <p>用户总数：{{tj_datas.overview.user_count}}</p>
            </el-card>

            <el-card class="box-card" style="width:-webkit-calc(70% - 20px)">
              <div slot="header" class="clearfix">
                <span>上次监控情况</span>
              </div>
                <span style="font-size: xx-small">用例通过率</span>
                <el-progress style="margin-bottom: 10px;" :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitor.case_pass"></el-progress>
                <span  style="font-size: xx-small">接口通过率</span>
                <el-progress style="margin-bottom: 10px" :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitor.api_pass" status="success"></el-progress>
                <span  style="font-size: xx-small">用例失败/报错率</span>
                <el-progress style="margin-bottom: 10px" :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitor.case_fail" status="exception"></el-progress>
            </el-card>


             <el-card class="box-card" style="float: left;width:-webkit-calc(70% - 20px);margin-right: 1px">
              <div slot="header" class="clearfix">
                <span>个人贡献</span>
              </div>
                 <table class="table">
                     <thead>
                        <tr>
                            <th>个人项目占比</th>
                            <th>个人用例占比</th>
                            <th>个人接口占比</th>
                            <th>监控贡献占比</th>
                        </tr>
                     </thead>
                     <tbody>
                        <tr>
                            <td><el-progress type="circle" :percentage="tj_datas.contribution.project"></el-progress></td>
                            <td><el-progress type="circle" :percentage="tj_datas.contribution.case"  color="#2c3e50"></el-progress></td>
                            <td><el-progress type="circle" :percentage="tj_datas.contribution.api" color="green"></el-progress></td>
                            <td><el-progress type="circle" :percentage="tj_datas.contribution.monitor" color="indianred"></el-progress></td>
                        </tr>
                     </tbody>
                 </table>
            </el-card>

            <el-card class="box-card" style="overflow-y: auto;width: 30%;">
              <div slot="header" class="clearfix">
                <span>待处理消息</span>
                  <a href="#/send_news/"><el-button style="float: right; padding: 3px 0" type="text">进入详情</el-button></a>
              </div>
                <div v-for="o in tj_datas.news" class="text item">
                    {{o.from_user_name+' 的消息： ' + o.content }}
                  </div>
            </el-card>

        </el-main>
        <el-footer style="min-height: 110px;padding-top: 15px;text-align: left">
            <el-card class="box-card" style="overflow-y: auto;width: 100%;min-height: 90%;">
              <div v-for="o in tj_datas.notices"  class="text item">
                {{'平台更新日志： ' + o.content }}
              </div>
            </el-card>
        </el-footer>
      </el-container>
    </el-container>

  </div>
</template>

<script>
    import Menu from '../components/Menu.vue'
    import axios from 'axios'

    export default {
      name: 'home',
      data() {
          return {
            tj_datas:{
                notices:[],
                news:[],
                overview:{
                    project_count:0,
                    api_count:0,
                    case_count:0,
                    env_count:0,
                    user_count:0
                },
                monitor:{
                    case_pass:0,
                    api_pass:0,
                    case_fail:0
                },
                contribution:{
                    project:0,
                    case:0,
                    api:0,
                    monitor:0
                }
            },
            real_time_datas:{
                ApiShop_count:0,
                UnReadNews_count:0,
                RunCase_count:0,
                Import_count:0,
            }
          };
        },
      methods:{

      },
      components: {
          Menu,
      },
      mounted:function () {
        axios('http://localhost:8000/get_tj_datas/').then(res=>{
           this.tj_datas = res.data;
        });
        axios.get('http://localhost:8000/get_real_time_datas/').then(
            res=>{
                this.real_time_datas = res.data
            });
        setInterval(()=>{
            axios.get('http://localhost:8000/get_real_time_datas/').then(
                res=>{
                    this.real_time_datas = res.data
                }
            )},100000
        )

      }
    }
</script>

<style>
   .el-header, .el-footer {
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
  .el-card{
      background-color: white;
      text-align: left;
      overflow-y: auto;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 0;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
    .box-card{
        max-height: 49%;
        min-height: 49%;
    }
    th,td{
        text-align: center;
        font-size: xx-small;
        width: 20%;
    }
    .staticbanner{
        color: white;
        height: 50px;
        border-radius: 3px;
        padding: 0 8px;
    }
    .title{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    p{
        font-size: 13px;
        font-weight: bold;
    }
</style>
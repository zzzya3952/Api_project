import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import project_list from "@/views/Project_list";
import project_detail from "@/views/Project_detail";
import Env from "@/views/Env_list";
import Env_list from "@/views/Env_list";


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            component: Home
        },

        {
            path: '/project_list',
            component: project_list
        },
        {
            path: '/project_detail',
            component: project_detail
        },
        {
            path: '/Env_list',
            component: Env_list
        },


        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
        }
    ]
})

import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListUser from '@/components/Usuarios/ListUser'
import EditarUsuario from '@/components/Usuarios/EditarUsuario'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/usuarios',
      name: 'ListUser',
      component: ListUser
    },
    {
      path: '/usuarios/editar',
      name: 'EditarUsuario',
      component: EditarUsuario
    }
  ],
  mode: 'history'
})

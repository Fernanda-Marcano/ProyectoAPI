<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de usuarios</h2>
                <div class="col-md-12">
                    <b-table striped hover :items="usuario" :fields="fields">                        
                        <template slot="action" slot-scope="data">
                                <b-button size="sm" variant="primary" :to="{ name:'EditarUsuario', params: {userId: data.item.id} }">Editar</b-button>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'; 

    export default 
    {
        data() 
        {
            return {
                fields: [
                    {key: 'id', label: 'id'},
                    {key: 'username', label: 'username'},
                    {key: 'email', label: 'email'},
                    {key: 'nombres', label: 'nombres'},
/*                     {key: 'apellido', label: 'apellido'}, */
/*                     {key: 'estado', label: 'estado'}, */
                    {key: 'is_staff', label: 'staff'}
                ],
                usuario: []
            }
        },
        methods: { 
                getUsuario() {
                    const path = 'http://127.0.0.1:8000/api/perfil/'
                    axios.get(path).then((response) => {
                        this.usuario = response.data
                    })
                    .catch((error) => {
                        console.log(error)
                    })
                }
            },
        created() {
            this.getUsuario()
        }
    }
</script>

<style lang="css" scoped>
</style>
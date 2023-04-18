<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar Usuario</h2>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">
                            <div class="form-group row">
                                <label for="titulo" class="col-sm-2 col-form-label">Título</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Titulo" name="titulo" class="form-control" v-model.trim="form.titulo">
                                </div>
                            </div>
                            <div class="rows">
                                <div class="col text-left">
                                    <b-button typo="submit" variant="primary">Editar</b-button>
                                    <b-button typo="submit" class="btn-large-space" :to="{ name: 'ListUser'}">Cancelar</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
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
                userId: this.$route.params.userId,
                form: {
                    titulo: ''
                }
            }
        },
        methods: {
            onSubmit(e) {
                e.preventDefault();
                const path = 'http://127.0.0.1:8000/api/perfil/${this.userId}/'
                axios.put(path, this.form).then((response) => {
                    this.form.titulo = response.data.titulo
                    alert('Usuario actualizado exitosamente')
                })
                .catch((error) => {
                    console.log(error);
                })
            },
            getUsuario() {
                const path = 'http://127.0.0.1:8000/api/perfil/${this.userId}'
                axios.get(path).then((response) => {
                    this.form.titulo = response.data.titulo
                })
                .catch((error) => {
                    console.log(error);
                })
            }
        }, 
        created() {
            this.getUsuario();
        }
    }
</script>
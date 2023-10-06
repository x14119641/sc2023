<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
export default {
    name: 'PingComponent',
    data() {
        return {
            msg:''
        }        
    },
    methods: {
        getMessage(){
            const path = 'http://127.0.0.1:5000/ping'

            this.axios.get(path)
                .then((res) => {
                    this.msg = res.data;
                })
                .catch((error)=>{console.log(error);
                });
        }
    },
    created(){
        this.getMessage();
    }
}
</script>



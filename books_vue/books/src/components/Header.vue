<template>
    <b-container>
        <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#" @click="getCates">嗨小说</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="#">Link</b-nav-item>
            <b-nav-item href="#">Link</b-nav-item>
            <b-nav-item href="#">Link</b-nav-item>
            <b-nav-item href="#">Link</b-nav-item>
          </b-navbar-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="输入图书名字或者作者名字"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">开始查询</b-button>
          </b-nav-form>

        </b-navbar-nav>
        </b-collapse>
        </b-navbar>
    </b-container>
</template>

<script>
export default{
  name: 'Header',
  data: function () {
    return {
      msg: 'this is a message'
    }
  },
  setup (props, context) {
  },
  methods: {
    getCates: function () {
      this.$axios.get('http://127.0.0.1:5000/books_cates').then(resp => {
        console.log(resp)
        alert(resp.data.data[0])
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>
// lang告诉解释器css符合什么编译器的语法；scoped: 当前vue文件生效，没有scope则全局生效
<style scoped>

</style>

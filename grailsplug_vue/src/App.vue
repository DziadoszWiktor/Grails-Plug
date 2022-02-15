<template>
  <div id="wrapper">
      <nav class="navbar">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item" style="color:black;"><strong>GrailsPlug</strong></router-link>

            <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobilemMenu = !showMobilemMenu">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>
        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobilemMenu }">
            <div class="navbar-end">
                <router-link to="/Summer" class="navbar-item" style="color:black;"><strong>Summer</strong></router-link>
                <router-link to="/Winter" class="navbar-item" style="color:black;"><strong>Winter</strong></router-link>
                <router-link to="/Man" class="navbar-item" style="color:black;"><strong>Man</strong></router-link>
                <router-link to="/Woman" class="navbar-item" style="color:black;"><strong>Woman</strong></router-link>
            </div>
            <div class="navbar-item">
                <div class="buttons">
                    <router-link to="/LogIn" class="button is-light"><strong>Log in</strong></router-link>
                    <router-link to="/Cart" class="button is-success">
                        <span class="icon">
                            <i class="fas fa-shopping-cart"></i>
                        </span>
                        <span><strong>Cart</strong></span>
                    </router-link>
                </div>
            </div>
        </div>
      </nav> 
        <section class="section">
            <router-view/>
        </section>

        <footer>
            <p class="has-text-centered">Copyright (C) 2021</p>
        </footer>
  </div>
</template>

<script>
export default {
    data() {
        return {
            showMobilemMenu: false,
        }
    }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>


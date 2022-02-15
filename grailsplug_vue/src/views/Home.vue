<template>
  <div class="home">
    <section class="hero is-medium mb-6" style="background-color:black;">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Here's your GrailsPlug
            </p>
            <p class="subtitle">
                The best sneakers shop online
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
          <div class="column is-3" v-for="product in latestProducts" v-bind:key="product.id">
            <div class="box">
              <figure class="image" mb-4>
                <img v-bind:src="product.get_thumbnail">
              </figure>
              <h3 class="is-size-4">{{ product.name }}</h3>
              <p class="is-size-6 has-text-grey">${{ product.price }}</p>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
//import ProductBox from '@/components/ProductBox'
export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    //ProductBox
  },
  mounted() {
    this.getLatestProducts()
    document.title = 'Home | GrailsPlug'
  },
  methods: {
    getLatestProducts() {
      //this.$store.commit('setIsLoading', true)
      axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
      //this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-right: -1.25rem;
    margin-left: -1.25rem;
  }
</style>
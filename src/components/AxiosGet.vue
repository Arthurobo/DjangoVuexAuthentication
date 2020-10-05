<template>
  <div>
      <h1>Titles</h1>
      <div v-for="jobs in individualJobs" :key="jobs.id">
          <p>{{ jobs.id }}</p>
          <p>{{ jobs.user }}</p>
          <p>{{ jobs.company_name }}</p>
          <p>{{ jobs.job_title }}</p>
          <p>{{ jobs.job_location }}</p>
          <p>{{ jobs.job_country_location }}</p>
          <p>{{ jobs.company_phone_number }}</p>
          <p>{{ jobs.company_info }}</p>
          <p>{{ jobs.job_description }}</p>
          <p>{{ jobs.experience_level }}</p>
          <p>{{ jobs.salary }}</p>
          <p>{{ jobs.company_email }}</p>
          <p>{{ jobs.date_created }}</p>
          <p>{{ jobs.last_updated }}</p><hr>
      </div><hr>

    <AxiosPost />

</div>  
</template>

<script>
import axios from 'axios'
import AxiosPost from './AxiosPost'

export default {
  name: 'AxiosGet',
    components: {
        AxiosPost,
    },
    data () {
        return {
            individualJobs: null,
        }
    },

    mounted () {
        axios
        .get('http://127.0.0.1:8000/api/jobs/users/list/',)
        .then(response => (
            this.individualJobs = response.data
        ))
        .catch(e => {
            this.errors.push(e)
        })
      
    },
  
}
</script>
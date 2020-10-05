<template>
  <div id="add-blog">
      <div v-for="blog in blog" :key="blog.id">
          <p>{{ blog.user }} </p>
          <p>{{ blog.salary }} </p>
      </div>
      <h2>Add a New Job</h2>
      <form v-if="!submitted">
          <input type="text" v-model.lazy="blog.user" placeholder="User" required />
          <input type="text" v-model.lazy="blog.company_name" placeholder="Company Name" required />
          <input type="text" v-model.lazy="blog.job_title" placeholder="Job Title" required />
          <input type="text" v-model.lazy="blog.job_location" placeholder="Job Location" required />
          <input type="text" v-model.lazy="blog.job_country_location" placeholder="Job Country Location" required />
          <input type="text" v-model.lazy="blog.company_phone_number" placeholder="Company Phone Number" required />
          <input type="text" v-model.lazy="blog.company_info" placeholder="Company Info" required />

          <input type="text" v-model.lazy="blog.job_description" placeholder="job_description" required />
          <input type="text" v-model.lazy="blog.experience_level" placeholder="experience_level" required />
          <input type="text" v-model.lazy="blog.salary" placeholder="salary" required />
          <input type="email" v-model.lazy="blog.company_email" placeholder="Email" required />
          <button @click.prevent="post">Add Blog Post</button>
      </form>
      <div v-if="submitted">
          <h3>Thanks for adding your post</h3>
      </div>
  </div>
</template>

<script>

export default {
  
  data() {
    return {
        blog: {
            user: "",
            company_name: "",
            job_title: "",
            job_location: "",
            job_country_location: "",
            company_phone_number: "",
            company_info: "",
            job_description: "",
            experience_level: "",
            salary: "",
            company_email: "",
        },
        submitted: false,
    }
  },
  methods: {
      post: function() {
          this.$http.post('http://127.0.0.1:8000/api/jobs/users/list/', this.blog ).then(function(data) {
              console.log(data);
              this.submitted = true;
          });
      }
  }
}
</script>

<style>
#add-blog *{
    box-sizing: border-box;
}
#add-blog{
    margin: 20px auto;
    max-width: 500px;
}
label{
    display: block;
    margin: 20px 0 10px;
}
input[type="text"], textarea{
    display: block;
    width: 100%;
    padding: 8px;
}
#preview{
    padding: 10px 20px;
    border: 1px dotted #ccc;
    margin: 30px 0;
}
h3{
    margin-top: 10px;
}

#checkboxes input {
    display: inline-block;
    margin-right: 10px;
}

#checkboxes label{
    display: inline-block;
}
</style>

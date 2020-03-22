<template>
  <div class="container">
      <div class="h1_new" > O que deseja ver? </div>
      <div class="cont">
        <button class="button_new" @click="$router.push({path:'sensor'})"> Sensores</button>
        <button class="button_new" @click="$router.push({path:'matriculas'})">Matriculas</button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style>

.cont{
  align-items: center;
  display: flex;
  justify-content: center;
  margin-top: 10%;
}

.button_new{
  color:#fff;
  background-color:#218838;
  border-color:#1e7e34;
  font-size: 50px;
  border-radius: 10%;
  margin-inline: 15%;
  padding: 30px;
  height: 100%;
}

.h1_new {
  margin-top: 20%;
  font-size: 60px;
  align-items: center;
  display: flex;
  justify-content: center;

  }

</style>

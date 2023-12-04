<script lang="ts">
  export let data
  const prepData = data.resp

  console.log({prepData})
</script>


<flex-wrapper class="site__preparation">
  {#each Object.keys(prepData) as dataPoint}
    <h2>{dataPoint}</h2>
    <p>{prepData[dataPoint]}</p>
  {/each}


</flex-wrapper>

<style>
  .site__preparation {
    flex-direction: column;
  }
</style>
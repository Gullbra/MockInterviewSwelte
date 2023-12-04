<script lang="ts">
  import ChildComponent from "./components/ChildComponent.svelte";

  let twoWayBind = [1, 2, 3]

  //$: derivedObj = {...twoWayBind}
</script>


<div>
  <h2>{`Parent: ${twoWayBind[0]}`}</h2>
  <button on:click={() => twoWayBind[0] += 1}>Parent</button>
  <ChildComponent bind:parentData={twoWayBind} childData={twoWayBind.slice()} />

  <!-- <h2>{`Derived parent obj: ${twoWayBind}`}</h2> -->
</div>


<style>
  
</style>

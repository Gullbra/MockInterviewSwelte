<script lang="ts">
  export let childData: number[], parentData: number[]
  const stateChange = () => parentData = childData

</script>

<div>
  <h3>{`Child: ${childData[0]}`}</h3>
  <button on:click={() => {
    childData[0] += 1
    stateChange()
  }}>{`Child`}</button>
</div>

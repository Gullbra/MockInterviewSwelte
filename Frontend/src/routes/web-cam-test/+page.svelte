<script lang="ts">

  let stream: MediaStream;
  let videoRef: HTMLVideoElement;

  //$: console.log({videoRef})

  async function getStream() {
    try {
      stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: false
      });
      videoRef.srcObject = stream;
    } catch (err) {
      console.error(err);
    }
    //console.log(stream.getTracks()[0])
  }

  async function stopStream() {
    stream.getTracks().forEach(track => track.stop());
    videoRef.srcObject = null;
  }
</script>

<div class="about-page">
  <h2>Webcam Test!</h2>

  <div>
    {#if videoRef?.srcObject === null}
      <button class="rounded-sm bg-slate-600 text-white px-4 py-2" on:click={getStream}>Start Stream</button>
    {:else}
      <button class="rounded-sm bg-red-600 text-white px-4 py-2" on:click={stopStream}>Stop Stream</button>
    {/if}

    <video class="mt-4 rounded-sm " width="640" height="480" autoplay={true} bind:this={videoRef} />
  </div>
</div>

<style>
  .about-page {
    display: block;
  }
</style>
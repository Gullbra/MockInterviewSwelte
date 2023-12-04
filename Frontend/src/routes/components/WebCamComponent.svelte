<script lang="ts">
  let stream: MediaStream, videoRef: HTMLVideoElement;

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
  }

  async function stopStream() {
    stream.getTracks().forEach(track => track.stop());
    videoRef.srcObject = null;
  }
</script>


<video class={`mt-4 rounded-sm ${videoRef?.srcObject === null ? "--stream-closed" : "--stream-open"}`} autoplay={true} bind:this={videoRef}><track kind="captions"></video>

{#if videoRef?.srcObject === null}
  <button class="start-stop-btn rounded-sm bg-slate-600 text-white" on:click={getStream}>Start Stream</button>
{:else}
  <button class="start-stop-btn rounded-sm bg-red-600 text-white" on:click={stopStream}>Stop Stream</button>
{/if}


<style>
  .--stream-closed {
    height: 0px;
  }
  .--stream-open {
    width: 640px;
    height: 480px;
  }
  .start-stop-btn {
    margin-top: 2rem;
    padding: 0.2rem 0.5rem;
    display: block;
    cursor: pointer;
  }
</style>

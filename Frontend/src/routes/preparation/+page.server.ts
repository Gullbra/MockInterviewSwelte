export const load = async ({ fetch }) => {
  return {
    resp: await fetch('./mock/questions.list.json')
      .then(response => response.json())
      .then(json => json)
  }
}
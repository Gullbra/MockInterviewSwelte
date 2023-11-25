import { PUBLIC_FLASK_DEV_URL } from '$env/static/public';

export const load = async ({ fetch }) => {
  return {
    resp: await fetch(PUBLIC_FLASK_DEV_URL + "/api/data/questionsToAnswer")
      .then((response: Response) => {
        return !!response.body
          ? response.json()
          : (() => {console.log("No data fetched"); return {}})()
      })
      .catch(err => {console.error(err); return {}})
  }
}

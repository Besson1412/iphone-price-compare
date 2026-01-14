export default {
  async fetch(request, env, ctx) {
    return new Response("Hello! DevOps Pipeline is waiting for deployment.", {
      headers: { "content-type": "text/plain" },
    });
  },
};
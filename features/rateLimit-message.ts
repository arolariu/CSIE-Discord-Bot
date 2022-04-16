import { Client } from "discord.js";
import WOKCommands from "wokcommands";

export default (client: Client, instance: WOKCommands) => {
  client.on("rateLimit", (info) => {
    const { /* timeout, limit, */ method, path, route, global } = info;

    // if the rate limit is global, the rate limit is for the entire bot
    if (global) {
      console.log("Global rate limit exceeded");
    }

    // if the rate limit is for a specific route, the rate limit is for a specific route
    if (route) {
      console.log(`Rate limit exceeded for route ${route}`);
    }

    // if the rate limit is for a specific method, the rate limit is for a specific method
    if (method) {
      console.log(`Rate limit exceeded for method ${method}`);
    }

    // if the rate limit is for a specific path, the rate limit is for a specific path
    if (path) {
      console.log(`Rate limit exceeded for path ${path}`);
    }

    // if the rate limit is for a specific route and method, the rate limit is for a specific route and method
    if (route && method) {
      console.log(
        `Rate limit exceeded for route ${route} and method ${method}`
      );
    }

    // if the rate limit is for a specific route and path, the rate limit is for a specific route and path
    if (route && path) {
      console.log(`Rate limit exceeded for route ${route} and path ${path}`);
    }

    // if the rate limit is for a specific method and path, the rate limit is for a specific method and path
    if (method && path) {
      console.log(`Rate limit exceeded for method ${method} and path ${path}`);
    }

    // if the rate limit is for a specific route, method and path, the rate limit is for a specific route, method and path
    if (route && method && path) {
      console.log(
        `Rate limit exceeded for route ${route}, method ${method} and path ${path}`
      );
    }
  });
};

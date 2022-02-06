import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "Ping me!",
  name: "ping",

  slash: "both",
  testOnly: true,

  cooldown: "10s",
  callback: ({ client }) => {
    return `🏓Pong!\nLatency is ${client.ws.ping}ms.`;
  },
} as ICommand;

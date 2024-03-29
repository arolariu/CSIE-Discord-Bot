import { EmbedFooterData, MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description:
    "This command will return the connectivity information of the bot.",
  name: "ping",
  slash: true,
  testOnly: true,
  cooldown: "10s",
  callback: ({ client }) => {
    return new MessageEmbed()
      .setColor("RED")
      .setTitle("Pong!")
      .setDescription("This command will return connectivity information.")
      .addField("Uptime:", `${require("pretty-ms")(client.uptime)}`)
      .addField("Latency:", `${client.ws.ping}ms`)
      .addField("Gateway:", `${client.ws.gateway}`)
      .setFooter({
        text: process.env.EMBED_TEXT!,
        icon_url: process.env.EMBED_ICON!,
      } as EmbedFooterData);
  },
} as ICommand;

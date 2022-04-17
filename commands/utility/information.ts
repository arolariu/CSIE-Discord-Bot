import { EmbedField, EmbedFooterData, MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "View general information about the bot.",
  name: "information",
  slash: true,
  testOnly: true,
  cooldown: "10s",
  callback: () => {
    const os = require("os");
    const nodeVersion = process.version;
    const discordVersion = require("discord.js").version;
    const arch = os.arch();
    const model = os.cpus()[0].model;
    const totalMemory = os.totalmem();
    const freeMemory = os.freemem();
    const uptime = os.uptime();
    const cpuCores = os.cpus().length;

    const uptimeReadable = require("pretty-ms")(uptime);

    const prettyBytes = require("pretty-bytes");
    const totalMemoryReadable = prettyBytes(totalMemory);
    const freeMemoryReadable = prettyBytes(freeMemory);
    const usedMemoryReadable = prettyBytes(totalMemory - freeMemory);

    const embedFields: EmbedField[] = [
      {
        name: "Operating system:",
        value: os.platform() + " (" + os.type() + ")",
        inline: true,
      },
      {
        name: "OS build information:",
        value: os.release() || "Could not get OS build information.",
        inline: true,
      },
      {
        name: "Node version:",
        value: nodeVersion || "Could not get Node version.",
        inline: true,
      },
      {
        name: "Discord.js version:",
        value: discordVersion || "Could not get Discord.js version.",
        inline: true,
      },
      {
        name: "CPU architecture:",
        value: arch || "Could not get CPU architecture.",
        inline: true,
      },
      {
        name: "CPU core(s):",
        value: `${cpuCores} core(s).`,
        inline: true,
      },
      {
        name: "CPU model:",
        value: model || "Could not get CPU model.",
        inline: false,
      },
      {
        name: "Total RAM:",
        value: totalMemoryReadable || "Could not get total RAM.",
        inline: false,
      },
      {
        name: "Used RAM:",
        value: usedMemoryReadable || "Could not get used RAM.",
        inline: true,
      },
      {
        name: "Free RAM:",
        value: freeMemoryReadable || "Could not get free RAM.",
        inline: true,
      },
      {
        name: "Uptime:",
        value: uptimeReadable || "Could not get uptime.",
        inline: false,
      },
    ];

    return new MessageEmbed()
      .setColor("BLUE")
      .setTitle("Bot Info")
      .setDescription("View general information about the bot.")
      .addFields(embedFields)
      .setImage(process.env.EMBED_ICON!)
      .setTimestamp()
      .setFooter({
        text: process.env.EMBED_TEXT!,
        icon_url: process.env.EMBED_ICON!,
      } as EmbedFooterData);
  },
} as ICommand;

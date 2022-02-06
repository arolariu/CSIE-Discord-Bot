import { MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "Vizualizează informații despre platforma pe care este botul.",
  name: "information",

  slash: "both",
  testOnly: true,

  cooldown: "10s",
  callback: () => {
    // get the OS version
    const os = require("os");
    // get the node version
    const nodeVersion = process.version;
    // get the discord.js version
    const discordVersion = require("discord.js").version;
    // get the CPU architecture
    const arch = os.arch();
    // get the CPU model
    const model = os.cpus()[0].model;
    // get the total memory
    const totalMemory = os.totalmem();
    // get the free memory
    const freeMemory = os.freemem();
    // get the uptime
    const uptime = os.uptime();
    // get the CPU cores
    const cpuCores = os.cpus().length;

    ///////////////////////////////////////////

    // get the uptime in a human readable format
    const uptimeReadable = require("pretty-ms")(uptime);
    // get the total memory in a human readable format
    const totalMemoryReadable = require("pretty-bytes")(totalMemory);
    // get the free memory in a human readable format
    const freeMemoryReadable = require("pretty-bytes")(freeMemory);

    ///////////////////////////////////////////

    const embedFields = [
      {
        name: "Sistem de operare:",
        value: os.platform() + " (" + os.type() + ")",
        inline: true,
      },
      {
        name: "Versiune KB sistem:",
        value: os.release() || "Nu s-a putut afla versiunea KB de sistem.",
        inline: true,
      },
      {
        name: "Versiune node:",
        value: nodeVersion || "Nu s-a putut afla versiunea node.",
        inline: true,
      },
      {
        name: "Versiune discord.js:",
        value: discordVersion || "Nu s-a putut afla versiunea discord.js.",
        inline: true,
      },
      {
        name: "Arhitectura CPU:",
        value: arch || "Nu s-a putut afla arhitectura CPU.",
        inline: true,
      },
      {
        name: "Nuclee CPU:",
        value: `Am ${cpuCores > 0 ? cpuCores : 0} nuclee`,
        inline: true,
      },
      {
        name: "Model CPU:",
        value: model || "Nu s-a putut afla modelul CPU.",
        inline: false,
      },
      {
        name: "Memorie totală:",
        value: totalMemoryReadable || "Nu s-a putut afla memoria totală.",
        inline: true,
      },
      {
        name: "Memorie liberă:",
        value: freeMemoryReadable || "Nu s-a putut afla memoria liberă.",
        inline: true,
      },
      {
        name: "Timp de funcționare:",
        value: uptimeReadable || "Nu s-a putut afla timpul de funcționare.",
        inline: false,
      },
    ];

    const embedFooterData = {
      text: "Copyright 2022 (©) - arolariu.ro",
      icon_url: "",
    };

    const embed = new MessageEmbed()
      .setColor("BLUE")
      .setTitle("Informații despre platforma")
      .setDescription(
        "Informații generale despre platforma pe care este ținut botul:"
      )
      .addFields(embedFields)
      .setImage(
        "https://cdn.discordapp.com/attachments/743466478707409037/744920174477443112/wat.gif"
      )
      .setTimestamp()
      .setFooter(embedFooterData);

    return embed;
  },
} as ICommand;

import { MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "View general information about the bot.",
  name: "version",
  slash: "both",
  testOnly: true,
  cooldown: "10s",
  callback: () => {
    const changelog = require("../../data/changelog.json");
    const latest = changelog[0];

    const embedFields = [
      {
        name: "Release name:",
        value: latest.name + " (" + latest.version + ")",
        inline: true,
      },
      {
        name: "Release version:",
        value:
          latest.version || "Nu există o versiune în fișierul changelog.json.",
        inline: true,
      },
      {
        name: "Release date:",
        value: latest.release || "Nu exista o dată în fișierul changelog.json.",
        inline: true,
      },
      {
        name: "Release description:",
        value:
          latest.description ||
          "Nu există o descriere în fișierul changelog.json.",
        inline: false,
      },
      {
        name: "Changelog:",
        value: latest.changes?.join("\n") || "Minor bugfixes.",
        inline: false,
      },
    ];

    const embedFooterData = {
      text: "Copyright 2022 (©) - arolariu.ro",
      icon_url: "",
    };

    return new MessageEmbed()
      .setColor("RED")
      .setTitle("중간끝 ( B O T )")
      .setDescription("General information about the bot:")
      .addFields(embedFields)
      .setImage(process.env.EMBED_ICON!)
      .setFooter(embedFooterData)
      .setTimestamp();
  },
} as ICommand;

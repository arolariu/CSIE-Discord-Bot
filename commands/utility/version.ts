import { MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "Vizualizează informații despre versiunea botului.",
  name: "version",

  slash: "both",
  testOnly: true,

  cooldown: "10s",
  callback: () => {
    // store the changelog.json file in a variable
    const changelog = require("../changelog.json");
    // store the latest version in a variable
    const latest = changelog[0];

    const embedFields = [
      {
        name: "Nume release:",
        value: latest.name + " (" + latest.version + ")",
        inline: true,
      },
      {
        name: "Versiune:",
        value:
          latest.version || "Nu există o versiune în fișierul changelog.json.",
        inline: true,
      },
      {
        name: "Data:",
        value: latest.release || "Nu exista o dată în fișierul changelog.json.",
        inline: true,
      },
      {
        name: "Descriere:",
        value:
          latest.description ||
          "Nu există o descriere în fișierul changelog.json.",
        inline: false,
      },
      {
        name: "Lista modificari:",
        value: latest.changes?.join("\n") || "Minor bugfixes.",
        inline: false,
      },
    ];

    const embedFooterData = {
      text: "Copyright 2022 (©) - arolariu.ro",
      icon_url: "",
    };

    const embed = new MessageEmbed()
      .setColor("RED")
      .setTitle("중간끝 ( B O T )")
      .setDescription("Informatii generale bot de discord:")
      .addFields(embedFields)
      .setImage(
        "https://cdn.discordapp.com/attachments/743466478707409037/744920174477443112/wat.gif"
      )
      .setTimestamp()
      .setFooter(embedFooterData);

    return embed;
  },
} as ICommand;

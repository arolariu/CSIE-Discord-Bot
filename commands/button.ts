import { MessageButton, MessageActionRow } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "Materiale pentru facultate.",
  name: "materiale",
  slash: "both",
  testOnly: true,

  cooldown: "10s",
  callback: async ({ interaction: msgInt, channel }) => {
    const row = new MessageActionRow()
      .addComponents(
        new MessageButton()
          .setURL("https://arolariu.ro")
          .setLabel("Visit arolariu.ro")
          .setStyle("LINK")
      )
      .addComponents(
        new MessageButton()
          .setURL("https://blog.arolariu.ro")
          .setLabel("Visit blog.arolariu.ro")
          .setStyle("LINK")
      );

    await msgInt.reply({
      content: "Visit my websites:",
      components: [row],
    });
  },
} as ICommand;

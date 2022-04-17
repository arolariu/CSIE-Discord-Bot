import { MessageButton, MessageActionRow } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "Materiale pentru facultate.",
  name: "materiale",
  slash: "both",
  testOnly: true,

  cooldown: "10s",
  callback: async ({ interaction }) => {
    const row = new MessageActionRow()
      .addComponents(
        new MessageButton()
          .setURL("https://arolariu.ro")
          .setLabel("Visit arolariu.ro")
          .setStyle("LINK")
      )
      .addComponents(
        new MessageButton()
          .setURL("https://itc.arolariu.ro")
          .setLabel("Visit itc.arolariu.ro")
          .setStyle("LINK")
      );

    await interaction.reply({
      content: "Visit my websites:",
      components: [row],
    });
  },
} as ICommand;

import { TextChannel } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Moderation",
  description: "Sends a message as the bot.",
  name: "send",
  slash: true,
  testOnly: true,
  guildOnly: true,
  minArgs: 2,
  expectedArgs: "<channel> <message>",
  expectedArgsTypes: ["CHANNEL", "STRING"],

  callback: async ({ interaction, args }) => {
    const channel = interaction.options.getChannel("channel") as TextChannel;
    if (!channel || channel.type !== "GUILD_TEXT")
      return "Please tag a valid text channel.";

    args.shift();
    const message = args.join(" ");

    channel.send({
      content: message,
    });

    return interaction.reply({
      content: `Sending message to ${channel}.\nPreview:\n${message}`,
    });
  },
} as ICommand;

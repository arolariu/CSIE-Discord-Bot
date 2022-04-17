import { TextChannel } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Moderation",
  description: "Edit an already sent message from the bot.",
  name: "edit",
  slash: true,
  testOnly: true,
  guildOnly: true,
  minArgs: 3,
  maxArgs: 3,
  expectedArgs: "<channel> <messageID> <message>",
  expectedArgsTypes: ["CHANNEL", "STRING", "STRING"],

  callback: async ({ interaction, args }) => {
    const channel = interaction.options.getChannel("channel") as TextChannel;
    if (!channel || channel.type !== "GUILD_TEXT")
      return "Please tag a valid text channel.";

    args.shift();
    const messageID = args.shift()!;
    const editedMessage = args.join(" ");
    const originalMessage = await channel.messages.fetch(messageID);
    if (!originalMessage) return "Could not find message.";

    originalMessage.edit(editedMessage);

    return interaction.reply({
      content: `Editing message in ${channel}.`,
    });
  },
} as ICommand;

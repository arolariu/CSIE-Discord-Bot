import {
  EmbedAuthorData,
  EmbedFooterData,
  GuildMember,
  MessageEmbed,
  MessageOptions,
  TextChannel,
} from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Moderation",
  description: "Embeds a message as the bot.",
  name: "embed",
  slash: true,
  testOnly: true,
  guildOnly: true,
  minArgs: 2,
  expectedArgs: "<channel> <message>",
  expectedArgsTypes: ["CHANNEL", "STRING"],

  callback: async ({ interaction, args }) => {
    const channel = interaction.options.getChannel("channel") as TextChannel;
    const author = interaction.member as GuildMember;
    if (!channel || channel.type !== "GUILD_TEXT")
      return "Please tag a valid text channel.";

    args.shift();
    const message = args.join(" ");

    const embed = new MessageEmbed()
      .setDescription(message)
      .setColor("#00ff00")
      .setTimestamp()
      .setAuthor({
        name: author.displayName + " wants to announce that:",
        iconURL: author.displayAvatarURL(),
      } as EmbedAuthorData)
      .setFooter({
        text: "Sent by " + author.displayName,
        iconURL: author.displayAvatarURL(),
      } as EmbedFooterData);

    channel.send({
      embeds: [embed],
    } as MessageOptions);

    return interaction.reply({
      content: `Sending message to ${channel}.\nPreview:`,
      embeds: [embed],
    });
  },
} as ICommand;

import { EmbedFooterData, GuildMember, MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";
import generateLoremIpsum from "../../utils/generateLoremIpsum";

export default {
  category: "Moderation",
  description: "Sends a `Lorem Ipsum` message.",
  name: "lorem",
  slash: true,
  testOnly: true,
  guildOnly: true,
  minArgs: 1,
  expectedArgs: "<length>",
  expectedArgsTypes: ["NUMBER"],

  callback: async ({ interaction }) => {
    const length = interaction.options.getNumber("length");
    const author = interaction.member as GuildMember;
    const message = await generateLoremIpsum(length!);
    const embed = new MessageEmbed()
      .setTitle("Lorem Ipsum Generator.")
      .setDescription(message)
      .setColor("#00ff00")
      .setTimestamp()
      .setFooter({
        text: "Requested by " + author.displayName,
        iconURL: author.displayAvatarURL(),
      } as EmbedFooterData);

    return interaction.reply({ embeds: [embed] });
  },
} as ICommand;

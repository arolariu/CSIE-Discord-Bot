import {
  EmbedField,
  EmbedFooterData,
  Guild,
  GuildMember,
  MessageEmbed,
} from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "View general information about the server.",
  name: "server",
  slash: true,
  testOnly: true,
  guildOnly: true,
  cooldown: "10s",
  callback: async ({ guild }) => {
    const GUILD: Guild = await guild!.fetch();
    const OWNER: GuildMember = await GUILD.fetchOwner();

    const embedFields: EmbedField[] = [
      {
        name: "Server description:",
        value: GUILD.description || "No description provided.",
        inline: false,
      },
      {
        name: "Server owner:",
        value: OWNER.user.tag,
        inline: true,
      },
      {
        name: "Server created on:",
        value: GUILD.createdAt.toLocaleDateString(),
        inline: false,
      },
      {
        name: "Server ID:",
        value: GUILD.id,
        inline: false,
      },
      {
        name: "Owner ID:",
        value: OWNER.id,
        inline: false,
      },
      {
        name: "Current member count:",
        value: GUILD.memberCount.toString(),
        inline: true,
      },
      {
        name: "Maximum server capacity:",
        value: GUILD.maximumMembers!.toString(),
        inline: true,
      },
      {
        name: "Rules channel:",
        value: GUILD.rulesChannel?.toString() || "N/A",
        inline: false,
      },
      {
        name: "Starting channel:",
        value: GUILD.systemChannel?.toString() || "N/A",
        inline: true,
      },
    ];
    const embedFooter: EmbedFooterData = {
      text: `${GUILD.name} - Copyright © 2022 - ${OWNER.displayName}#${OWNER.user.discriminator}`,
      iconURL: GUILD.iconURL() ?? process.env.EMBED_ICON!,
    };

    return new MessageEmbed()
      .setColor("AQUA")
      .setTitle(`General information about the ${GUILD.name} discord server.`)
      .setThumbnail(GUILD.iconURL() ?? process.env.EMBED_ICON!)
      .setImage(GUILD.iconURL() ?? process.env.EMBED_ICON!)
      .addFields(embedFields)
      .setFooter(embedFooter)
      .setTimestamp();
  },
} as ICommand;

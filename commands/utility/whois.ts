import {
  Collection,
  EmbedField,
  EmbedFooterData,
  GuildMember,
  ImageURLOptions,
  MessageEmbed,
  Role,
  User,
} from "discord.js";
import { ICommand } from "wokcommands";
import filterRolesBasedOnCategory from "../../utils/filterRolesBasedOnCategory";

export default {
  category: "Utility",
  name: "whois",
  description: "Do a whois search on a specific user.",
  slash: true,
  testOnly: true,
  guildOnly: true,
  minArgs: 1,
  maxArgs: 1,
  expectedArgs: "<user>",
  expectedArgsTypes: ["USER"],

  callback: async ({ interaction }) => {
    const guildMember = interaction.options.getMember("user") as GuildMember;
    const guildMemberRoles: Collection<string, Role> = guildMember.roles.cache;
    const user: User = guildMember.user;

    const embedFields: EmbedField[] = [
      {
        name: "User display name:",
        value: guildMember.displayName,
        inline: true,
      },
      {
        name: "UID (User ID):",
        value: guildMember.id,
        inline: false,
      },
      {
        name: "User identifier",
        value: user.tag,
        inline: true,
      },
      {
        name: "User status:",
        value: guildMember.presence?.status || "Offline",
        inline: true,
      },
      {
        name: "Avatar URL:",
        value: user.displayAvatarURL({ format: "png", size: 2048 }),
        inline: false,
      },
      {
        name: "Joined discord on:",
        value: user.createdAt.toLocaleString(),
        inline: false,
      },
      {
        name: "Joined this server on :",
        value: guildMember.joinedAt!.toLocaleString(),
        inline: false,
      },
      {
        name: "Study Year:",
        value:
          filterRolesBasedOnCategory(guildMemberRoles, "Year")
            .map((role) => role.name)
            .join(".") || "None.",
        inline: true,
      },
      {
        name: "Study plan:",
        value:
          filterRolesBasedOnCategory(guildMemberRoles, "University")
            .map((role) => role.name)
            .join(".") || "None.",
        inline: true,
      },
      {
        name: "Known technologies:",
        value:
          filterRolesBasedOnCategory(guildMemberRoles, "Tech")
            .map((role) => role.name)
            .join(", ") || "None.",
        inline: false,
      },
      {
        name: "Wants to know more about:",
        value:
          filterRolesBasedOnCategory(guildMemberRoles, "Career Path")
            .map((role) => role.name)
            .join(", ") || "None.",
        inline: false,
      },
    ];

    const embedFooter: EmbedFooterData = {
      text: `whois executed by ${interaction.member?.user.username}#${interaction.member?.user.discriminator}`,
      iconURL: user.avatarURL({ format: "png", dynamic: true }) || "",
    };

    const embedImage: ImageURLOptions = {
      format: "png",
      dynamic: true,
      size: 4096,
    };

    return new MessageEmbed()
      .setColor("BLUE")
      .setTitle(
        `Whois executed for ${guildMember.displayName}#${user.discriminator}`
      )
      .addFields(embedFields)
      .setFooter(embedFooter)
      .setImage(user.displayAvatarURL(embedImage))
      .setThumbnail(user.displayAvatarURL(embedImage))
      .setTimestamp();
  },
} as ICommand;

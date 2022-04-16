import { GuildMember, MessageEmbed, Role, User } from "discord.js";
import { ICommand } from "wokcommands";
import getGuildMemberFromUID from "../../utils/getGuildMemberFromUID";
import getPresenceStatusFromGuildMember from "../../utils/getPresenceStatusFromGuildMember";
import filterRolesBasedOnCategory from "../../utils/helpers/filterRolesBasedOnCategory";
import getRolesFromGuildMember from "../../utils/getRolesFromGuildMember";
import sanitizeUID from "../../utils/helpers/sanitizeUID";

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

  callback: async ({ args, guild }) => {
    const guildMember: GuildMember = await getGuildMemberFromUID(
      sanitizeUID(args[0]!),
      guild!
    );
    const user: User = guildMember.user;

    const guildMemberRoles: Role[] = getRolesFromGuildMember(guildMember);

    const embedFields = [
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
        value: getPresenceStatusFromGuildMember(guildMember),
        inline: true,
      },
      {
        name: "Communication disabled:",
        value: guildMember.communicationDisabledUntil
          ? guildMember.communicationDisabledUntil.toLocaleDateString()
          : "No.",
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

    const embedFooter = {
      text: `whois executed for ${guildMember.displayName}#${user.discriminator}`,
      icon_url: user.avatarURL({ format: "png", dynamic: true }),
    };

    return new MessageEmbed()
      .setColor("BLUE")
      .setTitle(
        `Whois executed for ${guildMember.displayName}#${user.discriminator}`
      )
      .addFields(embedFields)
      .setFooter(embedFooter)
      .setImage(user.displayAvatarURL({ format: "png", dynamic: true }))
      .setThumbnail(user.displayAvatarURL({ format: "png", dynamic: true }))
      .setTimestamp();
  },
} as ICommand;

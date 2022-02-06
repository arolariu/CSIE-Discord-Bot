import { GuildMember, MessageEmbed, Role, User } from "discord.js";
import { ICommand } from "wokcommands";
import getGuildMemberFromUID from "../../utils/getGuildMemberFromUID";
import getPresenceStatusFromGuildMember from "../../utils/getPresenceStatusFromGuildMember";
import filterRolesBasedOnCategory from "../../utils/helpers/filterRolesBasedOnCategory";
import getRolesExceptEveryoneFromGuildMember from "../../utils/getRolesExceptEveryoneFromGuildMember";
import sanitizeUID from "../../utils/helpers/sanitizeUID";

export default {
  category: "Utility",
  name: "whois",
  description: "Do a whois search on a specific user.",

  slash: "both",
  testOnly: true,
  guildOnly: true,
  minArgs: 1,
  maxArgs: 1,
  expectedArgs: "<user>",

  callback: ({ args, guild }) => {
    const taggedUser: GuildMember = getGuildMemberFromUID(
      sanitizeUID(args[0]!),
      guild!
    )!;
    const taggedUserRoles: Role[] =
      getRolesExceptEveryoneFromGuildMember(taggedUser);

    const embedFields = [
      {
        name: "Nume de utilizator:",
        value: taggedUser.displayName || "Nu s-a putut afla username-ul.",
        inline: true,
      },
      {
        name: "Discriminator (tag):",
        value:
          taggedUser.user!.discriminator ||
          "Nu s-a putut afla discriminatorul.",
        inline: true,
      },
      {
        name: "UID:",
        value: taggedUser.id || "Nu s-a putut afla ID-ul.",
        inline: false,
      },
      {
        name: "Status utilizator:",
        value:
          getPresenceStatusFromGuildMember(taggedUser) ||
          "Nu s-a putut afla statutul pe server.",
        inline: true,
      },
      {
        name: "URL poză de profil:",
        value:
          taggedUser.user!.displayAvatarURL({ format: "png", size: 2048 }) ||
          "Nu s-a putut afla imaginea.",
        inline: false,
      },
      {
        name: "Anul de studiu:",
        value:
          filterRolesBasedOnCategory(taggedUserRoles, "Year")
            .map((role) => role.name)
            .join(".") || "Nu s-a putut afla anul de studiu.",
        inline: true,
      },
      {
        name: "Specializare:",
        value:
          filterRolesBasedOnCategory(taggedUserRoles, "University")
            .map((role) => role.name)
            .join(".") || "Nu s-a putut afla specializarea.",
        inline: true,
      },
      {
        name: "Tehnologii cunoscute:",
        value:
          filterRolesBasedOnCategory(taggedUserRoles, "Tech")
            .map((role) => role.name)
            .join(", ") || "Nu s-au putut afla tehnologiile cunoscute.",
        inline: false,
      },
      {
        name:
          "Domenii de care este interesat(ă) " + taggedUser.displayName + ":",
        value:
          filterRolesBasedOnCategory(taggedUserRoles, "Career Path")
            .map((role) => role.name)
            .join(", ") ||
          "Nu s-au putut afla domeniile de care este interesat(ă).",
        inline: false,
      },
      {
        name: "S-a alăturat pe discord în data de:",
        value:
          taggedUser.user!.createdAt.toLocaleString() ||
          "Nu s-a putut afla data de la care s-a alăturat pe discord.",
        inline: false,
      },
      {
        name: "S-a alăturat pe server în data de:",
        value:
          taggedUser.joinedAt!.toLocaleString() ||
          "Nu s-a putut afla data de la care s-a alăturat pe server.",
        inline: false,
      },
    ];

    const embedFooter = {
      text: `whois rulat pentru ${taggedUser.displayName}#${
        taggedUser.user!.discriminator
      }`,
      icon_url: taggedUser.user!.avatarURL({ format: "png", dynamic: true }),
    };

    const embed = new MessageEmbed()
      .setColor("#0099ff")
      .setTitle(
        `Whois pentru membrul ${taggedUser.displayName}#${
          taggedUser.user!.discriminator
        }`
      )
      .addFields(embedFields)
      .setFooter(embedFooter)
      .setImage(
        taggedUser.user!.displayAvatarURL({ format: "png", dynamic: true })
      )
      .setThumbnail(
        taggedUser.user!.displayAvatarURL({ format: "png", dynamic: true })
      )
      .setTimestamp();

    return embed;
  },
} as ICommand;

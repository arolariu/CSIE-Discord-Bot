import { GuildMember, Role, User } from "discord.js";
import IUser from "../interfaces/User.interface";
import getRolesFromGuildMember from "./getRolesFromGuildMember";
import filterRolesBasedOnCategory from "./helpers/filterRolesBasedOnCategory";

export default function getIUserFromGuildMember(
  guildMember: GuildMember
): IUser {
  try {
    const roles: Role[] = getRolesFromGuildMember(guildMember);
    const user: User = guildMember.user; // gets the discord user object.
    return {
      id: user.id,
      username: user.username,
      password: null,
      email: null,
      avatarURL: user.avatarURL(),
      verified: false,
      discordTAG: user.discriminator,
      createdAt: user.createdAt,
      joinedAt: guildMember.joinedAt,
      technologies:
        filterRolesBasedOnCategory(roles, "Tech")
          .map((role) => role.name)
          .join(", ") || "None",
      career:
        filterRolesBasedOnCategory(roles, "Career Path")
          .map((role) => role.name)
          .join(", ") || "None",
      degree:
        filterRolesBasedOnCategory(roles, "University")
          .map((role) => role.name)
          .join(", ") || "None",
    } as IUser;
  } catch (error) {
    throw new Error(
      `Could not create convert Guild Member ${guildMember.displayName} into JSON-format.
      Error: ${error}`
    );
  }
}

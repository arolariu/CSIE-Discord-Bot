import { GuildMember, Role } from "discord.js";
import User from "../../interfaces/User.interface";
import getRolesExceptEveryoneFromGuildMember from "../getRolesExceptEveryoneFromGuildMember";
import filterRolesBasedOnCategory from "./filterRolesBasedOnCategory";

export default function createJSONforGuildMember(
  guildMember: GuildMember
): User {
  try {
    const roles: Role[] = getRolesExceptEveryoneFromGuildMember(guildMember);
    const userJSON = {
      id: guildMember.id,
      username: guildMember.user!.username,
      discriminator: guildMember.user!.discriminator,
      avatar: guildMember.user!.avatarURL(),
      createdAt: guildMember.user!.createdAt,
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
    };
    return userJSON;
  } catch (error) {
    throw new Error(
      `Could not create JSON for Guild Member ${guildMember.displayName}.
      Error: ${error}`
    );
  }
}

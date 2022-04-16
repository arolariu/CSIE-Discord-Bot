import { GuildMember, Role } from "discord.js";

export default function getRolesFromGuildMember(member: GuildMember): Role[] {
  let roles: Role[] = [];
  member.roles.cache.forEach((role) => {
    if (role.id !== "0") roles.push(role);
  });
  return roles;
}

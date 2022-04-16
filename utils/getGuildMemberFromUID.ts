import { Guild, GuildMember } from "discord.js";

export default async function getGuildMemberFromUID(
  userID: string,
  guild: Guild
): Promise<GuildMember> {
  const guildMember: Promise<GuildMember> = guild.members.fetch(userID);
  if (!guildMember || typeof guildMember !== "object")
    throw new Error(`Could not find Guild Member with UID ${userID}.`);
  return guildMember;
}

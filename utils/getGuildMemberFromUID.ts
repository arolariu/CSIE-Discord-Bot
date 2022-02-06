import { Guild, GuildMember } from "discord.js";
import sanitizeUID from "./helpers/sanitizeUID";

export default function getGuildMemberFromUID(
  userID: string,
  guild: Guild
): GuildMember {
  const guildMember: GuildMember | undefined =
    guild.members!.cache.get(userID);

  if (!guildMember || typeof guildMember !== "object") {
    throw new Error(`Could not find Guild Member with UID ${userID}.`);
  }
  return guildMember;
}

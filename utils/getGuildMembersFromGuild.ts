import { Collection, Guild, GuildMember, GuildMemberManager } from "discord.js";

export default async function getGuildMembersFromGuild(
  guild: Guild
): Promise<GuildMember[]> {
  const guildMembersManager: GuildMemberManager = guild.members;

  if (guildMembersManager === undefined || !guildMembersManager)
    throw new Error(
      `Could not find the Guild Member Manager for Guild ${guild.name}.`
    );

  const guildMembersCollection: Collection<string, GuildMember> =
    await guildMembersManager.fetch();

  if (guildMembersCollection === undefined || !guildMembersCollection)
    throw new Error(
      `Could not find the Guild Members for Guild ${guild.name}.`
    );

  let guildMembers: GuildMember[] = [];
  for (let i = 0; i < guildMembersCollection.size; i++) {
    guildMembers.push(guildMembersCollection.at(i)!);
  }

  return guildMembers;
}

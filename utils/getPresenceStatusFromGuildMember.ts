import { GuildMember, Presence } from "discord.js";

export default function getPresenceStatusFromGuildMember(
  member: GuildMember
): string {
  const presence: Presence = member.presence!;
  if (!presence) return "offline";

  const status = presence.status;
  if (status === "online") return "online";
  if (status === "idle") return "idle";
  if (status === "dnd") return "dnd";

  return "offline";
}

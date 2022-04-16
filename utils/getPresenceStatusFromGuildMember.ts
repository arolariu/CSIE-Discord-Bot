import { GuildMember, Presence } from "discord.js";

export default function getPresenceStatusFromGuildMember(
  member: GuildMember
): string {
  const presence: Presence = member.presence!;
  if (!presence) return "offline";

  const status = presence.status;
  if (status === "online") return "Online";
  if (status === "idle") return "Idle";
  if (status === "dnd") return "Do not disturb";

  return "Offline (or invisible)";
}

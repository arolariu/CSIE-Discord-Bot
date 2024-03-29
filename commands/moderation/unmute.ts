import { User } from "discord.js";
import { Error } from "mongoose";
import { ICommand } from "wokcommands";
import WarningModel from "../../models/Warning.model";

export default {
  category: "Moderation",
  description: "Unmute an already muted user.",
  name: "unmute",
  permissions: ["MANAGE_MESSAGES"],
  slash: true,
  testOnly: true,
  guildOnly: true,
  minArgs: 2,
  maxArgs: 2,
  expectedArgs: "<user> <reason>",
  expectedArgsTypes: ["USER", "STRING"],

  callback: async ({ args, member: staff, guild, interaction }) => {
    if (!guild) return "This command can only be used in a server.";
    const userId = args.shift()!;
    const reason = args.join(" ");
    const user = interaction.options.getUser("user") as User;
    if (!user) return "Please provide a valid user.";
    const member = await guild.members.fetch(userId);
    if (!member) return "That user is not in this server.";
    const mutedRole = guild.roles.cache.find((r) => r.name === "Muted");
    if (!mutedRole) return "Muted ('<Muted>') role not found.";
    await member.roles.remove(mutedRole);
    const query = { id: userId };
    WarningModel.findOneAndRemove(query, (err: Error, result: any) => {
      if (err) return console.error(err);
      if (!result) return "That user is not muted.";
      return `<@${user.id}> has been unmuted by <@${staff.id}>.\nReason: ${reason}`;
    });
    return `<@${user.id}> has been unmuted by <@${staff.id}>.\nReason: ${reason}`;
  },
} as ICommand;

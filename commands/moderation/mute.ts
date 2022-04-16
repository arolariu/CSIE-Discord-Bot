import { User } from "discord.js";
import { ICommand } from "wokcommands";
import WarningModel from "../../models/Warning.model";

export default {
  category: "Moderation",
  description: "Mute a user",
  name: "mute",
  permissions: ["MANAGE_MESSAGES"],
  slash: true,
  testOnly: true,
  guildOnly: true,
  minArgs: 3,
  maxArgs: 3,
  expectedArgs: "<user> <duration> <reason>",
  expectedArgsTypes: ["USER", "STRING", "STRING"],

  callback: async ({ args, member: staff, guild, interaction }) => {
    if (!guild) return "This command can only be used in a server.";

    const userId = args.shift()!;
    const duration = args.shift()!;
    const reason = args.join(" ");

    let user: User = interaction.options.getUser("user") as User;
    if (!user) return "Please provide a valid user.";

    let time, type;
    try {
      const split = duration.match(/\d+|\D+/g);
      time = parseInt(split![0]);
      type = split![1].toLowerCase();
    } catch (e) {
      return "Invalid time format! Example format: <1d>, <1h>, <1m>";
    }

    if (type === "d") time *= 60 * 24;
    else if (type === "h") time *= 60;
    else if (type !== "m")
      return "Invalid time format! Example format: <1d>, <1h>, <1m>";

    const expires = new Date();
    expires.setMinutes(expires.getMinutes() + time);

    const result = await WarningModel.findOne({
      guildId: guild.id,
      userId: user.id,
    });
    if (result) return `<@${user.id}> is already muted.`;

    try {
      const member = await guild.members.fetch(userId);
      if (member) {
        const mutedRole = guild.roles.cache.find((r) => r.name === "Muted");
        if (!mutedRole) return "Muted ('<Muted>') role not found.";
        await member.roles.add(mutedRole);
      }
      await new WarningModel({
        guildId: guild.id,
        userId: userId,
        staffId: staff.id,
        reason,
        expiresAt: expires,
        createdAt: new Date(),
      }).save();
    } catch (e) {
      return `Cannot mute <@${user.id}>.`;
    }
    return `<@${user.id}> has been muted. (duration:${time}).`;
  },
} as ICommand;

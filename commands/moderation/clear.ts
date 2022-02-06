import { ICommand } from "wokcommands";

export default {
  category: "Moderation",
  name: "clear",
  description: "Clear messages from a channel.",
  permissions: ["MANAGE_MESSAGES"],
  slash: "both",
  testOnly: true,
  guildOnly: true,
  maxArgs: 1,
  expectedArgs: "<amount>",

  callback: async ({ message, interaction, channel, args }) => {
    const amount = args.length ? parseInt(args.shift()!) : 5;

    if (message) {
      await message.delete();
    }
    // Bulk delete the messages:
    const { size } = await channel.bulkDelete(amount, true);

    const reply = `Deleted ${size} message(s).`;
    if (interaction) {
      return reply;
    }
    channel.send(reply);
  },
} as ICommand;

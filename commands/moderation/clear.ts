import { ICommand } from "wokcommands";

export default {
  category: "Moderation",
  name: "clear",
  description: "Clear messages from a channel inside of a guild.",
  permissions: ["MANAGE_MESSAGES"],
  slash: "both",
  testOnly: true,
  guildOnly: true,
  maxArgs: 1,
  expectedArgs: "<amount of messages to be deleted>",

  callback: async ({ message, interaction, channel, args }) => {
    const amount = args.length ? parseInt(args.shift()!) : 5;

    if (message) await message.delete();

    // Bulk delete the messages:
    const { size } = await channel.bulkDelete(amount, true);

    const reply = `Successfully deleted ${size} message(s).`;
    return interaction ? reply : channel.send(reply);
  },
} as ICommand;

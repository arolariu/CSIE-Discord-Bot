import { ICommand } from "wokcommands";

export default {
  category: "Moderation",
  name: "clear",
  description: "Clear messages from a channel inside of a guild.",
  permissions: ["MANAGE_MESSAGES"],
  slash: true,
  testOnly: true,
  guildOnly: true,
  maxArgs: 1,
  expectedArgs: "<amount of messages to be deleted>",
  expectedArgsTypes: ["NUMBER"],
  callback: async ({ channel, args }) => {
    const amount = args.length ? parseInt(args.shift()!) : 5;
    const messages = await channel.messages.fetch({ limit: amount });
    const { size } = messages;
    messages.forEach((msg) => msg.delete());
    return `Successfully deleted ${size} message(s).`;
  },
} as ICommand;

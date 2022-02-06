import { Client, TextChannel } from "discord.js";
import WOKCommands from "wokcommands";

export default (client: Client, instance: WOKCommands) => {
  client.on("guildMemberRemove", (member) => {
    const { guild } = member;

    const channel = guild.channels.cache.find(
      (channel) => channel.name === "🎓│bun-venit"
    ) as TextChannel;

    if (!channel) {
      return;
    }

    channel.send({
      content: `${member} a parasit serverul.`,
    });
  });
};

import { Client, TextChannel } from "discord.js";
import WOKCommands from "wokcommands";

export default (client: Client, instance: WOKCommands) => {
  // Listen for new members joining a guild
  client.on("guildMemberAdd", (member) => {
    // Access the guild that they joined
    const { guild } = member;

    // Get the channel named "welcome"
    const channel = guild.channels.cache.find(
      (channel) => channel.name === "🎓│bun-venit"
    ) as TextChannel;

    // Ensure this channel exists
    if (!channel) {
      return;
    }

    // Send the welcome message
    channel.send({
      content: `Welcome ${member} to the server!`,
    });
  });
};

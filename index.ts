import DiscordJS from "discord.js";
import WOKCommands from "wokcommands";
import { intents, WOKOptions } from "./config";

const client: DiscordJS.Client = new DiscordJS.Client({
  intents: intents,
});

client.on("ready", async () => {
  new WOKCommands(client, WOKOptions)
    .setColor("#ff0000")
    .setDisplayName("Help menu")
    .setDefaultPrefix("$");
});

client.login(process.env.DISCORD_TOKEN);

import DiscordJS, { Intents } from "discord.js";
import WOKCommands from "wokcommands";
import dotenv from "dotenv";
import path from "path";
dotenv.config();

const client: DiscordJS.Client = new DiscordJS.Client({
  intents: [
    Intents.FLAGS.GUILDS,
    Intents.FLAGS.GUILD_MESSAGES,
    Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
    Intents.FLAGS.GUILD_PRESENCES,
  ],
});

client.on("ready", async () => {
  new WOKCommands(client, {
    testServers: [process.env.DISCORD_GUILD_ID || ""],
    botOwners: [process.env.DISCORD_BOT_OWNER_ID || ""],
    featureDir: path.join(__dirname, "features"),
    commandDir: path.join(__dirname, "commands"),
    mongoUri: process.env.MONGO_URI || "",
    dbOptions: { keepAlive: true },
    typeScript: true,
    showWarns: true,
    debug: true,
  }).setDefaultPrefix("$");
});

client.login(process.env.DISCORD_TOKEN);

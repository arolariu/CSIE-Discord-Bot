import { Options } from "wokcommands";
import { Intents } from "discord.js";
import dotenv from "dotenv";
import path from "path";
dotenv.config();

export const intents: number[] = [
  Intents.FLAGS.GUILDS,
  Intents.FLAGS.GUILD_MEMBERS,
  Intents.FLAGS.GUILD_BANS,
  Intents.FLAGS.GUILD_EMOJIS_AND_STICKERS,
  Intents.FLAGS.GUILD_INTEGRATIONS,
  Intents.FLAGS.GUILD_WEBHOOKS,
  Intents.FLAGS.GUILD_INVITES,
  Intents.FLAGS.GUILD_VOICE_STATES,
  Intents.FLAGS.GUILD_PRESENCES,
  Intents.FLAGS.GUILD_MESSAGES,
  Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
  Intents.FLAGS.GUILD_MESSAGE_TYPING,
  Intents.FLAGS.DIRECT_MESSAGES,
  Intents.FLAGS.DIRECT_MESSAGE_REACTIONS,
  Intents.FLAGS.DIRECT_MESSAGE_TYPING,
  Intents.FLAGS.GUILD_SCHEDULED_EVENTS,
];

export const WOKOptions: Options = {
  testServers: [process.env.DISCORD_GUILD_ID || ""],
  botOwners: [process.env.DISCORD_BOT_OWNER_ID || ""],
  featureDir: path.join(__dirname, "features"),
  commandDir: path.join(__dirname, "commands"),
  mongoUri: process.env.MONGO_URI || "",
  dbOptions: { keepAlive: true },
  typeScript: true,
  showWarns: true,
  debug: true,
};

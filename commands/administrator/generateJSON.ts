import { GuildMember, MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";
import User from "../../interfaces/User.interface";
import getGuildMembersFromGuild from "../../utils/getGuildMembersFromGuild";
import createJSONforGuildMember from "../../utils/helpers/createJSONforGuildMember";
import fs from "fs";

export default {
  category: "Administrator",
  description: "Generate JSON file with every user's info.",
  name: "generateJSON",
  slash: false,
  testOnly: true,
  guildOnly: true,
  permissions: ["ADMINISTRATOR"],
  minArgs: 1,
  maxArgs: 1,
  expectedArgs: "<channel id>",

  callback: async ({ message, client, args }) => {
    if (args[0].length < 1 || typeof args[0] !== "string")
      return "Please provide a channel id.";

    const guild = client.guilds.cache.get(args[0]);
    if (!guild) return "Could not find guild.";

    const timeUntilFetchUsers = Date.now();
    const guildMembers: GuildMember[] = await getGuildMembersFromGuild(guild);
    const timeAfterFetchUsers = Date.now();

    let JSONArray: User[] = [];
    guildMembers.forEach((user) =>
      JSONArray.push(createJSONforGuildMember(user))
    );
    const timeAfterGeneratingJSON = Date.now();
    const JSONFile = JSON.stringify(JSONArray);
    fs.writeFileSync(`./data/users.json`, JSONFile);
    const timeAfterWritingFile = Date.now();

    const embedFields = [
      {
        name: "Timp de asteptare pentru a descarca utilizatorii:",
        value: `${timeAfterFetchUsers - timeUntilFetchUsers} ms`,
        inline: false,
      },
      {
        name: "Timp de asteptare pentru a genera JSON:",
        value: `${timeAfterGeneratingJSON - timeAfterFetchUsers} ms`,
        inline: false,
      },
      {
        name: "Timp de asteptare pentru a scrie fisierul:",
        value: `${timeAfterWritingFile - timeAfterGeneratingJSON} ms`,
        inline: false,
      },
    ];

    const embedFooter = {
      text: `${JSONArray.length} utilizatori au fost găsiți.`,
      icon_url: client.user!.avatarURL(),
    };

    const embed = new MessageEmbed()
      .setColor("#0099ff")
      .setTitle(
        `Generated JSON file for ${guild.name} (${guildMembers.length} users)`
      )
      .addFields(embedFields)
      .setFooter(embedFooter)
      .setTimestamp();
    return embed;
  },
} as ICommand;

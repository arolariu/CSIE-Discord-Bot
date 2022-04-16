import { GuildMember, MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";
import IUser from "../../interfaces/User.interface";
import getGuildMembersFromGuild from "../../utils/getGuildMembersFromGuild";
import getIUserFromGuildMember from "../../utils/getIUserfromGuildMember";
import fs from "fs";

export default {
  category: "Administrator",
  description: "Generate JSON file with every user's information.",
  name: "generateJSON",
  slash: "both",
  testOnly: true,
  guildOnly: true,
  permissions: ["ADMINISTRATOR"],
  minArgs: 1,
  maxArgs: 1,
  expectedArgs: "<Guild ID>",

  callback: async ({ client, args }) => {
    if (args[0].length < 1 || typeof args[0] !== "string")
      return "Please provide a valid Guild ID.";

    // 0. Find  the guild from the args[0].
    const guild = client.guilds.cache.get(args[0]);
    if (!guild) return `Could not find the specified Guild ID: ${args[0]}`;

    // 1. Fetching the users from the guild.
    const timeUntilFetchUsers = Date.now();
    const guildMembers: GuildMember[] = await getGuildMembersFromGuild(guild);
    const timeAfterFetchUsers = Date.now();

    // 2. Adding the users to a JSON array object.
    let JSONArray: IUser[] = [];
    guildMembers.forEach((user) =>
      JSONArray.push(getIUserFromGuildMember(user))
    );
    const timeAfterGeneratingJSON = Date.now();

    // 3. Writing the JSON array to a file.
    const JSONFile = JSON.stringify(JSONArray);
    fs.writeFileSync(`./data/users.json`, JSONFile);
    const timeAfterWritingFile = Date.now();

    // 4. Sending a message to the channel.
    const embedFields = [
      {
        name: "Elapsed time for adding users:",
        value: `${timeAfterFetchUsers - timeUntilFetchUsers} ms.`,
        inline: false,
      },
      {
        name: "Elapsed time for generating JSON:",
        value: `${timeAfterGeneratingJSON - timeAfterFetchUsers} ms.`,
        inline: false,
      },
      {
        name: "Elapsed time for writing JSON file:",
        value: `${timeAfterWritingFile - timeAfterGeneratingJSON} ms.`,
        inline: false,
      },
      {
        name: "⌛ Total execution time:",
        value: `${timeAfterWritingFile - timeUntilFetchUsers} ms.`,
        inline: false,
      },
      {
        name: "💾 JSON file size:",
        value: `${JSONFile.length} bytes. - ${(
          JSONFile.length / 1024
        ).toFixed()} KB.`,
        inline: false,
      },
    ];

    const embedFooter = {
      text: `${JSONArray.length} users have been found.`,
      icon_url: client.user!.avatarURL(),
    };

    return new MessageEmbed()
      .setColor("#0099ff")
      .setTitle(
        `Generated JSON file for ${guild.name}. (${guildMembers.length} total users)`
      )
      .addFields(embedFields)
      .setFooter(embedFooter)
      .setTimestamp();
  },
} as ICommand;

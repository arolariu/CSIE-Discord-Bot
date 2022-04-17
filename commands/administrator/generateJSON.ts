import {
  EmbedFieldData,
  EmbedFooterData,
  Guild,
  MessageEmbed,
} from "discord.js";
import { ICommand } from "wokcommands";
import IUser from "../../interfaces/User.interface";
import getIUserFromGuildMember from "../../utils/getIUserFromGuildMember";
import fs from "fs";

export default {
  category: "Administrator",
  description: "Generate JSON file with every user's information.",
  name: "generateJSON",
  slash: true,
  testOnly: true,
  guildOnly: true,
  permissions: ["ADMINISTRATOR"],
  maxArgs: 1,
  expectedArgs: "<fullpath to the users json>",
  expectedArgsTypes: ["STRING"],

  callback: async ({ interaction, args }) => {
    const guild: Guild = interaction.guild!;
    const path = args.shift() ?? "./data/users.json";

    // 1. Fetching the users from the guild.
    const timeUntilFetchUsers = Date.now();
    const guildMembers = await guild.members.fetch();
    const timeAfterFetchUsers = Date.now();

    // 2. Adding the users to a JSON array object.
    let JSONArray: IUser[] = [];
    guildMembers.forEach((user) =>
      JSONArray.push(getIUserFromGuildMember(user))
    );
    const timeAfterGeneratingJSON = Date.now();

    // 3. Writing the JSON array to a file.
    const JSONFile = JSON.stringify(JSONArray);
    fs.writeFileSync(path, JSONFile);
    const timeAfterWritingFile = Date.now();

    // 4. Sending a message to the channel.
    const embedFields: EmbedFieldData[] = [
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

    const embedFooter: EmbedFooterData = {
      text: `${JSONArray.length} users have been found.`,
      iconURL: process.env.EMBED_ICON,
    };

    return new MessageEmbed()
      .setColor("BLUE")
      .setTitle(`Generated JSON file for ${guild.name}.`)
      .addFields(embedFields)
      .setFooter(embedFooter)
      .setTimestamp();
  },
} as ICommand;

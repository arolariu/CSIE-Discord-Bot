import axios from "axios";
import { MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Resources",
  description: "Useful resources & commands.",
  name: "mdn",
  slash: true,
  testOnly: true,
  guildOnly: true,
  cooldown: "3s",
  minArgs: 1,
  expectedArgs: "<search query>",
  callback: async ({ text }) => {
    const base = "https://developer.mozilla.org";
    const uri = `${base}/api/v1/search?q=${encodeURIComponent(
      text
    )}&locale=en-US`;

    const documents = await (await axios(uri)).data.documents;

    if (documents) {
      const embed = new MessageEmbed()
        .setAuthor({
          name: "MDN Documentation",
          iconURL: "https://avatars.githubusercontent.com/u/7565578?s=200&v=4",
        })
        .setColor("GREEN");

      let truncated = false;
      if (documents.length > 3) {
        documents.length = 3;
        truncated = true;
      }

      for (let { mdn_url, title, summary } of documents) {
        summary = summary.replace(/(\r\n|\n|\r)/gm, "");
        embed.addField(title, `${summary}\n[**Link**](${base}${mdn_url})`);
      }

      if (truncated) {
        embed.addField(
          "Too many results!!",
          `View more results [here](https://developer.mozzila.org/en-US/search?q=${encodeURIComponent(
            text
          )}
              ).`
        );
      }

      return embed;
    }
    return `Could not find any results for ${text}`;
  },
} as ICommand;

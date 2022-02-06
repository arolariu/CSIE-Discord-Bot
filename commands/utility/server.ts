import { Guild, GuildMember, MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "Vizualizează informații despre server.",
  name: "server",

  slash: "both",
  testOnly: true,
  guildOnly: true,

  cooldown: "10s",
  callback: async ({ guild }) => {
    const GUILD: Guild = await guild!.fetch();
    const OWNER: GuildMember = await GUILD.fetchOwner();

    const embedFields = [
      {
        name: "Descriere server:",
        value: GUILD.description || "Nu există descriere.",
        inline: false,
      },
      {
        name: "Server înființat la data de:",
        value: GUILD.createdAt!.toLocaleString() || "N/A",
        inline: false,
      },
      {
        name: "Nr. total de membri:",
        value:
          GUILD.memberCount!.toString() ||
          "Nu am putut obține numărul de membri.",
        inline: true,
      },
      {
        name: "Nr. maxim de membri:",
        value:
          GUILD.maximumMembers!.toString() ||
          "Nu am putut obține numărul maxim de membri.",
        inline: true,
      },
      {
        name: "Performanță canale voce:",
        value:
          GUILD.maximumBitrate === 12800
            ? "12.8 Kbps"
            : "N/A" || "Nu am putut obține performanța canalelor de voce.",
        inline: false,
      },
      {
        name: "Nr. server boosts:",
        value: GUILD.premiumSubscriptionCount!.toString() || "0",
        inline: false,
      },
      {
        name: "Nivel server boost:",
        value: GUILD.premiumTier || "N/A",
        inline: false,
      },
      {
        name: "Canalul de reguli:",
        value: GUILD.rulesChannel
          ? GUILD.rulesChannel!.toString() || "N/A"
          : "Nu există.",
        inline: false,
      },
      {
        name: "Administrator principal server:",
        value:
          OWNER.displayName + "#" + OWNER.user.discriminator || "Nu există.",
        inline: false,
      },
    ];
    const embedFooter = {
      text: `${GUILD.name} - Copyright © 2022 - ${OWNER.displayName}#${OWNER.user.discriminator}`,
      icon_url: GUILD.iconURL(),
    };

    const embed = new MessageEmbed()
      .setColor(0x00ae86)
      .setTitle(`Informații despre ${GUILD.name}`)
      .addFields(embedFields)
      .setFooter(embedFooter)
      .setTimestamp();

    return embed;
  },
} as ICommand;

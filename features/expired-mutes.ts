import { Client } from "discord.js";
import WarningModel from "../models/Warning.model";

export default (client: Client) => {
  client.on("guildMemberAdd", async (member) => {
    const result = await WarningModel.findOne({
      guildId: member.guild.id,
      userId: member.id,
    });
    if (result) {
      const mutedRole = member.guild.roles.cache.find(
        (r) => r.name === "Muted"
      );

      if (mutedRole) await member.roles.add(mutedRole);
    }
  });

  const check = async () => {
    const query = {
      expiresAt: { $lt: new Date() },
    };
    const results = await WarningModel.find(query);

    for (const result of results) {
      const { guildId, userId } = result;
      const guild = await client.guilds.fetch(guildId);
      if (!guild) continue;
      const mutedRole = guild.roles.cache.find((r) => r.name === "Muted");
      if (!mutedRole) continue;

      const member = await guild.members.fetch(userId);
      if (!member) continue;
      await member.roles.remove(mutedRole);
    }
    await WarningModel.deleteMany(query);
    setTimeout(check, 1000 * 3 * 60);
  };

  check();
};

import { MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";
import WarningModel from "../../models/Warning.model";

export default {
  category: "Moderation",
  description: "Warn a user",
  name: "warn",
  permissions: ["MANAGE_MESSAGES"],
  slash: true,
  testOnly: true,
  guildOnly: true,

  options: [
    {
      type: "SUB_COMMAND",
      name: "add",
      description: "Add a warning to a user.",
      options: [
        {
          name: "user",
          type: "USER",
          description: "The user to add a warning to.",
          required: true,
        },
        {
          name: "reason",
          type: "STRING",
          description: "The reason for the warning.",
          required: true,
        },
      ],
    },
    {
      type: "SUB_COMMAND",
      name: "remove",
      description: "Remove a warning from the user.",
      options: [
        {
          name: "user",
          type: "USER",
          description: "The user to remove the warning from.",
          required: true,
        },
        {
          name: "id",
          type: "STRING",
          description: "The ID of the warning to remove.",
          required: true,
        },
      ],
    },
    {
      type: "SUB_COMMAND",
      name: "list",
      description: "List all warnings",
      options: [
        {
          name: "user",
          type: "USER",
          description: "The user to list warnings for.",
          required: true,
        },
      ],
    },
    {
      type: "SUB_COMMAND",
      name: "clear",
      description: "Clear all warnings from a user.",
      options: [
        {
          name: "user",
          type: "USER",
          description: "The user to clear warnings from.",
          required: true,
        },
      ],
    },
  ],
  callback: async ({ guild, member: staff, interaction }) => {
    const subCommand = interaction.options.getSubcommand();
    const user = interaction.options.getUser("user");
    const reason = interaction.options.getString("reason");
    const id = interaction.options.getString("id");

    if (subCommand === "add") {
      const warning = await WarningModel.create({
        userId: user?.id,
        staffId: staff.id,
        guildId: guild?.id,
        reason,
      });
      return {
        custom: true,
        content: `Added warning ${warning.id} to <@${user?.id}>`,
      };
    } else if (subCommand === "remove") {
      const warning = await WarningModel.findByIdAndDelete(id);
      return {
        custom: true,
        content: `Removed warning ${warning.id} from <@${user?.id}>`,
      };
    } else if (subCommand === "list") {
      const warnings = await WarningModel.find({
        userId: user?.id,
        guildId: guild?.id,
      });

      let description = `<@${user?.id}> has ${warnings.length} warnings.\n\n`;

      for (const warning of warnings) {
        description += `**ID:** ${warning.id}\n`;
        description += `**Reason:** ${warning.reason}\n`;
        description += `**Staff:** <@${warning.staffId}>\n`;
        description += `**Date:** ${warning.createdAt.toLocaleString()})\n\n`;
      }
      return new MessageEmbed().setDescription(description);
    } else if (subCommand === "clear") {
      const warnings = await WarningModel.deleteMany({
        userId: user?.id,
        guildId: guild?.id,
      });
      return {
        custom: true,
        content: `Cleared ${warnings.deletedCount} warnings from <@${user?.id}>`,
      };
    }
    return "Could not find subcommand.";
  },
} as ICommand;

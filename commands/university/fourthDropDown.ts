import {
  Client,
  GuildMember,
  MessageActionRow,
  MessageSelectMenu,
  MessageSelectOptionData,
  Role,
  TextChannel,
} from "discord.js";
import { ICommand } from "wokcommands";

export default {
  category: "Administrator",
  name: "fourthDropDown",
  description: "Add a role to the auto role dropdown.",
  permissions: ["ADMINISTRATOR"],
  slash: true,
  testOnly: true,
  guildOnly: true,
  minArgs: 3,
  maxArgs: 3,
  expectedArgs: "<channel> <messageID> <role>",
  expectedArgsTypes: ["CHANNEL", "STRING", "ROLE"],

  init: (client: Client) => {
    client.on("interactionCreate", (interaction) => {
      if (!interaction.isSelectMenu()) return;
      const { customId, values, member } = interaction;
      if (customId === "auto_rolesV4" && member instanceof GuildMember) {
        const component = interaction.component as MessageSelectMenu;
        const removed = component.options.filter((option) => {
          return !values.includes(option.value);
        });

        for (const id of removed) {
          member.roles.remove(id.value);
          interaction.reply({
            ephemeral: true,
            content: `Removed role ${id.label} from user.`,
            allowedMentions: {
              users: [],
            },
          });
        }

        for (const id of values) {
          member.roles.add(id);
          interaction.reply({
            ephemeral: true,
            content: `Added role ${id} to user.`,
            allowedMentions: {
              users: [],
            },
          });
        }
      }
    });
  },
  callback: async ({ interaction, args, client }) => {
    const channel = interaction.options.getChannel("channel") as TextChannel;
    if (!channel || channel.type !== "GUILD_TEXT")
      return "Please tag a valid text channel.";

    const role = interaction.options.getRole("role") as Role;
    if (!role) return "Please tag a valid role.";

    const messageID = args[1];
    const targetMessage = await channel.messages.fetch(messageID, {
      cache: true,
      force: true,
    });
    if (!targetMessage) return "Could not find the specified message.";
    if (targetMessage.author.id !== client.user?.id)
      return "The specified message is not originally from the bot.";

    let row = targetMessage.components[0];
    if (!row) row = new MessageActionRow();

    const option: MessageSelectOptionData[] = [
      {
        label: role.name,
        value: role.id,
      },
    ];

    let menu = row.components[0] as MessageSelectMenu;
    if (menu) {
      for (const item of menu.options)
        if (item.value == option[0].value)
          return {
            custom: true,
            content: `<@&{item.value}> is already in the auto role dropdown.`,
            allowedMentions: {
              roles: [],
            },
            ephemeral: true,
          };

      menu.addOptions(option);
      menu.setMaxValues(menu.options.length);
    } else {
      row.addComponents(
        new MessageSelectMenu()
          .setCustomId("auto_rolesV4")
          .setMinValues(0)
          .setMaxValues(1)
          .setPlaceholder("Select your roles...")
          .addOptions(option)
      );
    }

    targetMessage.edit({
      components: [row],
    });

    return {
      custom: true,
      content: `<@&${role.id}> has been added to the auto role dropdown.`,
      allowedMentions: {
        roles: [],
      },
      ephemeral: true,
    };
  },
} as ICommand;

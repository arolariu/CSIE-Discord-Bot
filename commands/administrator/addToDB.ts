import { ICommand } from "wokcommands";
import UserInterface from "../../interfaces/User.interface";
import UserModel from "../../models/User.model";

export default {
  category: "Administrator",
  description: "Generate JSON file with every user's info.",
  name: "AddToDB",
  slash: false,
  testOnly: true,
  guildOnly: true,
  permissions: ["ADMINISTRATOR"],

  callback: async () => {
    const userDATA: UserInterface[] = require("../../data/users.json");

    const startTime = Date.now();
    userDATA.forEach(async (user: UserInterface) => {
      const userModel = new UserModel({
        id: user.id,
        name: user.username,
        discriminator: user.discriminator,
        avatar: user.avatar,
        createdAt: user.createdAt,
        joinedAt: user.joinedAt,
        technologies: user.technologies,
        career: user.career,
        degree: user.degree,
      });
      await userModel.save();
    });

    const endTime = Date.now();

    return `Done! It took me ~${endTime - startTime} ms to add ${
      userDATA.length
    } users to the database.`;
  },
} as ICommand;

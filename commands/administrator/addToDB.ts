import { ICommand } from "wokcommands";
import IUser from "../../interfaces/User.interface";
import UserModel from "../../models/User.model";

export default {
  category: "Administrator",
  description: "Add and/or refresh the users in the MongoDB database.",
  name: "AddToDB",
  slash: "both",
  testOnly: true,
  guildOnly: true,
  permissions: ["ADMINISTRATOR"],
  cooldown: "5m",

  callback: async () => {
    // 0. Fetch the user's JSON file.
    const userDATA: IUser[] = require("../../data/users.json");

    // 1. For each user in the JSON file, add them to the database.
    const startTime = Date.now();
    userDATA.forEach((user: IUser) => {
      const userEntry = new UserModel(user);
      // 2. Check if the user already exists in the database.
      UserModel.findOne({ id: user.id }, (err: any, existingUser: IUser) => {
        if (err) return `Error: ${err}`;
        if (!existingUser) return userEntry.save();
      });
    });

    const endTime = Date.now();

    // 3. Send a message to the channel.
    return `Done! It took me ~${endTime - startTime} ms call the MongoDB driver.
    Please be patient while the driver is executing background tasks.`;
  },
} as ICommand;

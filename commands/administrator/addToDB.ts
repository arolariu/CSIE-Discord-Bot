import { Error } from "mongoose";
import { ICommand } from "wokcommands";
import IUser from "../../interfaces/User.interface";
import UserModel from "../../models/User.model";

export default {
  category: "Administrator",
  description: "Add and/or refresh the users in the MongoDB database.",
  name: "AddToDB",
  slash: true,
  testOnly: true,
  guildOnly: true,
  permissions: ["ADMINISTRATOR"],
  //cooldown: "5m",
  maxArgs: 1,
  expectedArgs: "<path to the users json>",
  expectedArgsTypes: ["STRING"],
  callback: async ({ args }) => {
    const path = args.shift() ?? "../../data/users.json";
    let users: IUser[] = [];
    try {
      users = require(path);
    } catch (e) {
      return `Failed to fetch the users.json file.${e}`;
    }

    const startTime = Date.now();
    users.forEach((user: IUser) => {
      const userEntry = new UserModel(user);
      // Check if the user already exists in the database.
      const query = { id: user.id };
      UserModel.findOne(query, (err: Error, dbUser: IUser) => {
        if (err) return console.error(err);
        if (!dbUser) userEntry.save();
        else return console.log("Found:" + dbUser.username);
      });
    });

    const endTime = Date.now();

    // 3. Send a message to the channel.
    return `Done! It took me ~${endTime - startTime} ms call the MongoDB driver.
    Please be patient while the driver is executing background tasks.`;
  },
} as ICommand;

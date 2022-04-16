import { ICommand } from "wokcommands";

export default {
  category: "Utility",
  description: "Add two numbers together.",
  name: "add",
  slash: "both",
  testOnly: true,
  cooldown: "10s",
  expectedArgs: "<number> <number>",
  minArgs: 2,
  maxArgs: 2,
  syntaxError: {
    message: "You need to provide two numbers to add together.",
    usage: "add <number 1> <number 2>",
  },

  callback: ({ args }) => {
    const num1 = parseInt(args[0]);
    const num2 = parseInt(args[1]);
    return `${num1} + ${num2} = ${num1 + num2}`;
  },
} as ICommand;

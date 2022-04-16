import mongoose from "mongoose";

const UserSchema = new mongoose.Schema({
  id: {
    type: Number,
    required: true,
    unique: true,
    primaryKey: true,
  },
  username: {
    type: String,
    required: true,
  },
  discordTAG: {
    type: String,
    default: "NA",
  },
  avatar: {
    type: String,
    default: "https://cdn.discordapp.com/embed/avatars/1.png",
  },
  createdAt: {
    type: Date,
    required: true,
  },
  joinedAt: {
    type: Date,
    required: true,
  },
  technologies: {
    type: String,
    required: true,
  },
  career: {
    type: String,
    required: true,
  },
  degree: {
    type: String,
    required: true,
  },
});

export default mongoose.model("Licenta-Users", UserSchema);

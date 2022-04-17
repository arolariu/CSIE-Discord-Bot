import mongoose from "mongoose";

const UserSchema = new mongoose.Schema({
  id: {
    type: String,
    required: true,
    unique: true,
    primaryKey: true,
  },
  username: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    default: "password",
  },
  email: {
    type: String,
  },
  avatarURL: {
    type: String,
    default: "https://cdn.discordapp.com/embed/avatars/1.png",
  },
  verified: {
    type: Boolean,
    default: false,
  },
  discordTAG: {
    type: String,
    default: "NA",
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

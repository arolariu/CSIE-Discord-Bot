import mongoose from "mongoose";

const UserSchema = new mongoose.Schema({
  _id: {
    type: Number,
    required: true,
    unique: true,
    primaryKey: true,
  },
  name: {
    type: String,
    required: true,
  },
  discriminator: {
    type: String,
    required: true,
  },
  avatar: {
    type: String,
    required: true,
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

export default mongoose.model("Users", UserSchema);

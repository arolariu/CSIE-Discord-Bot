import mongoose from "mongoose";

const requiredString = {
  type: String,
  required: true,
};

const warningSchema = new mongoose.Schema({
  guildId: requiredString,
  userId: requiredString,
  staffId: requiredString,
  reason: requiredString,
  expiresAt: {
    type: Date,
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
  updatedAt: {
    type: Date,
    default: Date.now,
  },
});

export default mongoose.model("Warnings", warningSchema);

import mongoose, { Schema } from "mongoose";

const welcomeSchema = new Schema({
  _id: {
    type: String,
    required: true,
  },
  channelId: {
    type: String,
    required: true,
  },
  text: {
    type: String,
    required: true,
  },
});

export default mongoose.model("welcomes", welcomeSchema);

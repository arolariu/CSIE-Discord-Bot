export default interface IUser {
  id: string;
  username: string;
  password: string | null;
  email: string | null;
  avatarURL: string;
  verified: boolean;
  discordTAG: string;
  createdAt: Date;
  joinedAt: Date;
  technologies: string;
  career: string;
  degree: string;
}

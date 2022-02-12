export default interface User {
  id: string;
  username: string;
  discriminator: string;
  avatar: string | null;
  createdAt: Date;
  joinedAt: Date | null;
  technologies: string;
  career: string;
  degree: string;
}

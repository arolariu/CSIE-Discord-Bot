export default function sanitizeUID(UID: string): string {
  if (!UID || UID.length <= 10) throw new Error("Invalid user ID.");
  if (UID.startsWith("<@") && UID.endsWith(">")) {
    UID = UID.slice(2, -1);
    if (UID.startsWith("!")) UID = UID.slice(1);
  }
  return UID;
}

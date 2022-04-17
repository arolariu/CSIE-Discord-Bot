import axios from "axios";
export default async function generateLoremIpsum(
  number: number
): Promise<string> {
  const baseUrl = "https://baconipsum.com/api/?type=all-meat";
  const url = `${baseUrl}&paras=${number}`;
  const response = await axios.get(url);
  return response.data[0];
}

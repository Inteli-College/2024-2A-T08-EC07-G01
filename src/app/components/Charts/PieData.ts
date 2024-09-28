import axios from "axios";

export interface TestPieChart {
  name: string;
  total: number;
  predicted: number;
}

const baseURL = "http://localhost:8000/api/predictions";

export async function getTotalFailsChart(): Promise<TestPieChart[]> {
  try {
    const response = await axios.get(`${baseURL}/total-fails`);
    const data = response.data;

    return [
      { name: "No Fails", total: data.no_fails, predicted: 0 },
      { name: "Fails", total: data.fails, predicted: 0 },
    ];
  } catch (error) {
    console.error("Error fetching total fails data:", error);
    return [];
  }
}

export async function getFailCodesChart(): Promise<TestPieChart[]> {
  try {
    const response = await axios.get(`${baseURL}/fail-codes-predicted`);
    const data = response.data;

    return Object.keys(data).map((key) => ({
      name: `Code ${key}`,
      total: data[key],
      predicted: 0,
    }));
  } catch (error) {
    console.error("Error fetching fail codes data:", error);
    return [];
  }
}

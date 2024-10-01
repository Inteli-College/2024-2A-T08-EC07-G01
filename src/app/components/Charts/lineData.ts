import axios from "axios";
import LineChart from "./LineChart.vue";
export interface LineChartData {
  "real_fail_code_count": Month[];
  "predicted_fail_code_count": Month[];
}

export interface Month {
  name: string;
  value: number;
}



export async function fetchChartData(isFromFails: boolean): Promise<LineChartData> {
  const baseURL = "http://localhost:8000/api/predictions";

  try {
    let response;
    if (isFromFails) {
      response = await axios.get(`${baseURL}/fail-codes-by-month'`);
      const responseData = response.data;

      return [
        { name: "Sem Falha", total: responseData.no_fails, predicted: 0 },
        { name: "Com Falha", total: responseData.fails, predicted: 0 },
      ];
    } else {
      response = await axios.get(`${baseURL}/fail-codes-predicted`);
      const responseData = response.data;

      // return Object.keys(responseData).map((key) => ({
      //   name: `Falha ${key}`,
      //   total: responseData[key],
      //   predicted: 0,
      // }));
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    return []; // Reset to empty if there's an error
  }
}


export function getLineChart(): DataSets {
  return {
    TodasFalhas: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },

    ],
    Classe_1: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

    Classe_2: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

    Classe_3: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

    Classe_4: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

    Classe_5: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

    Classe_6: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

    Classe_7: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

    Classe_8: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

    Classe_9: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200) / 100, 'Import Growth Rate': Math.floor(Math.random() * 200) / 100 },
    ],

  };
}

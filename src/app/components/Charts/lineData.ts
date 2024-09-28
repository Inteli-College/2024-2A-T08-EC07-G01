// LineData.ts
export interface TestLineChart {
  year: number;
  'Export Growth Rate': number;
  'Import Growth Rate': number;
}

export type DataSets = {
  [key: string]: TestLineChart[];
};

export function getLineChart(): DataSets {
  return {
    TodasFalhas: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
     
    ],
    Classe_1: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],
    
    Classe_2: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],

    Classe_3: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],

    Classe_4: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],

    Classe_5: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],

    Classe_6: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],

    Classe_7: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],

    Classe_8: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],

    Classe_9: [
      { year: 1970, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1971, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1972, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1973, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1974, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1975, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
      { year: 1976, 'Export Growth Rate': Math.floor(Math.random() * 200)/100, 'Import Growth Rate': Math.floor(Math.random() * 200)/100},
    ],

  };
}

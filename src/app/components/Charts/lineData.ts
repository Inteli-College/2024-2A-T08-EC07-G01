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
    set1: [
      { year: 1970, 'Export Growth Rate': 2.04, 'Import Growth Rate': 1.53 },
      { year: 1971, 'Export Growth Rate': 1.96, 'Import Growth Rate': 1.58 },
      { year: 1972, 'Export Growth Rate': 1.96, 'Import Growth Rate': 1.61 },
      { year: 1973, 'Export Growth Rate': 1.93, 'Import Growth Rate': 1.61 },
      { year: 1974, 'Export Growth Rate': 1.88, 'Import Growth Rate': 1.67 },
      { year: 1975, 'Export Growth Rate': 1.79, 'Import Growth Rate': 1.64 },
      { year: 1976, 'Export Growth Rate': 1.77, 'Import Growth Rate': 1.62 },
      { year: 1977, 'Export Growth Rate': 1.74, 'Import Growth Rate': 1.69 },
      { year: 1978, 'Export Growth Rate': 1.74, 'Import Growth Rate': 1.7 },
      { year: 1979, 'Export Growth Rate': 1.77, 'Import Growth Rate': 1.67 },
      { year: 1980, 'Export Growth Rate': 1.79, 'Import Growth Rate': 1.7 },
      { year: 1981, 'Export Growth Rate': 1.81, 'Import Growth Rate': 1.72 },
      { year: 1982, 'Export Growth Rate': 1.84, 'Import Growth Rate': 1.73 },
      { year: 1983, 'Export Growth Rate': 1.77, 'Import Growth Rate': 1.73 },
      { year: 1984, 'Export Growth Rate': 1.78, 'Import Growth Rate': 1.78 },
      { year: 1985, 'Export Growth Rate': 1.78, 'Import Growth Rate': 1.81 },
      { year: 1986, 'Export Growth Rate': 1.82, 'Import Growth Rate': 1.89 },
    ],
    set2: [
      { year: 1980, 'Export Growth Rate': 1.79, 'Import Growth Rate': 1.7 },
      { year: 1981, 'Export Growth Rate': 1.81, 'Import Growth Rate': 1.72 },
      { year: 1982, 'Export Growth Rate': 1.84, 'Import Growth Rate': 1.73 },
      { year: 1983, 'Export Growth Rate': 1.77, 'Import Growth Rate': 1.73 },
      { year: 1984, 'Export Growth Rate': 1.78, 'Import Growth Rate': 1.78 },
      { year: 1985, 'Export Growth Rate': 1.78, 'Import Growth Rate': 1.81 },
      { year: 1986, 'Export Growth Rate': 1.82, 'Import Growth Rate': 1.89 },
      { year: 1987, 'Export Growth Rate': 1.82, 'Import Growth Rate': 1.91 },
      { year: 1988, 'Export Growth Rate': 1.77, 'Import Growth Rate': 1.94 },
      { year: 1989, 'Export Growth Rate': 1.76, 'Import Growth Rate': 1.94 },
      { year: 1990, 'Export Growth Rate': 1.75, 'Import Growth Rate': 1.97 },
      { year: 1991, 'Export Growth Rate': 1.62, 'Import Growth Rate': 1.99 },
      { year: 1992, 'Export Growth Rate': 1.56, 'Import Growth Rate': 2.12 },
      { year: 1993, 'Export Growth Rate': 1.5, 'Import Growth Rate': 2.13 },
      { year: 1994, 'Export Growth Rate': 1.46, 'Import Growth Rate': 2.15 },
    ],
  };
}

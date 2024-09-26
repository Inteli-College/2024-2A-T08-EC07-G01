interface testBarChart {
    name: string;
    total: number;
    predicted: number;
  }
  
  export type DataSets = {
    [key: string]: testBarChart[];
  }
  
  export function getBarChart(): DataSets {
    return {
      set1: [
        { name: 'Jan', total: Math.floor(Math.random() * 2000) + 500, predicted: Math.floor(Math.random() * 2000) + 500 },
        { name: 'Feb', total: Math.floor(Math.random() * 2000) + 500, predicted: Math.floor(Math.random() * 2000) + 500 },
        { name: 'Mar', total: Math.floor(Math.random() * 2000) + 500, predicted: Math.floor(Math.random() * 2000) + 500 },
        { name: 'Apr', total: Math.floor(Math.random() * 2000) + 500, predicted: Math.floor(Math.random() * 2000) + 500 },
        { name: 'May', total: Math.floor(Math.random() * 2000) + 500, predicted: Math.floor(Math.random() * 2000) + 500 },
        { name: 'Jun', total: Math.floor(Math.random() * 2000) + 500, predicted: Math.floor(Math.random() * 2000) + 500 },
        { name: 'Jul', total: Math.floor(Math.random() * 2000) + 500, predicted: Math.floor(Math.random() * 2000) + 500 },
      ],
      set2: [
        { name: 'Jan', total: Math.floor(Math.random() * 3000) + 1000, predicted: Math.floor(Math.random() * 3000) + 1000 },
        { name: 'Feb', total: Math.floor(Math.random() * 3000) + 1000, predicted: Math.floor(Math.random() * 3000) + 1000 },
        { name: 'Mar', total: Math.floor(Math.random() * 3000) + 1000, predicted: Math.floor(Math.random() * 3000) + 1000 },
        { name: 'Apr', total: Math.floor(Math.random() * 3000) + 1000, predicted: Math.floor(Math.random() * 3000) + 1000 },
        { name: 'May', total: Math.floor(Math.random() * 3000) + 1000, predicted: Math.floor(Math.random() * 3000) + 1000 },
        { name: 'Jun', total: Math.floor(Math.random() * 3000) + 1000, predicted: Math.floor(Math.random() * 3000) + 1000 },
        { name: 'Jul', total: Math.floor(Math.random() * 3000) + 1000, predicted: Math.floor(Math.random() * 3000) + 1000 },
      ],
    };
  }
  
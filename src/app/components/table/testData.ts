// testDataService.ts
export interface TestData {
    knr: string;
    dataPrevisao: string;
    falha: string;
    tipoFalha: string;
    testeIndicado: string;
  }
  
  export const fetchTestData = async (): Promise<TestData[]> => {
    try {
      const response = await fetch('http://localhost:8000/api/predictions/')
      const result = await response.json()
  
      return result.map((prediction: any) => ({
        knr: prediction.KNR,
        dataPrevisao: new Date().toISOString().split('T')[0], 
        falha: prediction.predicted_fail_codes && prediction.predicted_fail_codes.length > 0 ? 'Yes' : 'No',
        tipoFalha: prediction.predicted_fail_codes?.join(', ') || 'No predicted failure',
        testeIndicado: prediction.indicated_tests?.join(', ') || 'No test indicated',
      }))
    } catch (error) {
      console.error('Error fetching data:', error)
      return []
    }
  }
  
// knrsData.ts
export interface KNRData {
    knr: string;
    hasFailure: boolean;
    failureType: string | null;
  }
  
  // Dados mocados
  export function getMockedKNRData(): KNRData[] {
    return [
      { knr: '7777', hasFailure: false, failureType: null },
      { knr: '2023-2056234', hasFailure: true, failureType: 'Tipo 7' },
      { knr: '1234', hasFailure: true, failureType: 'Tipo 3' },
      { knr: '12345', hasFailure: true, failureType: 'Tipo 6' },
    ];
  }
  
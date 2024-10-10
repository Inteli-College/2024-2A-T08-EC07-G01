import { failTypes } from "../../pages/prediction/knrsData";

export interface Prediction {
  KNR: string;
  predicted_fail_codes: number[];
  real_fail_codes: number[];
  indicated_tests: string[];
}

export interface TableData {
  knr: string;
  //   dataPrevisao: string;
  falha: string;
  tipoFalha: string;
  testeIndicado: string;
}
export const convertPredictionToTableData = (
  predictionData: Prediction[]
): TableData[] => {
  // Helper function to map fail codes to their descriptions
  const getFailDescription = (failCode: number): string | null => {
    const failType = failTypes.value.find((ft) => ft.failType === failCode);
    return failType ? failType.description : null;
  };

  return predictionData.map((prediction) => {
    const realFailDescriptions =
      prediction.real_fail_codes
        .map((code) => getFailDescription(code))
        .filter((desc) => desc !== null)
        .join(", ") || "Sem Falhas";

    const predictedFailDescriptions =
      prediction.predicted_fail_codes
        .map((code) => getFailDescription(code))
        .filter((desc) => desc !== null)
        .join(", ") || "Sem Falhas";

    return {
      knr: prediction.KNR,
      falha: realFailDescriptions,
      tipoFalha:
        predictedFailDescriptions.length > 0
          ? predictedFailDescriptions
          : "Não Previsto",
      testeIndicado: prediction.indicated_tests.join(", ") || "Sem Testes",
    };
  });
};

// export const TestData: TableData[] = [
//   {
//     knr: "12345",
//     // dataPrevisao: "2024-08-30",
//     falha: "Conexão Interrompida",
//     tipoFalha: "Hardware",
//     testeIndicado: "Verificar Cabos",
//   },
//   {
//     knr: "67890",
//     // dataPrevisao: "2024-09-15",
//     falha: "Erro de Software",
//     tipoFalha: "Software",
//     testeIndicado: "Reinstalar Sistema",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "44556",
//     // dataPrevisao: "2024-11-20",
//     falha: "Falha de Rede",
//     tipoFalha: "Network",
//     testeIndicado: "Testar Conexão",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
//   {
//     knr: "11223",
//     // dataPrevisao: "2024-10-01",
//     falha: "Superaquecimento",
//     tipoFalha: "Hardware",
//     testeIndicado: "Limpeza de Ventoinha",
//   },
// ];
// //

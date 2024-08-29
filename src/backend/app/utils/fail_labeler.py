from app.models.KNR import KNR

fails = {
    1: "Parte Traseira",
    2: "Parte Central",
    4: "Portas",
    5: "Parte Dianteira",
    133: "Geral",
    137: "Assoalho Externo",
    140: "Documentação",
    9830945: "Teste Backoffice",
    9830946: "Elétrica",
}


def label_knr(knr: KNR) -> KNR:
    print('pre')
    print(knr)
    if knr.real_fail == '':
        knr.real_fail = fails.get(knr.real_fail_code, "")

    if knr.predicted_fail == '':
        knr.predicted_fail = fails.get(knr.predicted_fail_code, "")

    print('pos')
    print(knr)

    return knr

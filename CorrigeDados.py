from OperaBanco import brasileiro_stat_insert
import oracledb
import os
from dotenv import load_dotenv
import json


load_dotenv()
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
dsn = os.getenv("DSN")
walletpw = os.getenv("WALLET_PW")
wallet_location = r'.\Wallet'

try:
    con = oracledb.connect(user=usuario, password=senha, dsn=dsn, config_dir=wallet_location,  wallet_location=wallet_location, wallet_password=walletpw)
except oracledb.DatabaseError as e:
    error, = e.args
    print("Erro ao conectar ao banco de dados Oracle:", error.message)


cursor = con.cursor()

def jogo_completo_dados(jogo_completo,ID_Partida,Temporada):
    conta = 0
    for x in jogo_completo:
         print(x,conta)
         conta = conta + 1

    Dribles_Mandante = jogo_completo[28]['Mandante']
    Dribles_Visitante = jogo_completo[28]['Visitante']
    Cruzamento_Mandante = jogo_completo[27]['Mandante']
    Cruzamento_Visitante = jogo_completo[27]['Visitante']
    BolaLonga_Mandante = jogo_completo[26]['Mandante']
    BolaLonga_Visitante = jogo_completo[26]['Visitante']
    PassesPrecisos_Mandante = jogo_completo[25]['Mandante']
    PassesPrecisos_Visitante = jogo_completo[25]['Visitante']

    DribleCertoMandante, DribleTotalMandante = Dribles_Mandante.split("/")
    DribleCertoVisitante, DribleTotalVisitante = Dribles_Visitante.split("/")
    CruzamentoCertoMandante, CruzamentoTotalMandante = Cruzamento_Mandante.split("/")
    CruzamentoCertoVisitante, CruzamentoTotalVisitante = Cruzamento_Visitante.split("/")
    BolaLongaCertoMandante, BolaLongaTotalMandante = BolaLonga_Mandante.split("/")
    BolaLongaCertoVisitante, BolaLongaTotalVisitante = BolaLonga_Visitante.split("/")
    PassesPrecisos_Mandante = PassesPrecisos_Mandante.split(" ")
    PassesPrecisos_Visitante = PassesPrecisos_Visitante.split(" ")
    PassesPrecisos_Mandante = PassesPrecisos_Mandante[0]
    PassesPrecisos_Visitante = PassesPrecisos_Visitante[0]

    DribleCertoMandante = DribleCertoMandante.strip()
    DribleTotalMandante = DribleTotalMandante.split("(")[0].strip()
    DribleCertoVisitante = DribleCertoVisitante.strip()
    DribleTotalVisitante = DribleTotalVisitante.split("(")[0].strip()
    CruzamentoCertoMandante = CruzamentoCertoMandante.strip()
    CruzamentoTotalMandante = CruzamentoTotalMandante.split("(")[0].strip()
    CruzamentoCertoVisitante = CruzamentoCertoVisitante.strip()
    CruzamentoTotalVisitante = CruzamentoTotalVisitante.split("(")[0].strip()
    BolaLongaCertoMandante = BolaLongaCertoMandante.strip()
    BolaLongaTotalMandante = BolaLongaTotalMandante.split("(")[0].strip()
    BolaLongaCertoVisitante = BolaLongaCertoVisitante.strip()
    BolaLongaTotalVisitante = BolaLongaTotalVisitante.split("(")[0].strip()
    PassesPrecisos_Mandante = PassesPrecisos_Mandante.split("(")[0].strip()
    PassesPrecisos_Visitante = PassesPrecisos_Visitante.split("(")[0].strip()
    print(CruzamentoTotalMandante)

    jogo_completo_stats = {
        "ID_Partida": int(ID_Partida),
        "Periodo": "ALL",
        "Temporada": Temporada,
        "Posse_Mandante": int(jogo_completo[1]['Mandante']),
        "Posse_Visitante": int(jogo_completo[1]['Visitante']),
        "ChutesTotal_Mandante": int(jogo_completo[2]['Mandante']),
        "ChutesTotal_Visitante": int(jogo_completo[2]['Visitante']),
        "ChutesAlvo_Mandante": int(jogo_completo[3]['Mandante']),
        "ChutesAlvo_Visitante": int(jogo_completo[3]['Visitante']),
        "ChutesFora_Mandante": int(jogo_completo[4]['Mandante']),
        "ChutesFora_Visitante": int(jogo_completo[4]['Visitante']),
        "ChutesBloqueados_Mandante": int(jogo_completo[5]['Mandante']),
        "ChutesBloqueados_Visitante": int(jogo_completo[5]['Visitante']),
        "Escanteios_Mandante": int(jogo_completo[6]['Mandante']),
        "Escanteios_Visitante": int(jogo_completo[6]['Visitante']),
        "Impedimento_Mandante": int(jogo_completo[7]['Mandante']),
        "Impedimento_Visitante": int(jogo_completo[7]['Visitante']),
        "Faltas_Mandante": int(jogo_completo[8]['Mandante']),
        "Faltas_Visitante": int(jogo_completo[8]['Visitante']),
        "Amarelo_Mandante": int(jogo_completo[9]['Mandante']),
        "Amarelo_Visitante": int(jogo_completo[9]['Visitante']),
        "Vermelho_Mandante": int(jogo_completo[10]['Mandante']),
        "Vermelho_Visitante": int(jogo_completo[10]['Visitante']),
        "Lateral_Mandante": int(jogo_completo[12]['Mandante']),
        "Lateral_Visitante": int(jogo_completo[12]['Visitante']),
        "TiroMeta_Mandante": int(jogo_completo[13]['Mandante']),
        "TiroMeta_Visitante": int(jogo_completo[13]['Visitante']),
        "GrandesChances_Mandante": int(jogo_completo[14]['Mandante']),
        "GrandesChances_Visitante": int(jogo_completo[14]['Visitante']),
        "GrandesChancesPerdidas_Mandante": int(jogo_completo[15]['Mandante']),
        "GrandesChancesPerdidas_Visitante": int(jogo_completo[15]['Visitante']),
        "ContraAtaque_Mandante": int(jogo_completo[17]['Mandante']),
        "ContraAtaque_Visitante": int(jogo_completo[17]['Visitante']),
        "ChutesContraAtaque_Mandante": int(jogo_completo[18]['Mandante']),
        "ChutesContraAtaque_Visitante": int(jogo_completo[18]['Visitante']),
        "GolContraAtaque_Mandante": int(jogo_completo[19]['Mandante']),
        "GolContraAtaque_Visitante": int(jogo_completo[19]['Visitante']),
        "ChutesArea_Mandante": int(jogo_completo[20]['Mandante']),
        "ChutesArea_Visitante": int(jogo_completo[20]['Visitante']),
        "ChutesForaArea_Mandante": int(jogo_completo[21]['Mandante']),
        "ChutesForaArea_Visitante": int(jogo_completo[21]['Visitante']),
        "DefesasGoleiro_Mandante": int(jogo_completo[22]['Mandante']),
        "DefesasGoleiro_Visitante": int(jogo_completo[22]['Visitante']),
        "Passes_Mandante": int(jogo_completo[24]['Mandante']),
        "Passes_Visitante": int(jogo_completo[24]['Visitante']),
        "PassesPrecisos_Mandante": int(PassesPrecisos_Mandante),
        "PassesPrecisos_Visitante": int(PassesPrecisos_Visitante),
        "BolaLonga_Mandante": int(BolaLongaCertoMandante),
        "BolaLonga_Visitante": int(BolaLongaCertoVisitante),
        "BolaLongaTotal_Mandante": int(BolaLongaTotalMandante),
        "BolaLongaTotal_Visitante": int(BolaLongaTotalVisitante),
        "Cruzamento_Mandante": int(CruzamentoCertoMandante),
        "Cruzamento_Visitante": int(CruzamentoCertoVisitante),
        "CruzamentosTotal_Mandante": int(CruzamentoTotalMandante),
        "CruzamentosTotal_Visitante": int(CruzamentoTotalVisitante),
        "Dribles_Mandante": int(DribleCertoMandante),
        "Dribles_Visitante": int(DribleCertoVisitante),
        "DriblesTotal_Mandante": int(DribleTotalMandante),
        "DriblesTotal_Visitante": int(DribleTotalVisitante),
        "PerdaPosse_Mandante": int(jogo_completo[29]['Mandante']),
        "PerdaPosse_Visitante": int(jogo_completo[29]['Visitante']),
        "DuelosGanhos_Mandante": int(jogo_completo[30]['Mandante']),
        "DuelosGanhos_Visitante": int(jogo_completo[30]['Visitante']),
        "DueloAereoVencido_Mandante": int(jogo_completo[31]['Mandante']),
        "DueloAereoVencido_Visitante": int(jogo_completo[31]['Visitante']),
        "Desarmes_Mandante": int(jogo_completo[32]['Mandante']),
        "Desarmes_Visitante": int(jogo_completo[32]['Visitante']),

        "Interceptacoes_Mandante": int(jogo_completo[33]['Mandante']),
        "Interceptacoes_Visitante": int(jogo_completo[33]['Visitante']),
        "Cortes_Mandante": int(jogo_completo[34]['Mandante']),
        "Cortes_Visitante": int(jogo_completo[34]['Visitante'])
    }



    brasileiro_stat_insert(cursor, jogo_completo_stats)
    con.commit()
    jogo_completo.clear()

def primeiro_tempo_dados(primeiro_tempo, ID_Partida,Temporada):
    conta = 0
    for x in primeiro_tempo:
        print(x, conta)
        conta = conta + 1

    Dribles_Mandante = primeiro_tempo[25]['Mandante']
    Dribles_Visitante = primeiro_tempo[25]['Visitante']
    Cruzamento_Mandante = primeiro_tempo[24]['Mandante']
    Cruzamento_Visitante = primeiro_tempo[24]['Visitante']
    BolaLonga_Mandante = primeiro_tempo[23]['Mandante']
    BolaLonga_Visitante = primeiro_tempo[23]['Visitante']
    PassesPrecisos_Mandante = primeiro_tempo[22]['Mandante']
    PassesPrecisos_Visitante = primeiro_tempo[22]['Visitante']

    DribleCertoMandante, DribleTotalMandante = Dribles_Mandante.split("/")
    DribleCertoVisitante, DribleTotalVisitante = Dribles_Visitante.split("/")
    CruzamentoCertoMandante, CruzamentoTotalMandante = Cruzamento_Mandante.split("/")
    CruzamentoCertoVisitante, CruzamentoTotalVisitante = Cruzamento_Visitante.split("/")
    BolaLongaCertoMandante, BolaLongaTotalMandante = BolaLonga_Mandante.split("/")
    BolaLongaCertoVisitante, BolaLongaTotalVisitante = BolaLonga_Visitante.split("/")
    PassesPrecisos_Mandante = PassesPrecisos_Mandante.split(" ")
    PassesPrecisos_Visitante = PassesPrecisos_Visitante.split(" ")
    PassesPrecisos_Mandante = PassesPrecisos_Mandante[0]
    PassesPrecisos_Visitante = PassesPrecisos_Visitante[0]

    DribleCertoMandante = DribleCertoMandante.strip()
    DribleTotalMandante = DribleTotalMandante.split("(")[0].strip()
    DribleCertoVisitante = DribleCertoVisitante.strip()
    DribleTotalVisitante = DribleTotalVisitante.split("(")[0].strip()
    CruzamentoCertoMandante = CruzamentoCertoMandante.strip()
    CruzamentoTotalMandante = CruzamentoTotalMandante.split("(")[0].strip()
    CruzamentoCertoVisitante = CruzamentoCertoVisitante.strip()
    CruzamentoTotalVisitante = CruzamentoTotalVisitante.split("(")[0].strip()
    BolaLongaCertoMandante = BolaLongaCertoMandante.strip()
    BolaLongaTotalMandante = BolaLongaTotalMandante.split("(")[0].strip()
    BolaLongaCertoVisitante = BolaLongaCertoVisitante.strip()
    BolaLongaTotalVisitante = BolaLongaTotalVisitante.split("(")[0].strip()
    PassesPrecisos_Mandante = PassesPrecisos_Mandante.split("(")[0].strip()
    PassesPrecisos_Visitante = PassesPrecisos_Visitante.split("(")[0].strip()

    primeiro_tempo_stats = {
        "ID_Partida": int(ID_Partida),
        "Periodo": "1ST",
        "Temporada": Temporada,
        "Posse_Mandante": int(primeiro_tempo[0]['Mandante']),
        "Posse_Visitante": int(primeiro_tempo[0]['Visitante']),
        "ChutesTotal_Mandante": int(primeiro_tempo[1]['Mandante']),
        "ChutesTotal_Visitante": int(primeiro_tempo[1]['Visitante']),
        "ChutesAlvo_Mandante": int(primeiro_tempo[2]['Mandante']),
        "ChutesAlvo_Visitante": int(primeiro_tempo[2]['Visitante']),
        "ChutesFora_Mandante": int(primeiro_tempo[3]['Mandante']),
        "ChutesFora_Visitante": int(primeiro_tempo[3]['Visitante']),
        "ChutesBloqueados_Mandante": int(primeiro_tempo[4]['Mandante']),
        "ChutesBloqueados_Visitante": int(primeiro_tempo[4]['Visitante']),
        "Escanteios_Mandante": int(primeiro_tempo[5]['Mandante']),
        "Escanteios_Visitante": int(primeiro_tempo[5]['Visitante']),
        "Impedimento_Mandante": int(primeiro_tempo[6]['Mandante']),
        "Impedimento_Visitante": int(primeiro_tempo[6]['Visitante']),
        "Amarelo_Mandante": int(primeiro_tempo[7]['Mandante']),
        "Amarelo_Visitante": int(primeiro_tempo[7]['Visitante']),
        "Vermelho_Mandante": int(primeiro_tempo[8]['Mandante']),
        "Vermelho_Visitante": int(primeiro_tempo[8]['Visitante']),
        "Faltas_Mandante": int(primeiro_tempo[9]['Mandante']),
        "Faltas_Visitante": int(primeiro_tempo[9]['Visitante']),
        "Lateral_Mandante": int(primeiro_tempo[10]['Mandante']),
        "Lateral_Visitante": int(primeiro_tempo[10]['Visitante']),
        "TiroMeta_Mandante": int(primeiro_tempo[11]['Mandante']),
        "TiroMeta_Visitante": int(primeiro_tempo[11]['Visitante']),
        "GrandesChances_Mandante": int(primeiro_tempo[12]['Mandante']),
        "GrandesChances_Visitante": int(primeiro_tempo[12]['Visitante']),
        "GrandesChancesPerdidas_Mandante": int(primeiro_tempo[13]['Mandante']),
        "GrandesChancesPerdidas_Visitante": int(primeiro_tempo[13]['Visitante']),
        "ContraAtaque_Mandante": int(primeiro_tempo[15]['Mandante']),
        "ContraAtaque_Visitante": int(primeiro_tempo[15]['Visitante']),
        "ChutesContraAtaque_Mandante": int(primeiro_tempo[16]['Mandante']),
        "ChutesContraAtaque_Visitante": int(primeiro_tempo[16]['Visitante']),
        "GolContraAtaque_Mandante": int(primeiro_tempo[17]['Mandante']),
        "GolContraAtaque_Visitante": int(primeiro_tempo[17]['Visitante']),
        "ChutesArea_Mandante": int(primeiro_tempo[18]['Mandante']),
        "ChutesArea_Visitante": int(primeiro_tempo[18]['Visitante']),
        "ChutesForaArea_Mandante": int(primeiro_tempo[19]['Mandante']),
        "ChutesForaArea_Visitante": int(primeiro_tempo[19]['Visitante']),
        "DefesasGoleiro_Mandante": int(primeiro_tempo[20]['Mandante']),
        "DefesasGoleiro_Visitante": int(primeiro_tempo[20]['Visitante']),
        "Passes_Mandante": int(primeiro_tempo[21]['Mandante']),
        "Passes_Visitante": int(primeiro_tempo[21]['Visitante']),
        "PassesPrecisos_Mandante": int(PassesPrecisos_Mandante),
        "PassesPrecisos_Visitante": int(PassesPrecisos_Visitante),
        "BolaLonga_Mandante": int(BolaLongaCertoMandante),
        "BolaLonga_Visitante": int(BolaLongaCertoVisitante),
        "BolaLongaTotal_Mandante": int(BolaLongaTotalMandante),
        "BolaLongaTotal_Visitante": int(BolaLongaTotalVisitante),
        "Cruzamento_Mandante": int(CruzamentoCertoMandante),
        "Cruzamento_Visitante": int(CruzamentoCertoVisitante),
        "CruzamentosTotal_Mandante": int(CruzamentoTotalMandante),
        "CruzamentosTotal_Visitante": int(CruzamentoTotalVisitante),
        "Dribles_Mandante": int(DribleCertoMandante),
        "Dribles_Visitante": int(DribleCertoVisitante),
        "DriblesTotal_Mandante": int(DribleTotalMandante),
        "DriblesTotal_Visitante": int(DribleTotalVisitante),
        "PerdaPosse_Mandante": int(primeiro_tempo[26]['Mandante']),
        "PerdaPosse_Visitante": int(primeiro_tempo[26]['Visitante']),
        "DuelosGanhos_Mandante": int(primeiro_tempo[27]['Mandante']),
        "DuelosGanhos_Visitante": int(primeiro_tempo[27]['Visitante']),
        "DueloAereoVencido_Mandante": int(primeiro_tempo[28]['Mandante']),
        "DueloAereoVencido_Visitante": int(primeiro_tempo[28]['Visitante']),
        "Desarmes_Mandante": int(primeiro_tempo[29]['Mandante']),
        "Desarmes_Visitante": int(primeiro_tempo[29]['Visitante']),
        "Interceptacoes_Mandante": int(primeiro_tempo[30]['Mandante']),
        "Interceptacoes_Visitante": int(primeiro_tempo[30]['Visitante']),
        "Cortes_Mandante": int(primeiro_tempo[31]['Mandante']),
        "Cortes_Visitante": int(primeiro_tempo[31]['Visitante'])
    }
    brasileiro_stat_insert(cursor, primeiro_tempo_stats)
    con.commit()
    primeiro_tempo.clear()
    print('inserido com sucesso')

def segundo_tempo_dados(segundo_tempo,ID_Partida,Temporada):
        conta = 0
        for x in segundo_tempo:
          print(x, conta)
          conta = conta + 1

        Dribles_Mandante = segundo_tempo[25]['Mandante']
        Dribles_Visitante = segundo_tempo[25]['Visitante']
        Cruzamento_Mandante = segundo_tempo[24]['Mandante']
        Cruzamento_Visitante = segundo_tempo[24]['Visitante']
        BolaLonga_Mandante = segundo_tempo[23]['Mandante']
        BolaLonga_Visitante = segundo_tempo[23]['Visitante']
        PassesPrecisos_Mandante = segundo_tempo[22]['Mandante']
        PassesPrecisos_Visitante = segundo_tempo[22]['Visitante']

        DribleCertoMandante, DribleTotalMandante = Dribles_Mandante.split("/")
        DribleCertoVisitante, DribleTotalVisitante = Dribles_Visitante.split("/")
        CruzamentoCertoMandante, CruzamentoTotalMandante = Cruzamento_Mandante.split("/")
        CruzamentoCertoVisitante, CruzamentoTotalVisitante = Cruzamento_Visitante.split("/")
        BolaLongaCertoMandante, BolaLongaTotalMandante = BolaLonga_Mandante.split("/")
        BolaLongaCertoVisitante, BolaLongaTotalVisitante = BolaLonga_Visitante.split("/")
        PassesPrecisos_Mandante = PassesPrecisos_Mandante.split(" ")
        PassesPrecisos_Visitante = PassesPrecisos_Visitante.split(" ")
        PassesPrecisos_Mandante = PassesPrecisos_Mandante[0]
        PassesPrecisos_Visitante = PassesPrecisos_Visitante[0]

        DribleCertoMandante = DribleCertoMandante.strip()
        DribleTotalMandante = DribleTotalMandante.split("(")[0].strip()
        DribleCertoVisitante = DribleCertoVisitante.strip()
        DribleTotalVisitante = DribleTotalVisitante.split("(")[0].strip()
        CruzamentoCertoMandante = CruzamentoCertoMandante.strip()
        CruzamentoTotalMandante = CruzamentoTotalMandante.split("(")[0].strip()
        CruzamentoCertoVisitante = CruzamentoCertoVisitante.strip()
        CruzamentoTotalVisitante = CruzamentoTotalVisitante.split("(")[0].strip()
        BolaLongaCertoMandante = BolaLongaCertoMandante.strip()
        BolaLongaTotalMandante = BolaLongaTotalMandante.split("(")[0].strip()
        BolaLongaCertoVisitante = BolaLongaCertoVisitante.strip()
        BolaLongaTotalVisitante = BolaLongaTotalVisitante.split("(")[0].strip()
        PassesPrecisos_Mandante = PassesPrecisos_Mandante.split("(")[0].strip()
        PassesPrecisos_Visitante = PassesPrecisos_Visitante.split("(")[0].strip()

        segundo_tempo_stats = {
            "ID_Partida": int(ID_Partida),
            "Periodo": "2ND",
            "Temporada": Temporada,
            "Posse_Mandante": int(segundo_tempo[0]['Mandante']),
            "Posse_Visitante": int(segundo_tempo[0]['Visitante']),
            "ChutesTotal_Mandante": int(segundo_tempo[1]['Mandante']),
            "ChutesTotal_Visitante": int(segundo_tempo[1]['Visitante']),
            "ChutesAlvo_Mandante": int(segundo_tempo[2]['Mandante']),
            "ChutesAlvo_Visitante": int(segundo_tempo[2]['Visitante']),
            "ChutesFora_Mandante": int(segundo_tempo[3]['Mandante']),
            "ChutesFora_Visitante": int(segundo_tempo[3]['Visitante']),
            "ChutesBloqueados_Mandante": int(segundo_tempo[4]['Mandante']),
            "ChutesBloqueados_Visitante": int(segundo_tempo[4]['Visitante']),
            "Escanteios_Mandante": int(segundo_tempo[5]['Mandante']),
            "Escanteios_Visitante": int(segundo_tempo[5]['Visitante']),
            "Impedimento_Mandante": int(segundo_tempo[6]['Mandante']),
            "Impedimento_Visitante": int(segundo_tempo[6]['Visitante']),
            "Amarelo_Mandante": int(segundo_tempo[7]['Mandante']),
            "Amarelo_Visitante": int(segundo_tempo[7]['Visitante']),
            "Vermelho_Mandante": int(segundo_tempo[8]['Mandante']),
            "Vermelho_Visitante": int(segundo_tempo[8]['Visitante']),
            "Faltas_Mandante": int(segundo_tempo[9]['Mandante']),
            "Faltas_Visitante": int(segundo_tempo[9]['Visitante']),
            "Lateral_Mandante": int(segundo_tempo[10]['Mandante']),
            "Lateral_Visitante": int(segundo_tempo[10]['Visitante']),
            "TiroMeta_Mandante": int(segundo_tempo[11]['Mandante']),
            "TiroMeta_Visitante": int(segundo_tempo[11]['Visitante']),
            "GrandesChances_Mandante": int(segundo_tempo[12]['Mandante']),
            "GrandesChances_Visitante": int(segundo_tempo[12]['Visitante']),
            "GrandesChancesPerdidas_Mandante": int(segundo_tempo[13]['Mandante']),
            "GrandesChancesPerdidas_Visitante": int(segundo_tempo[13]['Visitante']),
            "ContraAtaque_Mandante": int(segundo_tempo[15]['Mandante']),
            "ContraAtaque_Visitante": int(segundo_tempo[15]['Visitante']),
            "ChutesContraAtaque_Mandante": int(segundo_tempo[16]['Mandante']),
            "ChutesContraAtaque_Visitante": int(segundo_tempo[16]['Visitante']),
            "GolContraAtaque_Mandante": int(segundo_tempo[17]['Mandante']),
            "GolContraAtaque_Visitante": int(segundo_tempo[17]['Visitante']),
            "ChutesArea_Mandante": int(segundo_tempo[18]['Mandante']),
            "ChutesArea_Visitante": int(segundo_tempo[18]['Visitante']),
            "ChutesForaArea_Mandante": int(segundo_tempo[19]['Mandante']),
            "ChutesForaArea_Visitante": int(segundo_tempo[19]['Visitante']),
            "DefesasGoleiro_Mandante": int(segundo_tempo[20]['Mandante']),
            "DefesasGoleiro_Visitante": int(segundo_tempo[20]['Visitante']),
            "Passes_Mandante": int(segundo_tempo[21]['Mandante']),
            "Passes_Visitante": int(segundo_tempo[21]['Visitante']),
            "PassesPrecisos_Mandante": int(PassesPrecisos_Mandante),
            "PassesPrecisos_Visitante": int(PassesPrecisos_Visitante),
            "BolaLonga_Mandante": int(BolaLongaCertoMandante),
            "BolaLonga_Visitante": int(BolaLongaCertoVisitante),
            "BolaLongaTotal_Mandante": int(BolaLongaTotalMandante),
            "BolaLongaTotal_Visitante": int(BolaLongaTotalVisitante),
            "Cruzamento_Mandante": int(CruzamentoCertoMandante),
            "Cruzamento_Visitante": int(CruzamentoCertoVisitante),
            "CruzamentosTotal_Mandante": int(CruzamentoTotalMandante),
            "CruzamentosTotal_Visitante": int(CruzamentoTotalVisitante),
            "Dribles_Mandante": int(DribleCertoMandante),
            "Dribles_Visitante": int(DribleCertoVisitante),
            "DriblesTotal_Mandante": int(DribleTotalMandante),
            "DriblesTotal_Visitante": int(DribleTotalVisitante),
            "PerdaPosse_Mandante": int(segundo_tempo[26]['Mandante']),
            "PerdaPosse_Visitante": int(segundo_tempo[26]['Visitante']),
            "DuelosGanhos_Mandante": int(segundo_tempo[27]['Mandante']),
            "DuelosGanhos_Visitante": int(segundo_tempo[27]['Visitante']),
            "DueloAereoVencido_Mandante": int(segundo_tempo[28]['Mandante']),
            "DueloAereoVencido_Visitante": int(segundo_tempo[28]['Visitante']),
            "Desarmes_Mandante": int(segundo_tempo[29]['Mandante']),
            "Desarmes_Visitante": int(segundo_tempo[29]['Visitante']),
            "Interceptacoes_Mandante": int(segundo_tempo[30]['Mandante']),
            "Interceptacoes_Visitante": int(segundo_tempo[30]['Visitante']),
            "Cortes_Mandante": int(segundo_tempo[31]['Mandante']),
            "Cortes_Visitante": int(segundo_tempo[31]['Visitante'])
        }
        brasileiro_stat_insert(cursor, segundo_tempo_stats)
        con.commit()
        segundo_tempo.clear()
        print('inserido com sucesso')

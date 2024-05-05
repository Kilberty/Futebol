import requests
import oracledb
from dotenv import load_dotenv
from CorrigeDados import jogo_completo_dados,primeiro_tempo_dados,segundo_tempo_dados
import os
Temporada = 36166
jogo_completo = []
primeiro_tempo= []
segundo_tempo = []
CartaoVermelho = 0
CartaoAmarelo = 0
ContraAtaque = 0
ContraAtaqueGol = 0
ContraAtaqueChute = 0
GrandeChance = 0
GrandeChancePerdida = 0
Impedimento = 0
ChuteTrave = 0
DefesasGoleiro = 0
load_dotenv()
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
dsn = os.getenv("DSN")
walletpw = os.getenv("WALLET_PW")
wallet_location = r'.\Wallet'


try:
    con = oracledb.connect(user=usuario, password=senha, dsn=dsn, config_dir=wallet_location,  wallet_location=wallet_location, wallet_password=walletpw)
    print("Conexão bem-sucedida!")
    print("Database version:", con.version)
except oracledb.DatabaseError as e:
    error, = e.args
    print("Erro ao conectar ao banco de dados Oracle:", error.message)


cursor = con.cursor()
SQL = """ SELECT ID_PARTIDA from Partidas WHERE Temporada = :temporada"""

ID_Partidas =  cursor.execute(SQL,Temporada=Temporada)
ID_Partidas = cursor.fetchall()



for x in range(len(ID_Partidas)) :
 Partida = ID_Partidas[x][0]
 print(Partida)
 req = requests.get(f'https://api.sofascore.com/api/v1/event/{Partida}/statistics')
 dados = req.json()
 print(dados)
 primeiro_json = dados['statistics'][0]
 segundo_json = dados['statistics'][1]
 terceiro_json = dados['statistics'][2]
 groups_0 = primeiro_json['groups']
 groups_1 = segundo_json['groups']
 groups_2 = terceiro_json['groups']

 for group in groups_0:
    groupName = group['groupName']
    statisticsItems = group['statisticsItems']
    for stat in statisticsItems:
        name = stat['name']
        homeValue = stat['home'].rstrip('%')
        awayValue = stat['away'].rstrip('%')
        if name == "Goalkeeper saves" :
            DefesasGoleiro = 1
        else:
            pass
        if name == "Red cards":
            CartaoVermelho = 1
        else:
            pass
        if name == "Yellow cards":
            CartaoAmarelo = 1
        else:
            pass
        if name == "Counter attack goals":
            ContraAtaqueGol = 1
        else:
            pass
        if name == "Counter attacks":
            ContraAtaque = 1
        else:
            pass
        if name == "Counter attack shots":
            ContraAtaqueChute = 1
        if name == "Offsides":
           Impedimento = 1
        if name == "Big chances missed":
            GrandeChancePerdida = 1
        else:
            pass
        if name == "Big chances":
            GrandeChance = 1
        else:
            pass
        if name == "Hit woodwork":
            ChuteTrave = 1
        else:
            pass
        estatisticas = {
            'Estatistica': name,
            'Mandante': homeValue,
            'Visitante': awayValue,
            'Periodo': primeiro_json['period']
        }
        jogo_completo.append(estatisticas)

 for group in groups_1:
    groupName = group['groupName']
    statisticsItems = group['statisticsItems']
    for stat in statisticsItems:
        name = stat['name']
        homeValue = stat['home'].rstrip('%')
        awayValue = stat['away'].rstrip('%')
        if name == "Goalkeeper saves":
            DefesasGoleiro = 1
        else:
            pass
        if name == "Red cards":
            CartaoVermelho = 1
        else:
            pass
        if name == "Yellow cards":
            CartaoAmarelo = 1
        else:
            pass
        if name == "Counter attack goals":
            ContraAtaqueGol = 1
        else:
            pass
        if name == "Counter attacks":
            ContraAtaque = 1
        else:
            pass
        if name == "Counter attack shots":
            ContraAtaqueChute = 1
        if name == "Offsides":
            Impedimento = 1
        if name == "Big chances missed":
            GrandeChancePerdida = 1
        else:
            pass
        if name == "Big chances":
            GrandeChance = 1
        else:
            pass
        if name == "Hit woodwork":
            ChuteTrave = 1
        else:
            pass
        estatisticas = {
            'Estatistica': name,
            'Mandante': homeValue,
            'Visitante': awayValue,
            'Periodo': segundo_json['period']
        }
        primeiro_tempo.append(estatisticas)

 for group in groups_2:
    groupName = group['groupName']
    statisticsItems = group['statisticsItems']
    for stat in statisticsItems:
        name = stat['name']
        homeValue = stat['home'].rstrip('%')
        awayValue = stat['away'].rstrip('%')
        if name == "Goalkeeper saves":
            DefesasGoleiro = 1
        else:
            pass
        if name == "Red cards":
            CartaoVermelho = 1
        else:
            pass
        if name == "Yellow cards":
            CartaoAmarelo = 1
        else:
            pass
        if name == "Counter attack goals":
            ContraAtaqueGol = 1
        else:
            pass
        if name == "Counter attacks":
            ContraAtaque = 1
        else:
            pass
        if name == "Counter attack shots":
            ContraAtaqueChute = 1
        if name == "Offsides":
            Impedimento = 1
        else:
          pass
        if name == "Big chances missed":
            GrandeChancePerdida = 1
        else:
            pass
        if name == "Big chances":
            GrandeChance = 1
        else:
            pass
        if name == "Hit woodwork":
            ChuteTrave = 1
        else:
            pass
        estatisticas = {
            'Estatistica': name,
            'Mandante': homeValue,
            'Visitante': awayValue,
            'Periodo': terceiro_json['period']
        }
        segundo_tempo.append(estatisticas)
 print(Impedimento)
 if Impedimento == 0:
    valor = {
        'Estatistica': "Impedimento",
        'Mandante': 0,
        'Visitante': 0,
    }
    jogo_completo.insert(6, valor)
    primeiro_tempo.insert(5, valor)
    segundo_tempo.insert(5, valor)

 print(CartaoAmarelo)
 if CartaoAmarelo == 0:
    valor = {
        'Estatistica': "Cartao Amarelo",
        'Mandante': 0,
        'Visitante': 0,
    }
    jogo_completo.insert(8, valor)
    primeiro_tempo.insert(7,valor)
    segundo_tempo.insert(7,valor)
 print(CartaoVermelho)
 if CartaoVermelho == 0 :
   valor = {
            'Estatistica': "Cartao Vermelho",
            'Mandante': 0,
            'Visitante': 0,
     }

   jogo_completo.insert(9, valor)
   primeiro_tempo.insert(8,valor)
   segundo_tempo.insert(8,valor)
 print(GrandeChance)
 if GrandeChance == 0 :
     valor = {
         'Estatistica': "Grande Chance",
         'Mandante': 0,
         'Visitante': 0,
     }
     jogo_completo.insert(13, valor)
     primeiro_tempo.insert(12, valor)
     segundo_tempo.insert(12, valor)
 print(ChuteTrave)


 if GrandeChancePerdida == 0 :
     valor = {
         'Estatistica': "Grande Chance Perdida",
         'Mandante': 0,
         'Visitante': 0,
     }
     jogo_completo.insert(14, valor)
     primeiro_tempo.insert(13, valor)
     segundo_tempo.insert(13, valor)

 if ChuteTrave == 0:
    valor = {
        'Estatistica': "Trave",
        'Mandante': 0,
        'Visitante': 0,
    }
    jogo_completo.insert(15, valor)
    primeiro_tempo.insert(14, valor)
    segundo_tempo.insert(14, valor)

 print(ContraAtaque)
 if ContraAtaque == 0:
    valor = {
        'Estatistica': "Contra Ataque",
        'Mandante': 0,
        'Visitante': 0,
    }
    jogo_completo.insert(16, valor)
    primeiro_tempo.insert(15, valor)
    segundo_tempo.insert(15, valor)
 print(ContraAtaqueChute)
 if ContraAtaqueChute == 0:
    valor = {
        'Estatistica': "Contra Ataque Chutes",
        'Mandante': 0,
        'Visitante': 0,
    }
    jogo_completo.insert(17, valor)
    primeiro_tempo.insert(16, valor)
    segundo_tempo.insert(16, valor)
 print(ContraAtaqueGol)
 if ContraAtaqueGol == 0 :
     valor = {
         'Estatistica': "Gol Contra Ataque",
         'Mandante': 0,
         'Visitante': 0,
     }
     jogo_completo.insert(18, valor)
     primeiro_tempo.insert(17, valor)
     segundo_tempo.insert(17, valor)

 if DefesasGoleiro == 0 :
     valor = {
         'Estatistica': "Defesa Goleiro",
         'Mandante':0,
         'Visitante':0,
     }
     jogo_completo.insert(22, valor)
     primeiro_tempo.insert(21, valor)
     segundo_tempo.insert(21, valor)



 ContraAtaqueGol = 0
 ContraAtaqueChute = 0
 ContraAtaque = 0
 ChuteTrave = 0
 GrandeChance = 0
 GrandeChancePerdida = 0
 CartaoVermelho = 0
 CartaoAmarelo = 0
 Impedimento = 0
 DefesasGoleiro = 0

 jogo_completo_dados(jogo_completo,Partida,Temporada)
 primeiro_tempo_dados(primeiro_tempo,Partida,Temporada)
 segundo_tempo_dados(segundo_tempo,Partida,Temporada)


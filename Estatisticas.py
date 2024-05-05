import requests
import oracledb
from dotenv import load_dotenv
from CorrigeDados import jogo_completo_dados,primeiro_tempo_dados,segundo_tempo_dados
import os
Temporada = 48982
jogo_completo = []
primeiro_tempo= []
segundo_tempo = []
CartaoVermelho = 0
CartaoAmarelo = 0
ContraAtaque = 0
ContraAtaqueChute = 0
GrandeChance = 0
GrandeChancePerdida = 0
ChuteTrave = 0
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

Tamanho = len(ID_Partidas)

ID_Partidas = 12117009
req = requests.get(f'https://api.sofascore.com/api/v1/event/{ID_Partidas}/statistics')
dados = req.json()
primeiro_json = dados['statistics'][0]
segundo_json = dados['statistics'][1]
terceiro_json = dados['statistics'][2]
groups_0 = primeiro_json['groups']
groups_1 = segundo_json['groups']
groups_2 = terceiro_json['groups']

for group in groups_0:
    groupName = group['groupName']
    statisticsItems = group['statisticsItems']


    # Itera sobre os itens de estatísticas de cada grupo
    for stat in statisticsItems:
        name = stat['name']
        homeValue = stat['home'].rstrip('%')
        awayValue = stat['away'].rstrip('%')

        if name == "Red cards":
            CartaoVermelho = 1
        else:
            pass
        if name == "Yellow cards":
            CartaoAmarelo = 1
        else:
            pass
        if name == "Counter attack goals":
            ContraAtaque = 1
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


    # Itera sobre os itens de estatísticas de cada grupo
    for stat in statisticsItems:
        name = stat['name']
        homeValue = stat['home'].rstrip('%')
        awayValue = stat['away'].rstrip('%')

        if name == "Red cards":
           CartaoVermelho = 1
        else:
            pass
        if name == "Yellow cards":
            CartaoAmarelo = 1
        else:
            pass
        if name == "Counter attack goals":
            ContraAtaque = 1
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


    # Itera sobre os itens de estatísticas de cada grupo
    for stat in statisticsItems:
        name = stat['name']
        homeValue = stat['home'].rstrip('%')
        awayValue = stat['away'].rstrip('%')
        if name == "Red cards":
            CartaoVermelho = 1
        else:
            pass
        if name == "Yellow cards":
            CartaoAmarelo = 1
        else:
            pass
        if name == "Counter attack goals":
            ContraAtaque = 1
        else:
            pass
        estatisticas = {
            'Estatistica': name,
            'Mandante': homeValue,
            'Visitante': awayValue,
            'Periodo': terceiro_json['period']
        }
        segundo_tempo.append(estatisticas)

if CartaoVermelho == 0 :
   valor = {
            'Estatistica': "Cartao Vermelho",
            'Mandante': 0,
            'Visitante': 0,
     }
   jogo_completo.insert(10,valor)
   primeiro_tempo.insert(9,valor)
   segundo_tempo.insert(9,valor)
if CartaoAmarelo == 0:
    valor = {
        'Estatistica': "Cartao Amarelo",
        'Mandante': 0,
        'Visitante': 0,
    }
    jogo_completo.insert(9, valor)
    primeiro_tempo.insert(8,valor)
    segundo_tempo.insert(8,valor)
if ContraAtaque == 0 :
     valor = {
         'Estatistica': "Gol Contra Ataque",
         'Mandante': 0,
         'Visitante': 0,
     }
     jogo_completo.insert(18, valor)
     primeiro_tempo.insert(17, valor)
     segundo_tempo.insert(17, valor)

if ChuteTrave == 0:
    valor = {
        'Estatistica': "Trave",
        'Mandante': 0,
        'Visitante': 0,
    }
    jogo_completo.insert(15, valor)
    segundo_tempo.insert(15, valor)
    segundo_tempo.insert(15, valor)


jogo_completo_dados(jogo_completo,ID_Partidas)
"""primeiro_tempo_dados(primeiro_tempo,ID_Partidas)
segundo_tempo_dados(segundo_tempo,ID_Partidas)"""
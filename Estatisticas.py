import requests
import oracledb
from dotenv import load_dotenv
import os
Temporada = 48982
jogo_completo = []
primeiro_tempo = []
segundo_tempo = []
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

for x in range(Tamanho) :
 req = requests.get(f'https://api.sofascore.com/api/v1/event/{ID_Partidas[0][0]}/statistics')
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
        homeValue = stat['home']
        awayValue = stat['away']
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
        homeValue = stat['home']
        awayValue = stat['away']
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
        homeValue = stat['home']
        awayValue = stat['away']
        estatisticas = {
            'Estatistica': name,
            'Mandante': homeValue,
            'Visitante': awayValue,
            'Periodo': terceiro_json['period']
        }
        segundo_tempo.append(estatisticas)



print(jogo_completo)
print(primeiro_tempo)
print(segundo_tempo)





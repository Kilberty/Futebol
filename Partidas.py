import requests
import oracledb


temporada = 22931
rodadas = range(1,39)
campeonato = 325
Partidas = []



usuario = 'ADMIN'
senha = 'Kilberty32316943'
dsn = 'dadosfutebol_high'
walletpw = '32316943a'

# Especifique o diretório de configuração que contém os arquivos da wallet
wallet_location = r'.\Wallet'

try:
    con = oracledb.connect(user=usuario, password=senha, dsn=dsn, config_dir=wallet_location,  wallet_location=wallet_location, wallet_password=walletpw)
    print("Conexão bem-sucedida!")
    print("Database version:", con.version)
except oracledb.DatabaseError as e:
    error, = e.args
    print("Erro ao conectar ao banco de dados Oracle:", error.message)



for rodada in rodadas:

  req = requests.get(f"https://api.sofascore.com/api/v1/unique-tournament/{campeonato}/season/{temporada}/events/round/{rodada}")
  dados = req.json()
  eventos = dados['events']

  for evento in eventos:
    if 'roundInfo' in evento:
      # Obtendo informações sobre os times
        time_casa = evento['homeTeam']['name']
        time_visitante = evento['awayTeam']['name']
        id = evento['id']

        info = {
            'Casa': time_casa,
            'Fora': time_visitante,
            'ID': id,
            'Campeonato':campeonato,
            'Temporada': temporada,
            'Rodada': rodada
        }

        Partidas.append(info)


for Partida in Partidas :
    try :
        cursor = con.cursor()
        SQL =  """
        INSERT INTO Partidas(ID_Partida,Temporada,Campeonato,Mandante,Visitante,Rodada)
        VALUES (:idPartida, :Temporada, :Campeonato, :Mandante, :Visitante,:Rodada)
        """

        Mandante = Partida['Casa']
        Visitante = Partida['Fora']
        ID_Partida = Partida['ID']
        ID_Campeonato = Partida['Campeonato']
        Temporada = Partida['Temporada']
        Rodada = Partida['Rodada']
        cursor.execute(SQL,idPartida=ID_Partida,Temporada=Temporada,Campeonato=ID_Campeonato,Mandante=Mandante,Visitante=Visitante,Rodada=Rodada)
        con.commit()
    except oracledb.DatabaseError as e:
        print(e)


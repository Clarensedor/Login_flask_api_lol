from nis import match
import pandas as pd
from riotwatcher import LolWatcher



# golbal variables
api_key = 'RGAPI-9ef3d314-3054-4480-8d39-4669dcab6de8'
watcher = LolWatcher(api_key)
region = 'LA2'


def datos_invocador(invocador):
    invocador = watcher.summoner.by_name(region, invocador)
    print(invocador)

    return invocador

def datos_ranked(invocador):
    my_ranked_stats = watcher.league.by_summoner(region, invocador)
    return my_ranked_stats

def armar_datos_soloq(invocador):
    invocador =  datos_invocador(invocador)
    print(invocador['id'])
    my_ranked_stats = datos_ranked(invocador['id'])
    list_soloq = {'invocador': invocador['name'],
             'nivel': invocador['summonerLevel'],
             'liga': {'RANKED_SOLO_5x5': my_ranked_stats[0]['tier']},
             'puntos_de_liga': my_ranked_stats[0]['leaguePoints'],
             'victorias': my_ranked_stats[0]['wins'],
             'derrotas':  my_ranked_stats[0]['losses'],
    }
    return list_soloq

def armar_datos_flex(invocador):
    invocador = watcher.summoner.by_name(region, invocador)
    my_ranked_stats = watcher.league.by_summoner(region, invocador['id'])
    list_flex = {'invocador': invocador['name'],
                  'nivel': invocador['summonerLevel'],
                  'liga': {'RANKED_SOLO_5x5': my_ranked_stats[1]['tier']},
                  'puntos_de_liga': my_ranked_stats[1]['leaguePoints'],
                  'victorias': my_ranked_stats[1]['wins'],
                  'derrotas':  my_ranked_stats[1]['losses'],
                  }

    return list_flex


def indices_partidas(invocador):
    invocador    = datos_invocador(invocador)
    puuid        = invocador['puuid']
    match_detail = watcher.match.matchlist_by_puuid(
        region=region, puuid=puuid, queue=420, type="ranked", count=10)
    return match_detail


def datos_partida(id):
    datos = watcher.match.by_id(region, id)
    return datos



soloq  = armar_datos_soloq('tefo')
flex   = armar_datos_flex('tefo')
matchs = indices_partidas('tefo')

partidas = pd.DataFrame(matchs)
print(partidas)



participants = []
for row in datos['info']['participants']:
    participants_row = {}
    participants_row['Invocador'] = row['summonerName']
    participants_row['Campeon'] = row['championName']
    participants_row['Id_champ'] = row['championId']
    participants_row['LA Q'] = row['spell1Casts']
    participants_row['LA W'] = row['spell2Casts']
    participants_row['LA E'] = row['spell3Casts']
    participants_row['LA R'] = row['spell4Casts']
    participants_row['Gano el pete'] = row['win']
    participants_row['Asesinatos'] = row['kills']
    participants_row['Muertes'] = row['deaths']
    participants_row['Asistencias'] = row['assists']
    participants_row['Cuanto Pego'] = row['totalDamageDealt']
    participants_row['Orito'] = row['goldEarned']
    participants_row['nivel de champ'] = row['champLevel']
    participants.append(participants_row)
df = pd.DataFrame(participants)
print(df.value_counts)




exit()



print('datos del invocador')
print('------------------------------------------------')

me = watcher.summoner.by_name(region, 'Showmaker')
print(me)
print('------------------------------------------------')
print('datos del rangou')
print('------------------------------------------------')

str(my_ranked_stats)
print(my_ranked_stats)


print('El nombre es: ' + me['name'])
print('Tiene el nivel de invocador: ' + str(me['summonerLevel']))
print('En el modo de juego '+str(my_ranked_stats[0]['queueType']))
print('Tiene el elo de: ' + str(my_ranked_stats[0]['tier']))
print('HE HE HE HE')







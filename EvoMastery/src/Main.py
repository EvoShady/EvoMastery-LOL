from RiotAPI import RiotAPI
from SummonerProfile import SummonerProfile


def main():
    summoner_profile = SummonerProfile('EvoShady', 'euw1')
    riot_api = RiotAPI()
    riot_api.champion_mastery_v4_by_summoner(summoner_profile.summoner_name)

    champions_json = riot_api.get_champions_json()
    for champion in champions_json['data']:
        print(champions_json['data'][champion]['id'], champions_json['data'][champion]['key'])


if __name__ == '__main__':
    main()

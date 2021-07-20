from RiotAPI import RiotAPI
from SummonerProfile import SummonerProfile
import json


def main():
    summoner_profile = SummonerProfile('EvoShady', 'euw1')
    riot_api = RiotAPI()
    champions_mastery = riot_api.champion_mastery_v4_by_summoner(summoner_profile.summoner_name)
    for champion in champions_mastery:
        pass
        # print(champion['championId'], champion['championPoints'], champion['chestGranted'])
    with open("./misc/champions.json", "r") as f:
        champions_json = json.load(f)
    print(champions_json)


if __name__ == '__main__':
    main()

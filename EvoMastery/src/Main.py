from RiotAPI import RiotAPI
from SummonerProfile import SummonerProfile
from tkinter import *


def main():
    summoner_profile = SummonerProfile('EvoShady', 'euw1')
    riot_api = RiotAPI()
    riot_api.champion_mastery_v4_by_summoner(summoner_profile.summoner_name)

    champions_json = riot_api.get_champions_json()
    for champion in champions_json['data']:
        print(champions_json['data'][champion]['id'], champions_json['data'][champion]['key'])

    root = Tk()
    i = j = 0
    for champion in champions_json['data']:
        Label(root, text=champions_json['data'][champion]['id']).grid(row=i, column=j)
        j += 1
        if j == 9:
            j = 0
            i += 1

    root.mainloop()


if __name__ == '__main__':
    main()

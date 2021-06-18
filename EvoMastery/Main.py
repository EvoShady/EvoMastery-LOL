from RiotAPI import RiotAPI
from SummonerProfile import SummonerProfile


def main():
    summoner_profile = SummonerProfile('EvoShady', 'euw1')
    print(summoner_profile.get_summoner_encrypted_id_by_name())
    print()


if __name__ == '__main__':
    main()

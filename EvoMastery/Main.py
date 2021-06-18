from RiotAPI import RiotAPI


def main():
    api = RiotAPI()
    summoner_by_name_response = api.summoner_v4_by_name('EvoShady')
    summoner_encrypted_id = summoner_by_name_response['id']
    print(summoner_encrypted_id)


if __name__ == '__main__':
    main()

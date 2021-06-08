from RiotAPI import RiotAPI


def main():
    api = RiotAPI()
    r = api.test_func()
    print(r)


if __name__ == '__main__':
    main()

import analysis_twitter_handler

def test_1(bbdd):
    print(bbdd.get_auth_from_user_name("ronny_peroni"))


if __name__ == '__main__':
    bbdd_analysis = analysis_twitter_handler.BBDD_ANALYSIS()
    test_1(bbdd_analysis)
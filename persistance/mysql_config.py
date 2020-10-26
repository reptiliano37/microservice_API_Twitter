MYSQL_IP = 'localhost'
MYSQL_PORT = "3306"
MYSQL_USER = 'root'
MYSQL_PASSWORD = ""
MYSQL_DATABASE = 'analysis_twitter'

ANALYSYS_TYPE = {"table": "analysis_types"}
ANALYSYS_TYPE["fields"] = {
    'id': '{}.id'.format(ANALYSYS_TYPE['table']),
    'title': '{}.id'.format(ANALYSYS_TYPE['table']),
    'description': '{}.description'.format(ANALYSYS_TYPE['table'])
}

TWEET_PARAMETERS = {"table": "tweet_parameters"}
TWEET_PARAMETERS["fields"] = {
    'id': '{}.id'.format(TWEET_PARAMETERS['table']),
    'param': '{}.param'.format(TWEET_PARAMETERS['table']),
    'id_tweet_config': '{}.id_tweet_config'.format(TWEET_PARAMETERS['table'])
}

TWEETS_CONFIGURATION = {"table": "tweets_configuration"}
TWEETS_CONFIGURATION["fields"] = {
    'id': '{}.id'.format(TWEETS_CONFIGURATION['table']),
    'name': '{}.name'.format(TWEETS_CONFIGURATION['table']),
    'description': '{}.description'.format(TWEETS_CONFIGURATION['table']),
    'init_date': '{}.init_date'.format(TWEETS_CONFIGURATION['table']),
    'end_date': '{}.end_date'.format(TWEETS_CONFIGURATION['table']),
    'id_analysis_type': '{}.id_analysis_type'.format(TWEETS_CONFIGURATION['table']),
    'id_user': '{}.id_user'.format(TWEETS_CONFIGURATION['table'])
}

TWITTER_AUTH = {"table": "twitter_auth"}
TWITTER_AUTH["fields"] = {
    'id': '{}.id'.format(TWITTER_AUTH['table']),
    'consumer_key': '{}.consumer_key'.format(TWITTER_AUTH['table']),
    'consumer_secret': '{}.consumer_secret'.format(TWITTER_AUTH['table']),
    'access_token': '{}.access_token'.format(TWITTER_AUTH['table']),
    'access_token_secret': '{}.access_token_secret'.format(TWITTER_AUTH['table']),
    'id_user': '{}.id_user'.format(TWITTER_AUTH['table'])
}

USERS = {"table": "users"}
USERS["fields"] = {
    'id': '{}.id'.format(USERS['table']),
    'name': '{}.name'.format(USERS['table']),
    'id_twitter_auth': '{}.id_twitter_auth'.format(USERS['table'])
}

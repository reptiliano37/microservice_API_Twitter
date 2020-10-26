import pymysql
import mysql_config


class BBDD_ANALYSIS(object):

    def __init__(self):
        self.dbconnection = pymysql.connect(host=mysql_config.MYSQL_IP,
                                            user=mysql_config.MYSQL_USER,
                                            # password=mysql_config.MYSQL_PASSWORD,
                                            db=mysql_config.MYSQL_DATABASE,
                                            use_unicode=True,
                                            charset="utf8")
        self.cursor = self.dbconnection.cursor()

    def close_db(self):
        if self.cursor.connection:
            self.cursor.close()
            self.dbconnection.close()

    def commit_db(self):
        self.dbconnection.commit()

    def insert_tweet_parameters(self, param, id_tweet_config):
        """
            Metodo que realiza la insercion en la tabla tweet_parameters, en la cual se almacenan
            las busquedas que ha realizado el usuario.
            :param id_tweet_config:
            :param param: search(#, palabra o lista de palabras , @cuenta).
            """

        self.cursor.execute(
            'INSERT INTO {table} ({param},{id_tweet_config}) VALUES (%s,%s)'
            .format(
                    table=mysql_config.TWEET_PARAMETERS['table'],
                    param=mysql_config.TWEET_PARAMETERS['fields']['param'],
                    id_tweet_config=mysql_config.TWEET_PARAMETERS['fields']['id_tweet_config']),
            (param, id_tweet_config)
        )
        self.commit_db()

    def insert_tweets_configuration(self, description, init_date, end_date, id_analysis_type, id_user):
        """
            Metodo que realiza la insercion en la tabla tweets_configuration, en la cual se almacenan la
            descripcion de la busqueda que ha realizado el usuario.
            :param description: descripcion de la busqueda.
            :param init_date: fecha de inicio de la busqueda.
            :param end_date: fecha de fin de la busqueda.
            :param id_user: id del usuario de la busqueda.
            :param id_analysis_type: id de tipo de analisis.
        """
        self.cursor.execute(
            'INSERT INTO {table} ({description},{init_date},{end_date},'
            '{id_analysis_type},{id_user}) VALUES (%s,%s,%s,%s,%s)'
            .format(
                    table=mysql_config.TWEETS_CONFIGURATION['table'],
                    description=mysql_config.TWEETS_CONFIGURATION['fields']['description'],
                    init_date=mysql_config.TWEETS_CONFIGURATION['fields']['init_date'],
                    end_date=mysql_config.TWEETS_CONFIGURATION['fields']['end_date'],
                    id_analysis_type=mysql_config.TWEETS_CONFIGURATION['fields']['id_analysis_type'],
                    id_user=mysql_config.TWEETS_CONFIGURATION['fields']['id_user']),
            (description, init_date, end_date, id_analysis_type, id_user,)
        )
        self.commit_db()

    def get_id_analysis_type_from_search(self, search):

        self.cursor.execute("SELECT {id} FROM {table} WHERE {title} =%s".format(
            id=mysql_config.ANALYSYS_TYPE['fields']['id'],
            title=mysql_config.ANALYSYS_TYPE['fields']['title'],
            table=mysql_config.ANALYSYS_TYPE['table']),
            (search,)
        )
        return self.cursor.fetchone()

    def get_id_user(self, user_name):

        self.cursor.execute("SELECT {id} FROM {table} WHERE {name} = %s ".format(
                id=mysql_config.USERS['fields']['id'],
                name=mysql_config.USERS['fields']['name'],
                table=mysql_config.USERS['table']),
                (user_name,)
        )
        return self.cursor.fetchone()

    def get_id_tweet_config(self, id_user):
        """
        Metodo que devuelve el id del ultimo registro de la tabla tweets_configuration, que se relacionara con
        la busqueda/s que se hagan en ese momento, las cuales se insertaran en la tabla tweets_parameters
        :param id_user: id del usuario que realiza la busqueda.
        :return:
        """
        self.cursor.execute(" SELECT {id} FROM {table} WHERE {id_user} = %s ORDER BY {id} DESC LIMIT 1".format(
            id=mysql_config.TWEETS_CONFIGURATION['fields']['id'],
            id_user=mysql_config.TWEETS_CONFIGURATION['fields']['id_user'],
            table=mysql_config.TWEETS_CONFIGURATION['table']),
            (id_user,)
        )
        return self.cursor.fetchone()


    def get_auth_from_user_name(self, name):
            self.cursor.execute(
                "SELECT {consumer_key}, "
                "{consumer_secret}, " 
                "{access_token}, "
                "{access_token_secret} "
                "FROM {twitter_auth_table} "
                "INNER JOIN {users_table} "
                "ON {id} = {id_twitter_auth} " 
                "WHERE {name} = %s".format(
                    consumer_key=mysql_config.TWITTER_AUTH['fields']['consumer_key'],
                    consumer_secret=mysql_config.TWITTER_AUTH['fields']['consumer_secret'],
                    access_token=mysql_config.TWITTER_AUTH['fields']['access_token'],
                    access_token_secret=mysql_config.TWITTER_AUTH['fields']['access_token_secret'],
                    twitter_auth_table=mysql_config.TWITTER_AUTH['table'],
                    users_table=mysql_config.USERS['table'],
                    id=mysql_config.TWITTER_AUTH['fields']['id'],
                    id_twitter_auth=mysql_config.USERS['fields']['id_twitter_auth'],
                    name=mysql_config.USERS['fields']['name']),
                (name,)
            )
            row = self.cursor.fetchone()
            field_names = [i[0] for i in self.cursor.description]
            result = {}
            for index, field in enumerate(field_names):
                result[field] = row[index]

            return result if result else None


   #################################### TABLAS PARA NUEVOS USUARIOS  ##########################################


    def insert_twitter_auth(self, description, consumer_key, consumer_secret, access_token, access_token_secret,):
        self.cursor.execute(
            'INSERT INTO {table} ({consumer_key},{consumer_secret},{access_token},{access_token_secret}) '
            'VALUES (%s,%s,%s,%s)'
            .format(
                    table=mysql_config.TWITTER_AUTH['table'],
                    consumer_key=mysql_config.TWITTER_AUTH['fields']['consumer_key'],
                    consumer_secret=mysql_config.TWITTER_AUTH['fields']['consumer_secret'],
                    access_token=mysql_config.TWITTER_AUTH['fields']['access_token'],
                    access_token_secret=mysql_config.TWITTER_AUTH['fields']['access_token_secret']
                    (description, consumer_key, consumer_secret, access_token, access_token_secret,))
        )

    def insert_users(self, name):
        self.cursor.execute(
            'INSERT INTO {table} ({name}) VALUES (%s)'
            .format(
                    table=mysql_config.USERS['table'],
                    name=mysql_config.USERS['fields']['name']
                    (name,))
        )
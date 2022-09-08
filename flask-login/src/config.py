class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'
##datos de la base
class DevelopmentConfig(Config):
      DEBUG = True
      MYSQL_HOST = 'sql10.freesqldatabase.com'
      MYSQL_USER = 'sql10502724'
      MYSQL_PASSWORD = '57CfF9YKKE'
      MYSQL_DB = 'sql10502724'

config = {
   'development': DevelopmentConfig

}

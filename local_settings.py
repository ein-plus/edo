import yaml

secrets = yaml.load(open('secrets.yaml'))

SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}'.format(**secrets['mysql'])

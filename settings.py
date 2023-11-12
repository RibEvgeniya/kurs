from envparse import Env

env = Env()

DATABASE_URL = env.str(
    "DATABASE_URL",
    default='postgresql+asyncpg://postgres:wokawoka23@localhost:5432/med_data',
)


##%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s
##postgres:wokawoka23@localhost:5432/med_data
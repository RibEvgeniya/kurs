from envparse import Env

env = Env()

DATABASE_URL = env.str(
    "DATABASE_URL",
    default='postgresql+asyncpg://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:5432/%(DB_NAME)s',
)


##%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s
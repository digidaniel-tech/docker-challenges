import providers.postgres as postgres

from sqlalchemy.orm import sessionmaker

def setup():
  engine = postgres.setup()
  session = sessionmaker()
  session.configure(bind=engine, expire_on_commit=False)
  return session()

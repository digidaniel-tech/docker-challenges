import models.base as base

from sqlalchemy import create_engine

def setup():
  # TODO: is pg8000 best module?
  engine = create_engine("postgresql+pg8000://user:myrandompassword123@db/usermanager", client_encoding='utf8')
  base.Base.metadata.create_all(engine)
  return engine

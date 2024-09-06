import models.userModel as userModel
import providers.sessionProvider as sessionProvider

def add(user):
  session = sessionProvider.setup()
  session.add(user)
  session.commit()
  session.close()
  
  return user

def all():
  session = sessionProvider.setup()
  users = session.query(userModel.User).all()
  session.close()

  return users

import models.userModel as userModel
import services.userService as userService

def addUser(user):
  userService.add(user)

  return user

def getAllUsers():
  users = userService.all()  
  return users

import json


def get_stored_username():
  """ 如果以前存储了用户名就加载它。 """
  filename = './test_files/username.json'
  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    return None
  else:
    return username
  

def get_new_username():
  """ 提示用户输入用户名。"""
  username = input("What is your namej?")
  filename = './test_files/username.json'
  with open(filename, 'w') as f:
      json.dump(username, f)
  return username

def greet_user():
  """ 否则，提示用户输入用户名并存储它。"""
  username = get_stored_username()
  if username:
    print(f"Welcome back, {username}")
  else:
    username = get_new_username()
    print(f"We`ll remember you when you come back, {username}!")

greet_user()

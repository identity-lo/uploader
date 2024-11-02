from models import User

a = [x.username for x in User.select()]
res = User.get_or_none(User.username == "amirali")

print(res)




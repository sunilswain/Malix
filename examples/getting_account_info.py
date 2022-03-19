import malix

client = malix.Client(address='example@domain.com', password='passowrd')
id = client.id
token = client.token

info = client.get_account(Id=id)
print(info.json)

import malix


client = malix.Client(address='example@domain.com', password='passowrd')

messages = client.get_message_collection()

info = client.get_message(Id='yourMessageId')  # returns a Message object if successful.

print(info.json)
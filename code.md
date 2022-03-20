Getting messages 

    messages = client.get_message_collection()
    
Get information for a specific message

    info = client.get_message(Id='MessageId')

    print(info.json)
  


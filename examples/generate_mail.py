import malix


domain = malix.get_domain_collection(domains_only=1)[0]
mail = malix.make_account(address='example@'+domain, password='passowrd')
# returns an Account object if successful.

print(mail.id)

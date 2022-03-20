get json response
  from malix import get_domain_collection
  response = get_domain_collection()
this would choose the ther first from the available domain
  domain = response["hydra:member"][0]["domain"]

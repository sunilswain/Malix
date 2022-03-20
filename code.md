Get json response

    from malix import get_domain_collection
    response = get_domain_collection()
  
Choosing domain(0 represents the frist domain)

    domain = response["hydra:member"][0]["domain"]


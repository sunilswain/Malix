Create an account(returns an account object if successful) 

    from malix import make_account
    mail = make_account(address='example@'+domain, password='y0urp4ss0wrd')
 
Prints emailId
    
    print(mail.id)


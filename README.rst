API Client from Deribit API version 2
===========================

API client for 'Deribit API version 2. 


example:

    import RestClient
    client = RestClient("KEY", "SECRET")
    client.index()
    client.getorderbook('BTC-PERPETUAL',10)     
    client.getinstruments('BTC','future')       
    client.getcurrencies()                      
    client.gettradesbycurrency('BTC',10)         
    client.getindex('BTC')                       


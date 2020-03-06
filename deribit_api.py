
import time, hashlib, requests, base64, sys, hmac
from collections import OrderedDict
import datetime

class RestClient(object):
    def __init__(self, key=None, secret=None, url=None):
        """
        constructors 

        input:
            key:string [from deribit]
            secret: string [from deribit]
            url: string [default: https://www.deribit.com]

        """
        self.key = key
        self.secret = secret
        self.session = requests.Session()

        if url:
            self.url = url
        else:
            self.url = "https://www.deribit.com"

    def request(self, action, data):
        """
        input:
            action:string [eg: /api/v2/xxxx]
            data: string [parameters of url]
        """
        response = None
        if action.startswith("/api/v2/private/"):           #if private need AUTH
            if self.key is None or self.secret is None:
                raise Exception("Key or secret empty")
        
            tstamp = int(time.time()* 1000)
            nonce = str(datetime.datetime.now())
            
            def converter(data):
                key = data[0]
                value = data[1]
                if isinstance(value, list):
                    return '='.join([str(key), ''.join(value)])
                else:
                    return '='.join([str(key), str(value)])

            items = map(converter, data.items())
            signature_string = '&'.join(items)
            if len(signature_string)>0:
                signature_string ='?'+signature_string;

            sig=self.generatesignature(action+signature_string,tstamp,nonce);   
            
            Authorization="deri-hmac-sha256 id=%s,ts=%s,sig=%s,nonce=%s" %(self.key,tstamp,sig,nonce);
            response = self.session.get(self.url + action, params=data, headers={'Authorization': Authorization}, verify=True)
        else:                                               #if public , no need AUTH
            response = self.session.get(self.url + action, params=data, verify=True)
        
        if response.status_code != 200:
            raise Exception("Wrong response code: {0}".format(response.status_code))

        json = response.json()

        if "error" in json:
            raise Exception("Failed: " + json["error"])

        if "result" in json:
            return json["result"]
        elif "message" in json:
            return json["message"]
        else:
            return "Ok"

    def generatesignature(self,url,tstamp,nonce):
        """
        To generate signature

        input:
            url: string [eg: [eg: /api/v2/private/xxxx]
            tstamp: int 
            nonce: string [any string for encryption]
        return:
            string [signature]
            
        """
        RequestData = 'GET' + "\n" + url + "\n" + "" + "\n";
        StringToSign = str(tstamp) + "\n" + nonce + "\n" + RequestData;

        signature = hmac.new(
            bytes(self.secret, "latin-1"),
            msg=bytes(StringToSign, "latin-1"),
            digestmod=hashlib.sha256
        ).hexdigest().lower()
        return signature;


    def getorderbook(self, instrument,depth=5):
        """
        to get order books 

        input:
            instrument: string [name of instrument eg: 'BTC-PERPETUAL' or 'ETH-PERPETUAL']
            depth: int 
        """
        return self.request("/api/v2/public/get_order_book", {'instrument_name': instrument,'depth':depth})


    def getcurrencies(self):
        '''
        to get the symbols support within this exchange platform

        output: list eg:[BTC, ETH]
        '''
        results=self.request("/api/v2/public/getcurrencies", {});
        currencies=[];
        for r in results:
            currencies.append(r['currency']);

        return currencies;


    def gettradesbycurrency(self, currency, count=10, sorting='default'):
        '''
        to retrieve the latest trades that have occurred for instruments
        input:
            currency: string [eg: 'BTC' /'ETH'
            count: int [how many trades you want to get]
            sorting: string [either 'default','desc','asc']
        '''
        assert sorting in ['default','desc','asc']

        options = {
            'currency': currency,
            'count':count,
            'sorting': sorting
        }

        return self.request("/api/v2/private/get_user_trades_by_currency", options)


    def getindex(self,currency):
        '''
        to get index of currency

        input:
            currency:string [eg: 'BTC' or 'ETH']
        '''

        response =self.request("/api/v2/public/get_index", {'currency':currency});
        return response[currency]

    def getinstruments(self,currency,kind='future'):
        '''
        to get available trading instruments

        input:
            currency: string ['BTC', 'ETH']
            kind:string [eg: 'future' or 'option']
        '''
        assert kind in ['future','option']
        
        options = {
            'currency': currency,
            'kind':kind
        }

        return self.request("/api/v2/public/get_instruments", options)

    def buy(self, instrument, amount, price, type='limit'):
        '''
        to place order to buy

        input:
            instrument:string  ['BTC-PERPETUAL' or 'ETH-PERPETUAL']
            amount: float [USD unit]
            price: float [price to buy]
            type: string ['limit' or 'market']
        '''
        assert amount>0
        assert price>0
        
        if instrument=='BTC-PERPETUAL':
            amount=int(round(amount,-1));     #BTC-PERPETUAL only allow amount with muliple of 10
        
        if instrument=='ETH-PERPETUAL':
            amount=int(round(amount));       #ETH-PERPETUAL only allow amount with muliple of 10

        options = {
            "instrument_name": instrument,  
            "amount": amount,     
            "type": type,         
            "price":price         
        }

        return self.request("/api/v2/private/buy", options)


    def sell(self, instrument, amount, price, type='limit'):
        '''
        to place order to sell

        input:
            instrument:string  ['BTC-PERPETUAL' or 'ETH-PERPETUAL']
            amount: float [USD unit]
            price: float [price to buy]
            type: string ['limit' or 'market']
        '''
        assert amount>0
        assert price>0

        options = {
            "instrument_name": instrument,  
            "amount": amount,    
            "type": type,         
            "price":price         
        }

        return self.request("/api/v2/private/sell", options)

    def edit(self, orderId, amount, price):
        '''
        to edit amount or price of a pending order

        input:
            orderId: string  [id of order]
            amount: float 
            price: float [price to buy]
        '''

        assert amount>0;
        assert price>0;

        options = {
            "order_id": orderId,
            "amount": amount,
            "price": price
        }

        return self.request("/api/v2/private/edit", options)


    def cancel(self, orderId):
        '''
        to cancel an order

        input:
            orderId:int  
        '''
        options = {
            "order_id": orderId
        }  

        return self.request("/api/v2/private/cancel", options)

    def cancelall(self):
        '''
        to cancel all pendings orders
        '''
        return self.request("/api/v2/private/cancel_all", {})


    def getopenorders(self, currency='BTC'):
        '''
        to retrieve pending orders [order not yet settled]

        input:
            currency: string in 'BTC' or 'ETH'
        output:
            [ID1, ID2...]
        '''
        options = {
            "currency":currency
            }

        response=self.request("/api/v2/private/get_open_orders_by_currency", options);

        orders=[];
        for record in response:
            orders.append(record['order_id'])

        return orders;


    def getpositions(self,currency='BTC'):
        '''
        to retrieve position by currency

        input:
            currency: string in 'BTC' or 'ETH'
        return: 
            int [size of position. positive for 'buy' and negative for 'sell'
            
        '''

        options = {
            "currency":currency
            }
        response=self.request("/api/v2/private/get_positions", options);

        if len(response)>0:
            return response[0]['size']
        else:
            return 0;


if __name__ == '__main__':

    pass;

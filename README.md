# API Client for Deribit python REST [version 2](https://docs.deribit.com/v2/)
### Example

```
import RestClient
client = RestClient("KEY", "SECRET")
client.index()
client.getorderbook('BTC-PERPETUAL',10)
client.getinstruments('BTC','future')
client.getcurrencies()
client.gettradesbycurrency('BTC',10)
client.getindex('BTC')
```

## API - REST Client

`RestClient(key, secret, url)`

Constructor creates new REST client.

**Parameters**

| Name     | Type     | Decription                                                |
|----------|----------|-----------------------------------------------------------|
| `key`    | `string` | Optional, Access Key needed to access Private functions   |
| `secret` | `string` | Optional, Access Secret needed to access Private functions|
| `url`    | `string` | Optional, server URL, default: `https://www.deribit.com`  |


### Methods
                                                             |

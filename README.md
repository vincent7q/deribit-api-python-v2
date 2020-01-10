# API Client for [Deribit API version 2](https://docs.deribit.com/v2/)
### Example

```
from deribit_api import RestClient
client = RestClient("KEY", "SECRET")
client.index()
client.account()
```

## API - REST Client

`new RestClient(key, secret, url)`

Constructor creates new REST client.

**Parameters**

| Name     | Type     | Decription                                                |
|----------|----------|-----------------------------------------------------------|
| `key`    | `string` | Optional, Access Key needed to access Private functions   |
| `secret` | `string` | Optional, Access Secret needed to access Private functions|
| `url`    | `string` | Optional, server URL, default: `https://www.deribit.com`  |


### Methods

* `getorderbook(instrument)` - [Doc](https://www.deribit.com/docs/api/#getinstruments), public

  Retrieve the orderbook for a given instrument.

  **Parameters**

  | Name         | Type       | Decription                                                 |
  |--------------|------------|------------------------------------------------------------|
  | `instrument` | `string`   | Required, instrument name                                  |

* `index()` - [Doc](https://www.deribit.com/docs/api/#index), public

  Get price index, BTC-USD rates.

* `getcurrencies()` - [Doc](https://www.deribit.com/docs/api/#getcurrencies), public

  Get all supported currencies.

* `getorderbook(instrument)` - [Doc](https://www.deribit.com/docs/api/#getorderbook), public

  Retrieve the orderbook for a given instrument.

  **Parameters**

  | Name         | Type       | Decription                                                 |
  |--------------|------------|------------------------------------------------------------|
  | `instrument` | `string`   | Required, instrument name                                  |

* `getlasttrades(instrument, count, since)` - [Doc](https://www.deribit.com/docs/api/#getlasttrades), public

  Retrieve the latest trades that have occured for a specific instrument.

  **Parameters**

  | Name         | Type       | Decription                                                                    |
  |--------------|------------|-------------------------------------------------------------------------------|
  | `instrument` | `string`   | Required, instrument name                                                     |
  | `count`      | `integer`  | Optional, count of trades returned (limitation: max. count is 100)            |
  | `since`      | `integer`  | Optional, “since” trade id, the server returns trades newer than that “since” |

* `getsummary(instrument)` - [Doc](https://www.deribit.com/docs/api/#getsummary), public

  Retrieve the summary info such as Open Interest, 24H Volume etc for a specific instrument.

  **Parameters**

  | Name         | Type       | Decription                                                 |
  |--------------|------------|------------------------------------------------------------|
  | `instrument` | `string`   | Required, instrument name                                  |

* `account()` - [Doc](https://www.deribit.com/docs/api/#account), Private

  Get user account summary.

* `buy(instrument, quantity, price, postOnly, label)` - [Doc](https://www.deribit.com/docs/api/#buy), private

  Place a buy order in an instrument.

  **Parameters**

  | Name         | Type       | Decription                                                                        |
  |--------------|------------|-----------------------------------------------------------------------------------|
  | `instrument` | `string`   | Required, instrument name                                                         |
  | `quantity`   | `integer`  | Required, quantity, in contracts ($10 per contract for futures, ฿1 — for options) |
  | `price`      | `float`    | Required, USD for futures, BTC for options                                        |
  | `postOnly`   | `boolean`  | Optional, if true then the order will be POST ONLY                                |
  | `label`      | `string`   | Optional, user defined maximum 4-char label for the order                         |

* `sell(instrument, quantity, price, postOnly, label)` - [Doc](https://www.deribit.com/docs/api/#sell), private

  Place a sell order in an instrument.

  **Parameters**

  | Name         | Type       | Decription                                                                        |
  |--------------|------------|-----------------------------------------------------------------------------------|
  | `instrument` | `string`   | Required, instrument name                                                         |
  | `quantity`   | `integer`  | Required, quantity, in contracts ($10 per contract for futures, ฿1 — for options) |
  | `price`      | `float`    | Required, USD for futures, BTC for options                                        |
  | `postOnly`   | `boolean`  | Optional, if true then the order will be POST ONLY                                |
  | `label`      | `string`   | Optional, user defined maximum 4-char label for the order                         |

* `edit(orderId, quantity, price)` - [Doc](https://www.deribit.com/docs/api/#edit)

  Edit price and/or quantity of the own order. (Authorization is required).

  **Parameters**

  | Name         | Type       | Decription                                                                        |
  |--------------|------------|-----------------------------------------------------------------------------------|
  | `orderId`    | `integer`  | Required, ID of the order returned by "sell" or "buy" request                     |
  | `quantity`   | `integer`  | Required, quantity, in contracts ($10 per contract for futures, ฿1 — for options) |
  | `price`      | `float`    | Required, USD for futures, BTC for options                                        |

* `cancel(orderId)` - [Doc](https://www.deribit.com/docs/api/#cancel), private

  Cancell own order by id.

  **Parameters**

  | Name         | Type       | Decription                                                                        |
  |--------------|------------|-----------------------------------------------------------------------------------|
  | `orderId`    | `integer`  | Required, ID of the order returned by "sell" or "buy" request                     |

* `cancelall(type)` - [Doc](https://www.deribit.com/docs/api/#cancelall)

  Cancel all own futures, or all options, or all.

  **Parameters**

  | Name         | Type       | Decription                                                                                    |
  |--------------|------------|-----------------------------------------------------------------------------------------------|
  | `type`       | `string`   | Optional, type of instruments to cancel, allowed: "all", "futures", "options", default: "all" |

* `getopenorders(instrument, orderId)` - [Doc](https://www.deribit.com/docs/api/#getopenorders), private

  Retrieve open orders.

  **Parameters**

  | Name         | Type       | Description                                                           |
  |--------------|------------|-----------------------------------------------------------------------|
  | `instrument` | `string`   | Optional, instrument name, use if want orders for specific instrument |
  | `orderId`    | `integer`  | Optional, order id                                                    |

* `positions()` - [Doc](https://www.deribit.com/docs/api/#positions), private

  Retreive positions.

* `orderhistory(count)` - [Doc](https://www.deribit.com/docs/api/#orderhistory), private

  Get history.

  **Parameters**

  | Name       | Type       | Description                                                |
  |------------|------------|------------------------------------------------------------|
  | `count`    | `integer`  | Optional, number of requested records                      |

* `tradehistory(count, instrument, startTradeId)` - [Doc](https://www.deribit.com/docs/api/#tradehistory), private

  Get private trade history of the account. (Authorization is required). The result is ordered by trade identifiers (trade id-s).

  **Parameters**

  | Name           | Type       | Description                                                                                        |
  |----------------|------------|----------------------------------------------------------------------------------------------------|
  | `count`        | `integer`  | Optional, number of results to fetch. Default: 20                                                  |
  | `instrument`   | `string`   | Optional, name of instrument, also aliases “all”, “futures”, “options” are allowed. Default: "all" |
  | `startTradeId` | `integer`  | Optional, number of requested records                                                              |

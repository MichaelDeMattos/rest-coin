# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: michael.ortiz <michael.ortiz@dotpyc.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/11 23:55:16 by michael.ort       #+#    #+#              #
#    Updated: 2022/11/12 11:06:40 by michael.ort      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import json
from flask import Flask
from libs.config import conf
from flask_restful import Api

# APP
app = Flask(__name__)

# CONFIG
app.secret_key = conf.get("app").get("secret_key")

# Rest API
api = Api(app)

from resources.controller_coin import CoinFetchOneForexAPI
from resources.controller_coin import CoinFetchMultiForexAPI
from resources.controller_coin import CoinFetchAllForexAPI
from resources.controller_coin import CoinConvertForexAPI
from resources.controller_coin import CoinHistoricalForexAPI
from resources.controller_coin import CoinTimeSeriesForexAPI
from resources.controller_coin import CoinCurrenciesForexAPI
from resources.controller_coin import CoinCryptoCurrenciesForexAPI
from resources.controller_coin import CoinCryptoPairsForexAPI
from resources.controller_coin import CoinCryptoFetchPricesForexAPI
from resources.controller_coin import CoinUsageForexAPI

api.add_resource(CoinFetchOneForexAPI, "/", "/fetch-one")
api.add_resource(CoinFetchMultiForexAPI, "/", "/fetch-multi")
api.add_resource(CoinFetchAllForexAPI, "/", "/fetch-all")
api.add_resource(CoinConvertForexAPI, "/", "/convert")
api.add_resource(CoinHistoricalForexAPI, "/", "/historical")
api.add_resource(CoinTimeSeriesForexAPI, "/", "/time-series")
api.add_resource(CoinCurrenciesForexAPI, "/", "/currencies")
api.add_resource(CoinCryptoCurrenciesForexAPI, "/", "/crypto/currencies")
api.add_resource(CoinCryptoPairsForexAPI, "/", "/crypto/pairs")
api.add_resource(CoinCryptoFetchPricesForexAPI, "/", "/crypto/fetch-prices")
api.add_resource(CoinUsageForexAPI, "/", "/usage")

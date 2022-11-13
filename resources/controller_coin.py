# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    controller_coin.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: michael.ortiz <michael.ortiz@dotpyc.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/12 00:14:07 by michael.ort       #+#    #+#              #
#    Updated: 2022/11/13 14:58:58 by michael.ort      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
import requests
import traceback
from libs.config import conf
from flask_restful import Resource
from libs.database import redis_client
from utils.soup_proxy import SoupProxy
from flask import request, make_response, jsonify


class CoinFetchOneForexAPI(Resource):
    def __init__(self, *args):
        self.list_proxy = None

    def get(self) -> make_response:
        try:
            self.list_proxy = sorted(SoupProxy().get_proxy_list())
            coin_from = request.args.get("coin_from")
            coin_to = request.args.get("coin_to")

            if not coin_from or not coin_to:
                return make_response(jsonify({"response": "Params [coin_from, coin_to] is required!"}), 403)

            if redis_client.get(f"coin_from={coin_from}&coin_to={coin_to}"):
                return make_response(
                    jsonify({"response": json.loads(redis_client.get("coin_from=USD&coin_to=BRL"))}), 200)

            req_ok = False
            count_try = 0
            result = None

            while req_ok == False:
                try:
                    if count_try == 100:
                        break

                    req = requests.get(
                        f"https://api.fastforex.io/fetch-one?from={coin_from}&to={coin_to}&api_key={conf.get('fastforex').get('api_key')}",
                        proxies={f"{self.list_proxy[count_try].split('://')[0]}": f"{self.list_proxy[count_try].split('://')[1]}"},
                        timeout=1)

                    if req.ok:
                        req_ok = True
                        result = req.json()
                        redis_client.set(f"coin_from={coin_from}&coin_to={coin_to}", json.dumps(result), ex=60)
                        break

                    count_try += 1

                except Exception as error:
                    count_try += 1
                    traceback.print_exc()
                    continue

            return make_response(jsonify({"response": result}), 200)

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinFetchMultiForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinFetchAllForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinConvertForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinHistoricalForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinTimeSeriesForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinCurrenciesForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinCryptoCurrenciesForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinCryptoPairsForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinCryptoFetchPricesForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)


class CoinUsageForexAPI(Resource):
    def __init__(self, *args):
        pass

    def get(self) -> make_response:
        try:
            coin_from = request.args.get("from")
            coint_to = request.args.get("to")
            return make_response()

        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def post(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def put(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

    def delete(self) -> make_response:
        try:
            raise Exception("Your request method is invalid or not implemented!")
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"error": str(error)}), 503)

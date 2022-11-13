# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_fetch_multi.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: michael.ortiz <michael.ortiz@dotpyc.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/13 15:09:00 by michael.ort       #+#    #+#              #
#    Updated: 2022/11/13 16:11:17 by michael.ort      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import json
import os.path
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


def test_fetch_nulti_request():
    """ Consumer Rest API /fech-multi with Method [GET, POST, PUT, DELETE] """

    req = requests.get(
        "http://localhost:5000/fetch-multi",
        params={"coin_from": "USD", "coin_to": "BRL,EUR,GBP"},
        timeout=60)

    assert req.status_code == 200
    resp = req.json()
    assert type(resp) == dict
    assert resp.get("response").get("base") == "USD"
    assert type(resp.get("response").get("results").get("BRL")) == float
    assert type(resp.get("response").get("results").get("EUR")) == float
    assert type(resp.get("response").get("results").get("GBP")) == float

    req = requests.post(
        "http://localhost:5000/fetch-multi",
        params={"coin_from": "USD", "coin_to": "BRL,EUR"},
        timeout=60)
    assert req.status_code == 503

    req = requests.put(
        "http://localhost:5000/fetch-multi",
        params={"coin_from": "USD", "coin_to": "BRL,EUR"},
        timeout=60)
    assert req.status_code == 503

    req = requests.delete(
        "http://localhost:5000/fetch-multi",
        params={"coin_from": "USD", "coin_to": "BRL,EUR"},
        timeout=60)
    assert req.status_code == 503

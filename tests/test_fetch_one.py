# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_fetch_one.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: michael.ortiz <michael.ortiz@dotpyc.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/13 15:09:00 by michael.ort       #+#    #+#              #
#    Updated: 2022/11/13 15:34:44 by michael.ort      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import json
import os.path
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


def test_fetch_one_request():
    """ Consumer Rest API /fech-one with Method [GET, POST, PUT, DELETE] """

    req = requests.get(
        "http://localhost:5000/fetch-one",
        params={"coin_from": "USD", "coin_to": "BRL"},
        timeout=60)

    assert req.status_code == 200
    resp = req.json()
    assert type(resp) == dict
    assert resp.get("response").get("base") == "USD"
    assert type(resp.get("response").get("result").get("BRL")) == float

    req = requests.post(
        "http://localhost:5000/fetch-one",
        params={"coin_from": "USD", "coin_to": "BRL"},
        timeout=60)
    assert req.status_code == 503

    req = requests.put(
        "http://localhost:5000/fetch-one",
        params={"coin_from": "USD", "coin_to": "BRL"},
        timeout=60)
    assert req.status_code == 503

    req = requests.delete(
        "http://localhost:5000/fetch-one",
        params={"coin_from": "USD", "coin_to": "BRL"},
        timeout=60)
    assert req.status_code == 503

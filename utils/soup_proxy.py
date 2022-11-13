# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    soup_proxy.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: michael.ortiz <michael.ortiz@dotpyc.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/12 11:21:04 by michael.ort       #+#    #+#              #
#    Updated: 2022/11/12 12:30:25 by michael.ort      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import traceback
from bs4 import BeautifulSoup
from flask_restful import Resource
from libs.database import redis_client
from flask import request, make_response, jsonify


class SoupProxy(object):
    def __init__(self, *args):
        self.url = "https://sslproxies.org/"
        self.list_proxie = []


    def get_proxy_list(self) -> list:
        try:
            proxie_list = self.format_layout(country="all")
            if type(proxie_list) == dict:
                raise Exception(soup.get("response"))
            elif len(proxie_list) == 0:
                raise Exception("Servers not found!")
            else:
                return proxie_list

        except Exception as error:
            return {"status": 503, "response": str(error)}


    def get_page_html(self) -> BeautifulSoup:
        """ This function return page html for scrape """
        try:

            req = requests.get(self.url)
            if req.status_code == 200:
                soup = BeautifulSoup(req.text, 'html.parser')
                return {"status": 200, "soup": soup}
            else:
                raise Exception(req.text)

        except Exception as error:
            traceback.print_exc()
            return {"status": 503, "response": str(error)}


    def format_layout(self, country: str | None = "all") -> list:
        """ This function formated html and transformed in dict
        Layout in 14/04/2021
        <tr>
            <td>20.151.27.156</td>           # param: ==> hostname: {"type": "CharField", "return": "CharField"}
            <td>3128</td>                    # param: ==> port: {"type": "CharField", "return": "CharField"}
            <td>CA</td>                      # param: ==> id_country: {"type": "CharField", "return": "CharField"}
            <td class="hm">Canada</td>       # param: ==> country: {"type": "CharField", "return": "CharField"}
            <td>anonymous</td>               # param: ==> anonymity: {"type": "CharField", "return": "CharField"}
            <td class="hm">no</td>           # param: ==> google: {"type": "CharField", "return": "Boolean"}
            <td class="hx">yes</td>          # param: ==> https: {"type": "CharField", "return": "Boolean"}
            <td class="hm">1 minute ago</td> # param: ==> last_checked: {"type": "CharField", "return": "TimeStampDescription"}
        </tr>"""
        try:
            soup = self.get_page_html().get("soup")
            table = soup.body.tbody.find_all(["tr"])
            self.list_proxie = []

            for tag in table:
                if tag is not [] and country.lower() == "all":
                    self.list_proxie.append({"hostname": tag.findAll("td")[0].text,
                                             "port": tag.findAll("td")[1].text,
                                             "id_country": tag.findAll("td")[2].text,
                                             "country": tag.findAll("td")[3].text,
                                             "anonymity": tag.findAll("td")[4].text,
                                             "google": tag.findAll("td")[5].text,
                                             "https": tag.findAll("td")[6].text,
                                             "last_checked": tag.findAll("td")[7].text})

                if country and tag is not [] and tag.findAll("td")[2].text.lower() == country:
                    self.list_proxie.append({"hostname": tag.findAll("td")[0].text,
                                             "port": tag.findAll("td")[1].text,
                                             "id_country": tag.findAll("td")[2].text,
                                             "country": tag.findAll("td")[3].text,
                                             "anonymity": tag.findAll("td")[4].text,
                                             "google": tag.findAll("td")[5].text,
                                             "https": tag.findAll("td")[6].text,
                                             "last_checked": tag.findAll("td")[7].text})

            proxy_list = []
            for row in self.list_proxie:
                if row.get("https") == "yes":
                    proxy_list.append(f"https://{row.get('hostname')}:{row.get('port')}")
                else:
                    proxy_list.append(f"http://{row.get('hostname')}:{row.get('port')}")

            return proxy_list

        except Exception as error:
            traceback.print_exc()
            return {"status": 503, "response": str(error)}

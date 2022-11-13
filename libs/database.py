# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    database.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: michael.ortiz <michael.ortiz@dotpyc.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/11 23:55:07 by michael.ort       #+#    #+#              #
#    Updated: 2022/11/12 11:04:24 by michael.ort      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import redis
from libs.config import conf


redis_client = redis.Redis(
    host=conf.get("redis").get("host"),
    password=conf.get("redis").get("secret"),
    port=conf.get("redis").get("port"),
    db=conf.get("redis").get("database"))

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: michael.ortiz <michael.ortiz@dotpyc.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/12 11:02:55 by michael.ort       #+#    #+#              #
#    Updated: 2022/11/12 11:08:28 by michael.ort      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import json

app_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(app_path, "config.json")) as json_file:
    conf = json.loads(json_file.read())

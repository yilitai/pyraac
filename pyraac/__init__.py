# Copyright (c) 2024 Litai Yi
#
# -*- coding:utf-8 -*-
# @Script: __init__.py
# @Author: Litai Yi
# @Email: yilitai@outlook.com
# @Last Modified By: Litai Yi
# @Last Modified At: 2024-10-13 11:23:03
# @Description: pyraac is a python package for complex reduction of amino acid sequences.

import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RT_DESC_PATH = BASE_DIR / Path("./json") / "rt_desc.json"
RT_OPTION_PATH = BASE_DIR / Path("./json") / "rt_option.json"
RT_TOPARENT_PATH = BASE_DIR / Path("./json") / "rt_toparent.json"


def raac_len():  # 检查一下长度
    temp_rt_toparent = None
    with open(RT_TOPARENT_PATH, "r", encoding="utf-8") as file:
        temp_rt_toparent = json.load(file)

    max_raa_value = max([int(item) for item in temp_rt_toparent.keys()])
    return max_raa_value

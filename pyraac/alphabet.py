import json

from pyraac import RT_DESC_PATH, RT_OPTION_PATH, RT_TOPARENT_PATH, raac_len


class Alphabet:
    def __init__(self, raa_value):
        self.raa_value = None

        if (
            isinstance(raa_value, int)
            and (raa_value > 999)
            and (raa_value < (raac_len() + 1))
        ):
            self.raa_value = raa_value

        else:
            raise RuntimeError(
                f"The range of 'raa_value' is between '1000' to {raac_len() + 1}"
            )

        self.parent_raa_value = None

        with open(RT_TOPARENT_PATH, "r", encoding="utf-8") as file:
            temp_rt_toparent_dict = json.load(file)

            self.parent_raa_value = temp_rt_toparent_dict[str(raa_value)]

        self.method = None
        self.desc = None
        self.vancouver = None
        self.value = None

        with open(RT_DESC_PATH, "r", encoding="utf-8") as file:
            temp_rt_desc_dict = json.load(file)
            desc_object = temp_rt_desc_dict[str(raa_value)]
            self.method = desc_object["method"]
            self.desc = desc_object["desc"]
            self.vancouver = desc_object["vancouver"]

        with open(RT_OPTION_PATH, "r", encoding="utf-8") as file:
            temp_rt_option_dict = json.load(file)
            option_object = temp_rt_option_dict[self.parent_raa_value]

            index = [item["raaValue"] for item in option_object["raaClusters"]].index(
                raa_value
            )
            self.value = option_object["raaClusters"][index]["raaLabel"]

import json
from ..helpers.guardianid import id_getter


class DataBase:
    """
    Class for accessing Guardians data
    """

    def __init__(self) -> None:

        self.error = None
        self.name = None
        self.code_name = None
        self.catchline = None
        self.type = None
        self.img_url = None

        self.health = None
        self.attack = None
        self.defense = None
        self.focus = None

        self.abilities = None
        self.talents = None

    def get_data(self, guardianid: str, tier: int, astral: int = 0):

        guardianid = id_getter(guardianid)

        if tier not in range(1, 6):
            if tier < 1:
                self.error = "Tier of guardian cannot be less than 1"
            elif tier > 5:
                self.error = "Tier of guardian cannot be more than 5"
            raise ValueError
        else:
            try:
                with open(f"./data/{guardianid}.json", "r") as fp:
                    data = json.load(fp)
                    self.name = data["name"]
                    self.code_name = data["code_name"]
                    self.catchline = data["catchline"]
                    self.type = data["type"]
                    self.img_url = data["image_url"]

                    if tier in range(1, 5):
                        self.astral = 0
                        self.health = data["data"][f"rarity_{tier}"]["health"]
                        self.attack = data["data"][f"rarity_{tier}"]["attack"]
                        self.defense = data["data"][f"rarity_{tier}"]["defense"]
                        self.focus = data["data"][f"rarity_{tier}"]["focus"]

                    elif tier == 5:
                        print(astral)
                        if astral in range(0, 11):
                            self.astral = astral

                            if astral == 0:
                                self.health = data["data"][f"rarity_{tier}"]["health"]
                                self.attack = data["data"][f"rarity_{tier}"]["attack"]
                                self.defense = data["data"][f"rarity_{tier}"]["defense"]
                                self.focus = data["data"][f"rarity_{tier}"]["focus"]
                            else:
                                self.health = data["data"][f"astral_{astral}"]["health"]
                                self.attack = data["data"][f"astral_{astral}"]["attack"]
                                self.defense = data["data"][f"astral_{astral}"][
                                    "defense"
                                ]
                                self.focus = data["data"][f"astral_{astral}"]["focus"]
                        else:
                            if astral > 10:
                                self.error = "Astral Rating cannot be more than 10"
                            elif astral < 0:
                                self.error = "Astral Rating cannot be less than 0"

                    self.abilities = data["abilities"]
                    self.talents = data["talents"]

            except FileNotFoundError:
                self.error = f"'{guardianid}' is not a valid Guardian ID."
                raise FileNotFoundError

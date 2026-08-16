import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import time

normal_reset = 4
mirage_reset = 2

app = FastAPI()

@app.get("/info/fruits/{fruit_name}")
def fruit_info(fruit_name: str):
    try:
        url = f"https://bloxfruitsvalues.com/values/fruits/{fruit_name}"

        resp = requests.get(url, timeout=5)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        label_value = soup.find("span", string="Value")
        label_beli = soup.find("span", string="Beli Price")
        label_best_use = soup.find("span", string="Best Used For")
        label_demand = soup.find("span", string="Demand")
        label_type = soup.find("span", string="Fruit Type")

        rarities = [
            "Mythical",
            "Legendary",
            "Rare",
            "Uncommon",
            "Common",
            "Limited"
        ]

        rarity = None

        for item in rarities:
            found = soup.find(
                string=lambda text: text and text.strip().lower() == item.lower()
            )

            if found:
                rarity = found.strip()
                break

        if not label_value:
            return {
                "message": "not found"
            }

        main_value = label_value.find_next_sibling("span")
        main_beli = label_beli.find_next_sibling("span") if label_beli else None
        main_best_use = label_best_use.find_next_sibling("span") if label_best_use else None
        main_demand = label_demand.find_next_sibling("span") if label_demand else None
        main_type = label_type.find_next_sibling("span") if label_type else None

        if not main_value:
            return {
                "message": "not found"
            }

        return {
            "message": "found",
            "value": main_value.get_text(strip=True),
            "beli_price": main_beli.get_text(strip=True) if main_beli else None,
            "best_use": main_best_use.get_text(strip=True) if main_best_use else None,
            "demand": main_demand.get_text(strip=True) if main_demand else None,
            "rarity": rarity,
            "type": main_type.get_text(strip=True) if main_type else None
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }

    except Exception as e:
        return {
            "error": str(e)
        }
@app.get("/info/gamepasses/{gamepass_name}")
def gamepass_info(gamepass_name: str):
    try:
        url = f"https://bloxfruitsvalues.com/values/gamepasses/{gamepass_name}"

        resp = requests.get(url, timeout=5)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        label_value = soup.find("span", string="Value")
        label_demand = soup.find("span", string="Demand")
        label_type = soup.find("span", string="Type")
        label_robux = soup.find("span", string="Robux Price")
        label_tradable = soup.find("span", string="Tradeable")
        label_tier = soup.find("span", string="Tier")
        label_trend = soup.find("span", string="Trend")

        if not label_value:
            return {
                "message": "not found"
            }

        main_value = label_value.find_next_sibling("span")
        main_robux = label_robux.find_next_sibling("span") if label_robux else None
        main_tradeable = label_tradable.find_next_sibling("span") if label_tradable else None
        main_demand = label_demand.find_next_sibling("span") if label_demand else None
        main_type = label_type.find_next_sibling("span") if label_type else None
        main_tier = label_tier.find_next_sibling("span") if label_tier else None
        main_trend = label_trend.find_next_sibling("span") if label_trend else None

        if not main_value:
            return {
                "message": "not found"
            }

        return {
            "message": "found",
            "value": main_value.get_text(strip=True),
            "robux_price": main_robux.get_text(strip=True) if main_robux else None,
            "tradeable": main_tradeable.get_text(strip=True) if main_tradeable else None,
            "demand": main_demand.get_text(strip=True) if main_demand else None,
            "tier": main_tier.get_text(strip=True) if main_tier else None,
            "type": main_type.get_text(strip=True) if main_type else None,
            "trend": main_trend.get_text(strip=True) if main_trend else None
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/info/limiteds/{limited_name}")
def limiteds_info(limited_name: str):
    try:
        url = f"https://bloxfruitsvalues.com/values/limiteds/{limited_name}"

        resp = requests.get(url, timeout=5)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        label_value = soup.find("span", string="Value")
        label_demand = soup.find("span", string="Demand")
        label_type = soup.find("span", string="Type")
        label_robux = soup.find("span", string="Robux Price")
        label_tradable = soup.find("span", string="Tradeable")
        label_tier = soup.find("span", string="Tier")
        label_trend = soup.find("span", string="Trend")

        if not label_value:
            return {
                "message": "not found"
            }

        main_value = label_value.find_next_sibling("span")
        main_robux = label_robux.find_next_sibling("span") if label_robux else None
        main_tradeable = label_tradable.find_next_sibling("span") if label_tradable else None
        main_demand = label_demand.find_next_sibling("span") if label_demand else None
        main_type = label_type.find_next_sibling("span") if label_type else None
        main_tier = label_tier.find_next_sibling("span") if label_tier else None
        main_trend = label_trend.find_next_sibling("span") if label_trend else None

        if not main_value:
            return {
                "message": "not found"
            }

        return {
            "message": "found",
            "value": main_value.get_text(strip=True),
            "robux_price": main_robux.get_text(strip=True) if main_robux else None,
            "tradeable": main_tradeable.get_text(strip=True) if main_tradeable else None,
            "demand": main_demand.get_text(strip=True) if main_demand else None,
            "tier": main_tier.get_text(strip=True) if main_tier else None,
            "type": main_type.get_text(strip=True) if main_type else None,
            "trend": main_trend.get_text(strip=True) if main_trend else None
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }

    except Exception as e:
        return {
            "error": str(e)
        }
@app.get("/info/stock")
def stock_all():
    def get_current_utc_time():
        current_time = time.gmtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec
        return hour, minute, second

    def seconds_until_next_reset(interval_hours):
        hour, minute, second = get_current_utc_time()
        hours_since_last_reset = hour % interval_hours
        seconds_passed = (
            (hours_since_last_reset * 3600) + (minute * 60) + second
        )
        total_seconds_in_interval = interval_hours * 3600
        seconds_left = total_seconds_in_interval - seconds_passed
        return seconds_left

    try:
        url = "https://fruityblox.com/stock"
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        normal_fruits = []
        mirage_fruits = []

        for h2 in soup.find_all("h2"):
            title = h2.get_text(strip=True)

            if title in ["Normal", "Mirage"]:
                section = h2.find_parent("section")

                if not section:
                    continue

                fruits = []

                for h3 in section.find_all("h3"):
                    fruits.append(h3.get_text(strip=True))

                if title == "Normal":
                    normal_fruits = fruits

                elif title == "Mirage":
                    mirage_fruits = fruits

        return {
            "status": True,
            "next_normal": seconds_until_next_reset(normal_reset),
            "next_mirage": seconds_until_next_reset(mirage_reset),
            "normal_now": normal_fruits,
            "mirage_now": mirage_fruits
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }

    except Exception as e:
        return {
            "error": str(e)
        }
@app.get("/fruits")
def fruits_list():
    return {
        "message": "found",
        "West-Dragon": "west-dragon",
        "East-Dragon": "east-dragon",
        "Kitsune": "kitsune",
        "Control": "control",
        "Yeti": "yeti",
        "Gas": "gas",
        "Tiger": "tiger",
        "Lightning": "lightning",
        "Venom": "venom",
        "Dough": "dough",
        "Pain": "pain",
        "T-Rex": "t-rex",
        "Gravity": "gravity",
        "Mammoth": "mammoth",
        "Spirit": "spirit",
        "Shadow": "shadow",
        "Portal": "portal",
        "Buddha": "buddha",
        "Blizzard": "blizzard",
        "Creation": "creation",
        "Phoenix": "phoenix",
        "Sound": "sound",
        "Spider": "spider",
        "Love": "love",
        "Magma": "magma",
        "Quake": "quake",
        "Diamond": "diamond",
        "Light": "light",
        "Ghost": "ghost",
        "Eagle": "eagle",
        "Rubber": "rubber",
        "Ice": "ice",
        "Sand": "sand",
        "Dark": "dark",
        "Flame": "flame",
        "Spike": "spike",
        "Smoke": "smoke",
        "Bomb": "bomb",
        "Spring": "spring",
        "Blade": "blade",
        "Spin": "spin",
        "Rocket": "rocket"
    }


@app.get("/gamepasses")
def gamepasses():
    return {
        "Fruit-Notifier": "fruit-notifier",
        "Dark-Blade": "dark-blade",
        "Mythical-Scrolls": "mythical-scrolls",
        "Legendary-Scrolls": "legendary-scrolls",
        "+1-Fruit-Storage": "+1-fruit-storage",
        "2x-Mastery": "2x-mastery",
        "2x-Money": "2x-money",
        "2x-Boss-Drops": "2x-boss-drops",
        "Fast-Boats": "fast-boats"
    }


@app.get("/limiteds")
def limiteds():
    return {
        "Fiend Yeti": "fiend-yeti",
        "Galaxy Empyrean Kitsune": "galaxy-empyrean-kitsune",
        "Ember West Dragon": "ember-west-dragon",
        "Crimson Kitsune": "crimson-kitsune",
        "Meme-Meme": "meme-meme",
        "Divine Portal": "divine-portal",
        "Purple Lightning": "purple-lightning",
        "Parrot": "parrot",
        "Red Lightning": "red-lightning",
        "Yellow Lightning": "yellow-lightning",
        "Green Lightning": "green-lightning",
        "Werewolf": "werewolf",
        "Rose Quartz Diamond": "rose-quartz-diamond",
        "Emerald Diamond": "emerald-diamond",
        "Topaz Diamond": "topaz-diamond",
        "Ruby Diamond": "ruby-diamond",
        "Dragon Token": "dragon-token",
        "Eclipse": "eclipse",
        "Super Spirit Pain": "super-spirit-pain",
        "Torment Pain": "torment-pain",
        "Sadness Pain": "sadness-pain",
        "Frustration Pain": "frustration-pain",
        "Celestial Pain": "celestial-pain",
        "Eagle Requiem": "eagle-requiem",
        "Eagle Glacier": "eagle-glacier",
        "Eagle Matrix": "eagle-matrix",
        "Celebration Bomb": "celebration-bomb",
        "Azura Bomb": "azura-bomb",
        "Thermite Bomb": "thermite-bomb",
        "Nuclear Bomb": "nuclear-bomb"
    }
def id_getter(champ):

    champ_urls = {
        "buzz": "buzz-lightyear",
        "hook": "captain-hook",
        "cruella": "cruella-de-vil",
        "hiro": "hiro-hamada",
        "frank": "frank-wolff",
        "ian": "ian-lightfoot",
        "judy": "judy-hopps",
        "kermit": "kermit-the-frog",
        "mickey":"mickey-mouse",
        "mike": "mike-wazowski",
        "minnie": "minnie-mouse",
        "violet": "violet-parr",
        "walle": "wall-e",
    }

    try:
        champurl = champ_urls[champ]
        return champurl
    except:
        return champ


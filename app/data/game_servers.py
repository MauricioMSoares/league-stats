servers: list[tuple[str, str]] = [
    ("BR1", "Brazil"),
    ("EUN1", "Europe Nordic & East"),
    ("EUW1", "Europe West"),
    ("JP1", "Japan"),
    ("KR", "Republic of Korea"),
    ("LA1", "Latin America North"),
    ("LA2", "Latin America South"),
    ("ME1", "Middle East"),
    ("NA1", "North America"),
    ("OC1", "Oceania"),
    ("RU", "Russia"),
    ("SG2", "Singapore and Malaysia"),
    ("TR1", "Turkey"),
    ("TW2", "Taiwan, Hong Kong, and Macao"),
    ("VN2", "Vietnam"),
]

servers_dict = {code: name for (code, name) in servers}

region_by_server = {
    "BR1": "americas",
    "LA1": "americas",
    "LA2": "americas",
    "NA1": "americas",
    "OC1": "americas",

    "KR": "asia",
    "JP1": "asia",
    "SG2": "asia",
    "TW2": "asia",
    "VN2": "asia",

    "EUN1": "europe",
    "EUW1": "europe",
    "RU": "europe",
    "TR1": "europe",
    "ME1": "europe"
}
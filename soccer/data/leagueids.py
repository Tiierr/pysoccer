__all__ = ['LEAGUE_IDS']

LEAGUE_IDS ={
    "BSA": 444,
    "PL": 445,
    "ELC": 446,
    "EL1": 447,
    "EL2": 448,
    "DED": 449,
    "FL1": 450,
    "FL2": 451,
    "BL1": 452,
    "BL2": 453,
    "PD": 455,
    "SA": 456,
    "PPL": 457,
    "DFB": 458,
    "SB": 459,
    "CL": 464,
    "AAL": 466
}


"""
更新当前赛季联赛序号

import requests
import json

__all__ = ['LEAGUE_IDS']

res = requests.get('http://api.football-data.org/v1/competitions')
competitions = json.loads(res.content.decode('utf-8'))

LEAGUE_IDS = {}

for cpt in competitions:
    LEAGUE_IDS[cpt['league']] = cpt['id']
"""

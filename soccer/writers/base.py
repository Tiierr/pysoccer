from abc import ABCMeta, abstractmethod
from itertools import groupby

from soccer.data import LEAGUE_IDS

__all__ = ['BaseWriter']

class BaseWriter(object):
    __metaclass__ = ABCMeta

    def __init__(self, output_file):
        self.output_filename = output_file

    @abstractmethod
    def live_scores(self, live_scores):
        pass

    @abstractmethod
    def team_scores(self, team_scores, time):
        pass

    @abstractmethod
    def team_players(self, team):
        pass

    @abstractmethod
    def standings(self, league_table, league):
        pass

    @abstractmethod
    def league_scores(self, total_data, time):
        pass

    def supported_leagues(self, total_data):
        """Filters out scores of unsupported leagues"""
        supported_leagues = {val: key for key, val in LEAGUE_IDS.items()}
        get_league_id = lambda x: int(x["_links"]["soccerseason"]["href"].split("/")[-1])
        fixtures = (fixture for fixture in total_data["fixtures"]
                    if get_league_id(fixture) in supported_leagues)

        # Sort the scores by league to make it easier to read
        fixtures = sorted(fixtures, key=get_league_id)
        for league, scores in groupby(fixtures, key=get_league_id):
            league = supported_leagues[league]
            for score in scores:
                yield league, score

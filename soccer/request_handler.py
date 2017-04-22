import requests
import click
from .exceptions import APIErrorException
from soccer.data import LEAGUE_LISTS, urls
import json

__all__ = ['RequestHandler']

class RequestHandler(object):

    BASE_URL = urls['base']
    SEASON_URL = urls['season']

    def __init__(self, headers, league_ids, team_names, writer):
        self.headers = headers
        self.league_ids = league_ids
        self.team_names = team_names
        self.writer = writer

    def _get(self, url):
        """Handles api.football-data.org requests"""
        req = requests.get(RequestHandler.BASE_URL + url, headers=self.headers)
        if req.status_code == requests.codes.ok:
            return req

        if req.status_code == requests.codes.bad:
            raise APIErrorException('Invalid request. Check parameters.')

        if req.status_code == requests.codes.forbidden:
            raise APIErrorException('This resource is restricted')

        if req.status_code == requests.codes.not_found:
            raise APIErrorException('This resource does not exist. Check parameters')

        if req.status_code == requests.codes.too_many_requests:
            raise APIErrorException('You have exceeded your allowed requests per minute/day')

    def _get_by_season(self, url):
        """Handles api.football-data.org requests"""
        req = requests.get(RequestHandler.SEASON_URL + url, headers=self.headers)

        if req.status_code == requests.codes.ok:
            return req

        if req.status_code == requests.codes.bad:
            raise APIErrorException('Invalid request. Check parameters.')

        if req.status_code == requests.codes.forbidden:
            raise APIErrorException('This resource is restricted')

        if req.status_code == requests.codes.not_found:
            raise APIErrorException('This resource does not exist. Check parameters')

        if req.status_code == requests.codes.too_many_requests:
            raise APIErrorException('You have exceeded your allowed requests per minute/day')


    def get_league(self, league):
        league_id = self.league_ids[league]
        try:
            req = self._get('competitions/{id}'.format(id=league_id))
            self.writer.league(req.json())
        except APIErrorException:
            click.secho("No information availble for {league}.".format(league=league),
                        fg="red", bold=True)

    def get_leagues(self):
        try:
            req = self._get('competitions')
            self.writer.leagues(req.json())
        except APIErrorException:
            click.secho("No information.",fg="red", bold=True)

    def get_leagues_by_season(self, season):
        try:
            req = self._get_by_season('soccerseasons?season={season}'
                            .format(season=season))
            self.writer.leagues_by_season(req.json())
        except APIErrorException:
            click.secho("No information availble for {season}."
                        .format(season=season), fg="red", bold=True)

    def get_standings(self, league):
        """Queries the API and gets the standings for a particular league"""
        league_id = self.league_ids[league]
        try:
            req = self._get('competitions/{id}/leagueTable'.format(id=league_id))
            self.writer.standings(req.json(), league)
        except APIErrorException:
            click.secho("No standings availble for {league}."
                    .format(league=league), fg="red", bold=True)

    def get_standings_by_matchday(self, league, md):
        """Queries the API and gets the standings for a particular league"""
        league_id = self.league_ids[league]
        try:
            req = self._get('competitions/{id}/leagueTable?matchday={md}'
                            .format(id=league_id,md=md))
            self.writer.standings(req.json(), league)
        except APIErrorException:
            click.secho("No standings availble for {league}."
                    .format(league=league),fg="red", bold=True)

    def get_teams(self, league):
        league_id = self.league_ids[league]
        try:
            req = self._get('competitions/{id}/teams'.format(id=league_id))
            self.writer.teams(req.json())
        except APIErrorException:
            click.secho("No teams availble for {league}."
                    .format(league=league), fg="red", bold=True)

    def get_players(self, team):
        team_id = self.team_names[team]
        try:
            req = self._get('teams/{id}/players'.format(id=team_id))
            self.writer.players(req.json(), team)
        except APIErrorException:
            click.secho("No players availble for {team}.".format(team=team),
                        fg="red", bold=True)

    def get_fixtures(self):
        try:
            req = self._get('fixtures')
            self.writer.fixtures(req.json())
        except APIErrorException:
            click.secho("No fixtures availble.", fg="red", bold=True)

    def get_fixtures_by_tf(self, tf):
        try:
            req = self._get('fixtures?timeFrame={tf}'.format(tf=tf))
            self.writer.fixtures(req.json())
        except APIErrorException:
            click.secho("No fixtures availble.", fg="red", bold=True)

    def get_fixtures_by_league(self, league):
        league_id = self.league_ids[league]
        try:
            req = self._get('competitions/{id}/fixtures'.format(id=league_id))
            self.writer.fixtures(req.json())
        except APIErrorException:
            click.secho("No teams availble for {league}."
                    .format(league=league), fg="red", bold=True)

    def get_fixtures_by_md_league(self, md, league):
        league_id = self.league_ids[league]
        try:
            req = self._get('competitions/{id}/fixtures?matchday={md}'
                            .format(id=league_id, md=md))
            self.writer.fixtures(req.json())
        except APIErrorException:
            click.secho("No fixtures availble.", fg="red", bold=True)


    def get_fixtures_by_tf_league(self, tf, league):
        league_id = self.league_ids[league]
        try:
            req = self._get('competitions/{id}/fixtures?timeFrame={tf}'
                            .format(id=league_id,tf=tf))
            self.writer.fixtures(req.json())
        except APIErrorException:
            click.secho("No fixtures availble.", fg="red", bold=True)

    def get_fixtures_by_md_tf_league(self, md, tf, league):
        league_id = self.league_ids[league]
        try:
            req = self._get('competitions/{id}/fixtures?matchday={md}&timeFrame={tf}'
                            .format(id=league_id, md=md, tf=tf))
            self.writer.fixtures(req.json())
        except APIErrorException:
            click.secho("No fixtures availble.", fg="red", bold=True)

    def get_fixtures_by_team(self, team):
        team_id = self.team_names[team]
        try:
            req = self._get('teams/{id}/fixtures'.format(id=team_id))
            self.writer.fixtures(req.json())
        except APIErrorException:
            click.secho("No fixtures availble for {team}."
                    .format(team=team), fg="red", bold=True)

    def get_fixtures_by_id(self, id, h2h):
        try:
            req = self._get('fixtures/{id}?head2head={h2h}'.format(id=id, h2h=h2h))
            self.writer.fixtures_by_id(req.json())
        except APIErrorException:
            click.secho("No fixtures availble.", fg="red", bold=True)

    def get_lists(self):
        try:
            self.writer.lists(LEAGUE_LISTS)
        except APIErrorException:
            click.secho("No leagues availble.", fg="red", bold=True)

    def jsonify(self,data):
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)

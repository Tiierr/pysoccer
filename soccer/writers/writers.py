from soccer.data import LEAGUE_PROPERTIES, LEAGUE_NAMES
from . import BaseWriter

import click
import json
import io

__all__ = ['Stdout', 'Fstdout', 'Fjson', 'Json']

class Stdout(BaseWriter):
    def __init__(self, output_file):
        enums = dict(
            CL_POSITION="green",
            EL_POSITION="yellow",
            RL_POSITION="red",
            POSITION="blue",
            TEXT="yellow",
        )
        self.colors = type('Enum', (), enums)


    def league(self, league_table):
        click.secho("-"*100, fg="green", bold=True)
        click.secho("%-35s %-8s %-8s %-8s %-8s %-8s %-8s" %
                    ("CAPTION", "CM", "LEAGUE", "GAMES","MD", "TEAMS", "YEAR"))
        click.secho("-"*100, fg="green", bold=True)
        league_str = (u"{caption:<35} {currentMatchday:<8} {league:<9}"
                      u"{numberOfGames:<8} {numberOfMatchdays:<9}"
                      u"{numberOfTeams:<8} {year}").format(**league_table)
        click.secho(league_str, bold=True, fg=self.colors.TEXT)
        click.secho("-"*100, fg="green", bold=True)

    def leagues(self, league_table):
        click.secho("-"*100, fg="green", bold=True)
        click.secho("%-35s %-8s %-8s %-8s %-8s %-8s %-8s" %
                    ("CAPTION", "CM", "LEAGUE", "GAMES","MD", "TEAMS", "YEAR"))
        click.secho("-"*100, fg="green", bold=True)

        for league in league_table:
            league_str = (u"{caption:<35} {currentMatchday:<8} {league:<9}"
                          u"{numberOfGames:<8} {numberOfMatchdays:<9}"
                          u"{numberOfTeams:<8} {year}").format(**league)
            click.secho(league_str, bold=True, fg=self.colors.TEXT)

        click.secho("-"*100, fg="green", bold=True)


    def leagues_by_season(self, league_table):
        click.secho("-"*80, fg="green", bold=True)
        click.secho("%-35s %-8s %-8s %-8s %-8s" %
                    ("CAPTION", "LEAGUE", "GAMES", "TEAMS", "YEAR"))
        click.secho("-"*80, fg="green", bold=True)

        for league in league_table:
            league_str = (u"{caption:<35} {league:<9} {numberOfGames:<8}"
                          u"{numberOfTeams:<8} {year}").format(**league)
            click.secho(league_str, bold=True, fg=self.colors.TEXT)
        click.secho("-"*80, fg="green", bold=True)

    def standings(self, league_table, league):
        """ Prints the league standings in a pretty way """
        click.secho("-"*80, fg="green", bold=True)
        click.secho("%-6s  %-30s    %-10s    %-10s    %-10s" %
                    ("POS", "CLUB", "PLAYED", "GOAL DIFF", "POINTS"))
        click.secho("-"*80, fg="green", bold=True)

        for team in league_table["standing"]:
            if team["goalDifference"] >= 0:
                team["goalDifference"] = ' ' + str(team["goalDifference"])

            cl_upper, cl_lower = LEAGUE_PROPERTIES[league]['cl']
            el_upper, el_lower = LEAGUE_PROPERTIES[league]['el']
            rl_upper, rl_lower = LEAGUE_PROPERTIES[league]['rl']

            team_str = (u"{position:<7} {teamName:<33} {playedGames:<12}"
                        u" {goalDifference:<14} {points}").format(**team)
            if cl_upper <= team["position"] <= cl_lower:
                click.secho(team_str, bold=True, fg=self.colors.CL_POSITION)
            elif el_upper <= team["position"] <= el_lower:
                click.secho(team_str, fg=self.colors.EL_POSITION)
            elif rl_upper <= team["position"] <= rl_lower:
                click.secho(team_str, fg=self.colors.RL_POSITION)
            else:
                click.secho(team_str, fg=self.colors.POSITION)
        click.secho("-"*80, fg="green", bold=True)

    def teams(self, league_table):
        click.secho("-"*80, fg="green", bold=True)
        click.secho("%-28s %-20s %-10s %-20s" %
                    ("NAME", "SHORT NAME", "CODE", "MARKET VALUE"))
        click.secho("-"*80, fg="green", bold=True)
        for team in league_table['teams']:
            self.toNone(team)
            team_str = (u"{name:<28} {shortName:<20} {code:<10}"
                        u"{squadMarketValue}").format(**team)
            click.secho(team_str, bold=True, fg=self.colors.TEXT)
        click.secho("-"*80, fg="green", bold=True)


    def players(self, league_table, team):
        click.secho("-"*120, fg="green", bold=True)
        click.secho("%-27s %-10s %-21s %-15s %-25s %-15s" %
                    ("NAME", "NUMBER", "POSITION","BIRTH",
                    "NATIONALITY", "CONTRACT UNTIL"))
        click.secho("-"*120, fg="green", bold=True)

        for player in league_table['players']:
            self.toNone(player)
            player_str = (u"{name:<27} {jerseyNumber:<10} {position:<22}"
                        u"{dateOfBirth:<15} {nationality:<25} {contractUntil}").format(**player)
            click.secho(player_str, bold=True, fg=self.colors.TEXT)
        click.secho("-"*120, fg="green", bold=True)

    def fixtures(self, league_table):
        click.secho("-"*120, fg="green", bold=True)
        click.secho("%-27s %-27s %-6s %-6s %-22s %-10s %-8s %-6s" %
                    ("HOME TEAM", "AWAY TEAM", "RES","MD",
                    "DATE", "STATUS", "ID", "LEAGUE"))
        click.secho("-"*120, fg="green", bold=True)

        for fixture in league_table['fixtures']:
            fixture['league'] = LEAGUE_NAMES[fixture['competitionId']]
            if fixture['result']['goalsAwayTeam'] is None:
                fixture['result'] = 'None'
            else:
                fixture['result'] = '{0}:{1}'.format(fixture['result']['goalsHomeTeam'], fixture['result']['goalsAwayTeam'])
            fixture_str= (u"{homeTeamName:<27} {awayTeamName:<27} "
                        u"{result:<6} {matchday:<6} {date:<22} "
                        u"{status:<10} {id:<8} {league}").format(**fixture)
            click.secho(fixture_str, bold=True, fg=self.colors.TEXT)
        click.secho("-"*120, fg="green", bold=True)

    def fixtures_by_id(self, league_table):
        click.secho("-"*120, fg="green", bold=True)
        click.secho("%-27s %-27s %-6s %-6s %-22s %-10s %-8s %-6s" %
                    ("HOME TEAM", "AWAY TEAM", "RES","MD",
                    "DATE", "STATUS", "ID", "LEAGUE"))
        click.secho("-"*120, fg="green", bold=True)

        for fixture in league_table['head2head']['fixtures']:
            fixture['league'] = LEAGUE_NAMES[fixture['competitionId']]
            if fixture['result']['goalsAwayTeam'] is None:
                fixture['result'] = 'None'
            else:
                fixture['result'] = '{0}:{1}'.format(
                        fixture['result']['goalsHomeTeam'], fixture['result']['goalsAwayTeam'])

            if fixture['status'] is None:
                fixture['status'] = 'FINISHED'

            fixture_str = (u"{homeTeamName:<27} {awayTeamName:<27} "
                        u"{result:<6} {matchday:<6} {date:<22} "
                        u"{status:<10} {id:<8} {league}").format(**fixture)
            click.secho(fixture_str, bold=True, fg=self.colors.TEXT)
        click.secho("-"*120, fg="green", bold=True)

        HOME = league_table['fixture']['homeTeamName']
        AWAY = league_table['fixture']['awayTeamName']
        HW = league_table['head2head']['homeTeamWins']
        AW = league_table['head2head']['awayTeamWins']
        COUNT = league_table['head2head']['count']

        league_table['head2head']['homeWins'] = round(HW / COUNT, 2)
        league_table['head2head']['awayWins'] = round(AW / COUNT, 2)

        click.secho("%-30s %-29s %-6s %-6s %-10s %-10s %-12s %-12s" %
                    (HOME + " WINS", AWAY + " WINS","DRAWS", "COUNT",
                    "HOME WINS", "AWAY WINS", "START", "END"))

        result_str = (u"{homeTeamWins:<30} {awayTeamWins:<30}"
            u"{draws:<6} {count:<6} {homeWins:<11}"
            u"{awayWins:<10} {timeFrameStart:<13}"
            u"{timeFrameEnd}").format(**league_table['head2head'])

        click.secho(result_str, bold=True, fg=self.colors.TEXT)
        click.secho("-"*120, fg="green", bold=True)

    def lists(self, league_table):
        click.secho("-"*45, fg="green", bold=True)
        click.secho("%-10s %-20s" %("LEAGUE", "CAPTION"))
        click.secho("-"*45, fg="green", bold=True)

        for _list in league_table:
            list_str= (u"{league:<10} {caption}").format(**_list)
            click.secho(list_str, bold=True, fg=self.colors.TEXT)
        click.secho("-"*45, fg="green", bold=True)

    def toNone(self, lists):
        for key in lists:
            if lists[key] is None:
                lists[key] = 'None'

class Fstdout(BaseWriter):
    def __init__(self,output_file):

        enums = dict(
            CL_POSITION="green",
            EL_POSITION="yellow",
            RL_POSITION="red",
            POSITION="blue",
        )
        self.colors = type('Enum', (), enums)

    def standings(self, league_table, league):
        """ Prints the league standings in a pretty way """
        click.secho("-"*120, fg="green", bold=True)
        click.secho("%-4s %-25s %-9s %-10s %-10s %-9s %-10s %-11s %-11s %-7s" %
                    ("POS", "CLUB", "PLAYED", "WINS", "DRAWS", "LOSSES",
                            "GOALS", "GOAL LOSS", "GOAL DIFF", "POINTS"))
        click.secho("-"*120, fg="green", bold=True)

        for team in league_table["standing"]:
            if team["goalDifference"] >= 0:
                team["goalDifference"] = ' ' + str(team["goalDifference"])

            cl_upper, cl_lower = LEAGUE_PROPERTIES[league]['cl']
            el_upper, el_lower = LEAGUE_PROPERTIES[league]['el']
            rl_upper, rl_lower = LEAGUE_PROPERTIES[league]['rl']

            team_str = (u"{position:<4} {teamName:<25} {playedGames:<10}"
                        u"{wins:<10} {draws:<10} {losses:<10}"
                        u"{goals:<10} {goalsAgainst:<10}"
                        u" {goalDifference:<12} {points}").format(**team)
            if cl_upper <= team["position"] <= cl_lower:
                click.secho(team_str, bold=True, fg=self.colors.CL_POSITION)
            elif el_upper <= team["position"] <= el_lower:
                click.secho(team_str, fg=self.colors.EL_POSITION)
            elif rl_upper <= team["position"] <= rl_lower:
                click.secho(team_str, fg=self.colors.RL_POSITION)
            else:
                click.secho(team_str, fg=self.colors.POSITION)
        click.secho("-"*120, fg="green", bold=True)

class Fjson(BaseWriter):
    def __init__(self, output_file):
        super(Fjson, self).__init__(output_file)

    def generate_output(self, result):
        if not self.output_filename:
            click.echo(json.dumps(result, indent=4, separators=(',', ': '),
                       ensure_ascii=False))
        else:
            with io.open(self.output_filename, 'w', encoding='utf-8') as json_file:
                data = json.dumps(result, json_file, indent=4,
                                  separators=(',', ': '), ensure_ascii=False)
                json_file.write(data)

    def standings(self, league_table, league):
        self.generate_output(league_table)

    def league(self, league_table):
        self.generate_output(league_table)

    def leagues(self, league_table):
        self.generate_output(league_table)

    def teams(self, league_table):
        self.generate_output(league_table)

    def players(self, league_table, team):
        self.generate_output(league_table)

    def fixtures(self, league_table):
        self.generate_output(league_table)

    def fixtures_by_id(self, league_table):
        self.generate_output(league_table)

    def leagues_by_season(self, league_table):
        self.generate_output(league_table)

    def lists(self, league_table):
        self.generate_output(league_table)


class Json(BaseWriter):
    def __init__(self, output_file):
        super(Json, self).__init__(output_file)

    def generate_output(self, result):
        if not self.output_filename:
            click.echo(json.dumps(result, indent=4, separators=(',', ': '),
                       ensure_ascii=False))
        else:
            with io.open(self.output_filename, 'w', encoding='utf-8') as json_file:
                data = json.dumps(result, json_file, indent=4,
                                  separators=(',', ': '), ensure_ascii=False)
                json_file.write(data)

    def standings(self, league_table, league):
        """Store output of league standings to a JSON file"""
        data = []
        for team in league_table['standing']:
            item = {'position': team['position'],
                    'teamName': team['teamName'],
                    'playedGames': team['playedGames'],
                    'goalsFor': team['goals'],
                    'goalsAgainst': team['goalsAgainst'],
                    'goalDifference': team['goalDifference'],
                    'points': team['points']}
            data.append(item)
        self.generate_output({'standings': data})

    def league(self, league_table):
        """Store output of league standings to a JSON file"""

        self.generate_output(league_table)

    def leagues(self, league_table):
        """Store output of league standings to a JSON file"""
        for league in league_table:
            del league['_links']
        self.generate_output(league_table)

    def teams(self, league_table):
        del league_table['_links']
        for team in league_table['teams']:
            del team['_links']
        self.generate_output(league_table)

    def players(self, league_table, team):
        del league_table['_links']
        self.generate_output(league_table)

    def fixtures(self, league_table):
        for fixture in league_table['fixtures']:
            del fixture['odds']
        self.generate_output(league_table)

    def leagues_by_season(self, league_table):
        for league in league_table:
            del league['_links']
        self.generate_output(league_table)

    def lists(self, league_table):
        self.generate_output(league_table)

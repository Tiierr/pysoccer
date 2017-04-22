import os
import sys
import json
import click

from soccer.data import LEAGUE_IDS, TEAM_NAMES, config, urls
from soccer.writers import get_writer
from .exceptions import IncorrectParametersException
from .request_handler import RequestHandler

__all__ = ['main']

key = os.environ.get('SOCCER_CLI_API_TOKEN')  or config['key']

@click.command()
@click.option('--apikey', default=key,
              help="API key to use.")
@click.option('--standings', is_flag=True,
              help="Standings for a particular league.")
@click.option('--lists', is_flag=True,
              help="Lists of all league.")
@click.option('--teams', is_flag=True,
              help="Teams for a particular league.")
@click.option('--team', type=click.Choice(TEAM_NAMES.keys()),
              help=("Choose a particular team."))
@click.option('--players', is_flag=True,
              help="Shows players for a particular team.")
@click.option('--fixtures', is_flag=True,
              help="Shows fixtures.")
@click.option('--id', '-id', type=int,
              help=("Choose the Matchday for team's fixtures."))
@click.option('--h2h', '-h2h', type=int, default=10,
              help=("Choose the numbers of head to head for recently fixtures."))
@click.option('--md', '-md', type=int,
              help=("Choose the Matchday for team's fixtures."))
@click.option('--tf', '-tf', type=int,
              help=("Choose a particular day for team's fixtures. \
                    Positive number means future fixtures, \
                    negative number means previous fixtures"))
@click.option('--league', '-league', type=click.Choice(LEAGUE_IDS.keys()),
              help=("Choose a particular league."))
@click.option('--competition', '-competition',is_flag=True,
              help=("Shows information of the all leagues."))
@click.option('--season', '-season', type=int,
              help=("Choose the season for competition."))
@click.option('--stdout', 'output_format', flag_value='stdout', default=True,
              help="Print to stdout.")
@click.option('--fs', 'output_format', flag_value='fstdout',
              help="Print to stdout for full standings table, except group game.")
@click.option('--gs', 'output_format', flag_value='gstdout',
              help='Print to stdout for the group game of the league.')
@click.option('--json', 'output_format', flag_value='json',
              help='Output in JSON format, except the standings table of group game.')
@click.option('--fjson', 'output_format', flag_value='fjson',
              help='Output in JSON format of the full version.')
@click.option('--gjson', 'output_format', flag_value='gjson',
              help='Output in JSON format for the group game of the league.')
@click.option('-o', '--output-file', default=None,
              help="Save output to a file (only json option is provided).")

def main(league, lists, teams, team, players, fixtures, id, h2h, md, tf,
        competition, season, standings, output_format, output_file, apikey):

    if not key:
        click.secho('No API Token detected. \n'
                    'Please visit {0} and get an API Token, '
                    'which will be used by Soccer '
                    'to get access to the data.'
                    .format(urls['web']), fg="red", bold=True)
        sys.exit(1)

    if fixtures:
        headers = {'X-Auth-Token': apikey, 'X-Response-Control': 'minified'}
    else:
        headers = {'X-Auth-Token': apikey}

    try:
        if output_format in ['stdout', 'fstdout', 'gstdout'] and output_file:
            raise IncorrectParametersException('Printing output to stdout and '
                                               'saving to a file are mutually exclusive')
        writer = get_writer(output_format, output_file)
        rh = RequestHandler(headers, LEAGUE_IDS, TEAM_NAMES, writer)

        if lists:
            rh.get_lists()

        if standings:
            if not league:
                raise IncorrectParametersException('Please specify a league. '
                                                   'Example --standings --league=EPL')
            if league in ['CL', 'EC'] and output_format not in ['gstdout', 'gjson']:
                raise IncorrectParametersException('Standings for CL and EC '
                                                   'Champions League must use --gs(group stdout) '
                                                   'and --gjson(group json) as output format.')
            elif league not in ['CL', 'EC'] and output_format in ['gstdout', 'gjson']:
                    raise IncorrectParametersException('Output format gstdout and gjson '
                                                       'only for EC and CL.')
            if md:
                rh.get_standings_by_matchday(league, md)
            else:
                rh.get_standings(league)

        if teams:
            if not league:
                raise IncorrectParametersException('Please specify a league. '
                                                   'Example --teams --league=PD')
            rh.get_teams(league)

        if competition:
            if league:
                rh.get_league(league)
            elif season:
                rh.get_leagues_by_season(season)
            else:
                rh.get_leagues()

        if players:
            if not team:
                raise IncorrectParametersException('Please specify a league. '
                                                   'Example --players --team=FCB')
            rh.get_players(team)

        if fixtures:
            if tf and md and league:
                tf = 'n' + str(tf) if tf > 0 else 'p' + str(abs(tf))
                rh.get_fixtures_by_md_tf_league(md, tf, league)
            elif tf and league:
                tf = 'n' + str(tf) if tf > 0 else 'p' + str(abs(tf))
                rh.get_fixtures_by_tf_league(tf, league)
            elif md and league:
                rh.get_fixtures_by_md_league(md, league)
            elif tf:
                tf = 'n' + str(tf) if tf > 0 else 'p' + str(abs(tf))
                rh.get_fixtures_by_tf(tf)
            elif team:
                rh.get_fixtures_by_team(team)
            elif league:
                rh.get_fixtures_by_league(league)
            elif id:
                rh.get_fixtures_by_id(id, h2h)

            if not league and not team and not id and not tf and not md:
                rh.get_fixtures()

    except IncorrectParametersException as e:
        click.secho(str(e), fg="red", bold=True)

if __name__ == '__main__':
    main()

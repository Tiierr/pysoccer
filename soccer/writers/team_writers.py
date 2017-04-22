from . import BaseWriter
import click
import json

__all__ = ['Gstdout', 'Gjson']

class Gstdout(BaseWriter):
    def __init__(self, output_file):
        self.colors = dict(
            A="green",
            B="yellow",
            C="blue",
            D="red",
            E="green",
            F="yellow",
            G="blue",
            H="red",
        )
    def standings(self, league_table, league):
        """ Prints the league standings in a pretty way """
        click.secho("-"*100, fg="green", bold=True)
        click.secho("%-2s  %-5s %-25s %-10s %-10s %-11s %-11s %-10s" %
                    ("GP", "POS", "CLUB", "PLAYED",  "GOALS", "GOAL LOSS", "GOAL DIFF","POINTS"))
        click.secho("-"*100, fg="green", bold=True)

        for key in sorted(league_table["standings"].keys()):
            for team in league_table["standings"][key]:
                if team["goalDifference"] >= 0:
                    team["goalDifference"] = ' ' + str(team["goalDifference"])
                team_str = (u"{group:<3} {rank:<5} {team:<25} "
                            u"{playedGames:<10} {goals:<10} {goalsAgainst:<10}"
                            u" {goalDifference:<12} {points}").format(**team)
                click.secho(team_str, bold=True, fg=self.colors[team['group']])

        click.secho("-"*100, fg="green", bold=True)

class Gjson(BaseWriter):
    def __init__(self, output_file):
        super(Gjson, self).__init__(output_file)

    def generate_output(self, result):
        click.echo(json.dumps(result, indent=4, separators=(',', ': '),
                   ensure_ascii=False))

    def standings(self, league_table, league):
        self.generate_output(league_table)

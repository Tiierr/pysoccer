# PySoccer - a CLI for all european football data.

![][badge-author] ![][badge-build] ![][badge-version] ![][badge-python] ![][badge-license]

[中文版][readme-zh]

## Introduction

PySoccer is a CLI that get specific football data. Includes:

- competitions
- leagues
- teams
- players
- standings
- fixtures

## Preparation

Get a [API Key][football-data-api-key] and activate it.

## Install

### Using pip

```
sudo pip install pysoccer
```

Set your API key in an environment variable SOCCER_CLI_API_TOKEN

For example:

```
export SOCCER_CLI_API_TOKEN="<YOUR_API_TOKEN>"
```

Note:

Only testing on Linux.


## Usage

### Get all competitions for current season

```
soccer --competition
```

![][competitions]

### Get all competitions for a season

```
soccer --competition --season 2015
```

![][competitions-season]

### Get all teams for a league

```
soccer --teams --league PD
```
![][teams]

### Get all players for a team

```
soccer --players --team FCB
```
![][players]

### Get standings for a league (mini)

```
soccer --standings --league PD
```

![][standings]

### Get standings for a league (full)

```
soccer --standings --league PD --fs
```

![][full-standings]

### Get all fixtures for next 7 days

```
soccer --fixtures
```

![][fixtures-default]


### Get all fixtures for next 3 days

```
soccer --fixtures --tf 3
```

![][fixtures-next]

### Get all fixtures for previous 3 days

```
soccer --fixtures --tf -3
```

![][fixtures-previous]


### Get all fixtures for a league

```
soccer --fixtures --league PD
```

![][fixtures-league]


### Get all fixtures for a league of a specific macth day

```
soccer --fixtures --league PD --md 33
```

![][fixtures-league-md]


### Get all fixtures for a league of a specific macth day (next 2 days)

```
soccer --fixtures --league PD --md 33 -tf 2
```

![][fixtures-league-md-tf]

### Get historical fixtures for two team (default=10)

```
soccer --fixtures --id 153722
```

![][fixtures-two-teams]

### Get historical fixtures for two team (specific numbers)

```
soccer --fixtures --id 153722 --h2h 30
```

![][fixtures-two-teams-h2h]


## Output format

- `--stdout`: standard out format(default)
- `--fs`: only for all standings data(except group game)
- `--gs`: only for group game standings data
- `--json`: json format(mini)
- `--fjson`: json format(full)
- `--gjson`: json format(only for group game and get standings data)
- `-o`: only for `--json`, `--fjson`, `--gjson`, save data.

## Contribution

- Fork me
- Create a new branch from dev branch
- Add your code, comment, document and meaningful commit message
- Add yourself to CONTRIBUTION.md and describe your work
- PR to dev branch

Thanks all contributors!

You can see a list of contributors in [CONTRIBUTIONS.md][contributors].

## Acknowledgements

- Thanks Football-Data and her developers
- Thanks Soccer-cli and her developers
- Thanks Python language
- Thanks Atom and her developers
- Thanks Open Source

## License

All code of Distance system are open source, based on MIT license.

See [LICENSE][license].

[readme-zh]: https://github.com/RayYu03/pysoccer/blob/master/README.zh.md

[badge-author]: https://img.shields.io/badge/Author-RayYu03-blue.svg
[badge-build]: https://img.shields.io/badge/build-passing-brightgreen.svg
[badge-version]: https://img.shields.io/badge/version-0.0.1-blue.svg
[badge-license]: https://img.shields.io/badge/license-MIT-blue.svg
[badge-python]: https://img.shields.io/badge/python-3.5%2C%203.6-blue.svg

[football-data-api-key]: http://api.football-data.org/client/register

[competitions]: http://oospx4z42.bkt.clouddn.com/competition.png
[competitions-season]: http://oospx4z42.bkt.clouddn.com/competition_by_season.png
[teams]: http://oospx4z42.bkt.clouddn.com/teams.png
[players]: http://oospx4z42.bkt.clouddn.com/players.png
[standings]: http://oospx4z42.bkt.clouddn.com/standings.png
[full-standings]: http://oospx4z42.bkt.clouddn.com/full-standings.png
[fixtures-default]: http://oospx4z42.bkt.clouddn.com/fixtures.png
[fixtures-next]: http://oospx4z42.bkt.clouddn.com/next3.png
[fixtures-previous]: http://oospx4z42.bkt.clouddn.com/previous3.png
[fixtures-league]: http://oospx4z42.bkt.clouddn.com/league_fixtures.png
[fixtures-league-md]: http://oospx4z42.bkt.clouddn.com/md.png
[fixtures-league-md-tf]: http://oospx4z42.bkt.clouddn.com/md_tf.png
[fixtures-two-teams]: http://oospx4z42.bkt.clouddn.com/twoteam.png
[fixtures-two-teams-h2h]: http://oospx4z42.bkt.clouddn.com/h2h.png

[contributors]: https://github.com/RayYu03/pysoccer/blob/master/CONTRIBUTIONS.md

[license]: https://github.com/RayYu03/pysoccer/blob/master/LICENSE

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

[competitions]: http://ww1.sinaimg.cn/large/647dc635ly1fevdawerjbj21150ilq6p.jpg
[competitions-season]: http://ww1.sinaimg.cn/large/647dc635ly1fevdavn2naj20yk0cz40z.jpg
[teams]: http://ww1.sinaimg.cn/large/647dc635ly1fevdavio1uj20yx0ie77t.jpg
[players]: http://ws1.sinaimg.cn/large/647dc635ly1fevc6z0lzbj218o0jnjxf.jpg
[standings]: http://ws1.sinaimg.cn/large/647dc635ly1fevc774gsbj20wk0hiju3.jpg
[full-standings]: http://ws1.sinaimg.cn/large/647dc635ly1fevc7hpv9rj217z0hogp6.jpg
[fixtures-default]: http://ws1.sinaimg.cn/large/647dc635ly1fevc7xs7mfj21840opk1k.jpg
[fixtures-next]: http://ws1.sinaimg.cn/large/647dc635ly1fevc8c5aruj217w0ks46u.jpg
[fixtures-previous]: http://ws1.sinaimg.cn/large/647dc635ly1fevc8mxv3gj218c0ivtfw.jpg
[fixtures-league]: http://ws1.sinaimg.cn/large/647dc635ly1fevc912nlkj21850o4n7a.jpg
[fixtures-league-md]: http://ws1.sinaimg.cn/large/647dc635ly1fevc9ayqrmj218g09y41p.jpg
[fixtures-league-md-tf]: http://ws1.sinaimg.cn/large/647dc635ly1fevc9pe8h5j218708vtbc.jpg
[fixtures-two-teams]: http://ws1.sinaimg.cn/large/647dc635ly1fevca436tij21890c9n0o.jpg
[fixtures-two-teams-h2h]: http://ws1.sinaimg.cn/large/647dc635ly1fevcadcoz7j218g0pkqci.jpg

[contributors]: https://github.com/RayYu03/pysoccer/blob/master/CONTRIBUTIONS.md

[license]: https://github.com/RayYu03/pysoccer/blob/master/LICENSE
aster/LICENSE

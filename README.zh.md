# PySoccer - 一个欧洲足球数据的命令行界面程序。

![][badge-author] ![][badge-build] ![][badge-version] ![][badge-python] ![][badge-license]

[English][readme]

## 简介

PySoccer 是一个获取欧洲一个欧洲足球数据的命令行界面程序。她包括:

- 赛事(competitions)
- 联赛(leagues)
- 球队(teams)
- 球员(players)
- 排名(standings)
- 赛程(fixtures)

## 准备工作

获取[API Key][football-data-api-key] 并激活。

## 安装

### 使用 pip

```
sudo pip install pysoccer
```

将你的 API key 设置为环境变量。

```
export SOCCER_CLI_API_TOKEN="<YOUR_API_TOKEN>"
```

注意:

本程序仅在 Linux 下测试可以正常使用。欢迎其他平台的同学使用并反馈是否正常工作。


## 用法

### 获取当前赛季的所有联赛

```
soccer --competition
```

![][competitions]

### 获取指定赛季的所有联赛

```
soccer --competition --season 2015
```

![][competitions-season]

### 获取指定联赛的所有球队

```
soccer --teams --league PD
```
![][teams]

### 获取指定球队的所有球员

```
soccer --players --team FCB
```
![][players]

### 获取联赛排名(简易版)

```
soccer --standings --league PD
```

![][standings]

### 获取联赛排名(完整版)

```
soccer --standings --league PD --fs
```

![][full-standings]

### 获取赛程（缺省为未来七天）

```
soccer --fixtures
```

![][fixtures-default]


### 获取未来三天的赛程

```
soccer --fixtures --tf 3
```

![][fixtures-next]

### 获取过去三天的赛程

```
soccer --fixtures --tf -3
```

![][fixtures-previous]


### 获取指定联赛的赛程

```
soccer --fixtures --league PD
```

![][fixtures-league]


### 获取指定联赛指定比赛日的赛程

```
soccer --fixtures --league PD --md 33
```

![][fixtures-league-md]


### 获取指定联赛指定比赛日指定时间的赛程

```
soccer --fixtures --league PD --md 33 -tf 2
```

![][fixtures-league-md-tf]

### 获取指定两只球队的历史赛程（缺省为10次）

```
soccer --fixtures --id 153722
```

![][fixtures-two-teams]

### 获取指定两只球队指定次数的历史赛程

```
soccer --fixtures --id 153722 --h2h 30
```

![][fixtures-two-teams-h2h]


## 输出格式

- `--stdout`: 标准输出格式（缺省）
- `--fs`: 仅用于获取联赛排名（不包括小组赛）
- `--gs`: 仅用于获取小组赛形式的联赛排名
- `--json`: json 格式（简易）
- `--fjson`: json 格式（完整）
- `--gjson`: json 格式（仅用于获取小组赛的排名数据）
- `-o`: 仅用于将 `--json`, `--fjson`, `--gjson` 形式的json数据保存为文件。

## 协助开发

- Fork
- 从 dev 分支新建一个分支
- 写代码，注释和文档，并使用有意义的 commit message 提交
- 将自己加入 CONTRIBUTIONS.md，并且描述你做了什么
- PR 到 dev 分支

在 [CONTRIBUTIONS.md][contributors] 里可以看到贡献者名单。


## 致谢

- 感谢 Football-Data 及其开发团队
- 感谢 Soccer-CLI 及其开发团队
- 感谢 Atom 及其开发团队
- 感谢 Python 语言
- 感谢开源精神

## License


PySoccer 项目的所有代码均基于 MIT 协议开源。

详见 [LICENSE][license] 文件。

[readme]: https://github.com/RayYu03/pysoccer/blob/master/README.md

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

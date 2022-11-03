import os
import re
from operator import itemgetter
from typing import Dict, List
from urllib.parse import urljoin

import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from requesting_urls import get_html
from example_plot import plot_NBA_player_statistics
## --- Task 8, 9 and 10 --- ##

try:
    import requests_cache
except ImportError:
    print("install requests_cache to improve performance")
    pass
else:
    requests_cache.install_cache()

base_url = "https://en.wikipedia.org"


def find_best_players(url: str) -> None:
    """Find the best players in the semifinals of the nba.

    This is the top 3 scorers from every team in semifinals.
    Displays plot over points, assists, rebounds

    arguments:
        - html (str) : html string from wiki basketball
    returns:
        - None
    """
    # gets the teams
    teams = get_teams(url)
    # assert len(teams) == 8

    # Gets the player for every team and stores in dict (get_players)
    all_players = {}
    for team in teams:
        team_url = team["url"]
        players = get_players(team_url)
        all_players[team["name"]] = players

    # get player statistics for each player,
    # using get_player_stats
    for team, players in all_players.items():
        for player in players:
            stats = get_player_stats(player["url"], team)
            player.update(stats)

    # at this point, we should have a dict of the form:
    # {
    #     "team name": [
    #         {
    #             "name": "player name",
    #             "url": "https://player_url",
    #             # added by get_player_stats
    #             "points": 5,
    #             "assists": 1.2,
    #             # ...,
    #         },
    #     ]
    # }

    # Select top 3 for each team by points:
    best = {}
    best_a = {}
    best_r = {}
    for team, players in all_players.items():
        # Sort and extract top 3 based on points
        top_apg = 0
        second_apg = 0
        third_apg = 0

        top_rpg = 0
        second_rpg = 0
        third_rpg = 0

        top_ppg = 0
        second_ppg = 0
        third_ppg = 0
        f_a = 1
        f_r = 1
        f_p = 1
        s_a = 1
        s_r = 1
        s_p = 1
        t_a = 1
        t_r = 1
        t_p = 1

        for player in players:
            try:
                apg = player["assists"]
                ppg = player["points"]
                rpg = player["rebounds"]
            except KeyError:
                continue                    # The player does not have stats recorded for this season.
            # if p_apg > first_apg:
            #     top_apg = p_apg
            #     top_a = player["name"]
            #     continue
            #
            # if p_rpg > first_rpg:
            #     top_rpg = p_rpg
            #     top_r = player["name"]
            #     continue
            #
            # if p_ppg > first_ppg:
            #     top_ppg = p_ppg
            #     top_p = player["name"]
            #     continue

            if rpg > third_rpg:
                if rpg > second_rpg:
                    if rpg > top_rpg:
                        top_rpg = rpg
                        f_r = player["name"]

                    else:
                        second_rpg = rpg
                        s_r = player["name"]

                else:
                    third_rpg = rpg
                    t_r = player["name"]

            if apg > third_apg:
                if apg > second_apg:
                    if apg > top_apg:
                        top_apg = apg
                        f_a = player["name"]

                    else:
                        second_apg = apg
                        s_a = player["name"]

                else:
                    third_apg = apg
                    f_a = player["name"]

            if ppg > third_ppg:
                if ppg > second_ppg:
                    if ppg > top_ppg:
                        top_ppg = ppg
                        f_p = player["name"]

                    else:
                        second_ppg = ppg
                        s_p = player["name"]

                else:
                    third_ppg = ppg
                    t_p = player["name"]



        best[team] = [{"name":f_p, "points":top_ppg},
         {"name":s_p, "points":second_ppg}, {"name":t_p, "points":third_ppg}]
        best_a[team] = [{"name":f_a, "points":top_apg},
         {"name":s_a, "points":second_apg}, {"name":t_a, "points":third_apg}]
        best_r[team] = [{"name":f_r, "points":top_rpg},
          {"name":s_r, "points":second_rpg}, {"name":t_r, "points":third_rpg}]


    #plot_best(best, p=True)
    plot_best(best_a, a=True)
    plot_best(best_r, r=True)


def plot_best(best: Dict[str, List[Dict]], stat: str = "points", p = False, a = False, r = False) -> None:
    """Plots a single stat for the top 3 players from every team.

    Arguments:
        best (dict) : dict with the top 3 players from every team
            has the form:

            {
                "team name": [
                    {
                        "name": "player name",
                        "points": 5,
                        ...
                    },
                ],
            }

            where the _keys_ are the team name,
            and the _values_ are lists of length 3,
            containing dictionaries about each player,
            with their name and stats.

        stat (str) : [points | assists | rebounds] which stat to plot.
            Should be a key in the player info dictionary.
    """
    stats_dir = "NBA_player_statistics"
    all_names = []
    count_so_far = 0
    fig = plt.figure()
    for team, players in best.items():
        points = []
        names = []
        for player in players:

            names.append(player["name"])
            if p:
                points.append(player["points"])
            if a:
                points.append(player["points"])
            if r:
                points.append(player["points"])

        all_names.extend(names)
        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team's players points,
        # with the team name as the label
        bars = plt.bar(x, points, label=team)
        # add the value as text on the bars
        plt.bar_label(bars)
    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    # add the legend with the colors  for each team
    plt.legend(loc="best")
    # turn off gridlines
    plt.grid(False)
    # set the title

    #fig.subplots_adjust(bottom="spacing")
    if p:
        plt.title("points per game")
        fig.tight_layout()
        plt.savefig("NBA_player_statistics/points.png")

    if a:
        plt.title("assists per game")
        fig.tight_layout()
        plt.savefig("NBA_player_statistics/assists.png")

    if r:
        plt.title("rebounds per game")
        fig.tight_layout()
        plt.savefig("NBA_player_statistics/rebounds.png")


def get_teams(url: str) -> list:
    """Extracts all the teams that were in the semi finals in nba

    arguments:
        - url (str) : url of the nba finals wikipedia page
    returns:
        teams (list) : list with all teams
            Each team is a dictionary of {'name': team name, 'url': team page
    """
    # Get the table
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Bracket").find_next("table")

    # find all rows in table
    rows = table.find_all("tr")
    rows = rows[2:]
    # maybe useful: identify cells that look like 'E1' or 'W5', etc.
    seed_pattern = re.compile(r"^[EW][1-8]$")

    # lots of ways to do this,
    # but one way is to build a set of team names in the semifinal
    # and a dict of {team name: team url}

    team_links = {}         # dict of team name: team url
    in_semifinal = set()    # set of teams in the semifinal

    # Loop over every row and extract teams from semi finals
    # also locate the links tot he team pages from the First Round column
    for row in rows:
        cols = row.find_all("td")
        # useful for showing structure
        # print([c.get_text(strip=True) for c in cols])

        # TODO:
        # 1. if First Round column, record team link from `a` tag
        # 2. if semifinal column, record team name

        # quarterfinal, E1/W8 is in column 1
        # team name, link is in column 2
        if len(cols) >= 3 and seed_pattern.match(cols[1].get_text(strip=True)):
            team_col = cols[2]
            a = team_col.find("a")
            team_links[team_col.get_text(strip=True)] = urljoin(base_url, a["href"])

        elif len(cols) >= 4 and seed_pattern.match(cols[2].get_text(strip=True)):
            team_col = cols[3]
            in_semifinal.add(team_col.get_text(strip=True))

        elif len(cols) >= 5 and seed_pattern.match(cols[3].get_text(strip=True)):
            team_col = cols[4]
            in_semifinal.add(team_col.get_text(strip=True))

    # return list of dicts (there will be 8):
    # [
    #     {
    #         "name": "team name",
    #         "url": "https://team url",
    #     }
    # ]

    assert len(in_semifinal) == 8
    return [
        {
            "name": team_name.rstrip("*"),
            "url": team_links[team_name],
        }
        for team_name in in_semifinal
    ]


def get_players(team_url: str) -> list:
    """Gets all the players from a team that were in the roster for semi finals
    arguments:
        team_url (str) : the url for the team
    returns:
        player_infos (list) : list of player info dictionaries
            with form: {'name': player name, 'url': player wikipedia page url}
    """
    print(f"Finding players in {team_url}")

    # Get the table
    html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Roster").find_next("table", {"class": "sortable"})
    headings = table.find_all("th")
    for j, head in enumerate(headings):
        head = head.text
        if head == "Name":
            name_column_indx = j

    players = []
    # Loop over every row and get the names from roster
    rows = table.find_all("tr")
    rows = rows[1:]
    wiki_pat = re.compile("(?<=href=\")\/wiki\/.*?(?=\")")
    base_url = "https://en.wikipedia.org"
    for row in rows:
        # Get the columns
        cols = row.find_all("td")[name_column_indx]
        name = cols.text.strip()
        wiki = re.search(wiki_pat, str(cols)).group(0)
        player_url = "".join((base_url, wiki))
        # find name links (a tags)
        # and add to players a dict with
        # {'name':, 'url':}
        players.append(
        {"name": name, "url": player_url}
        )

    # return list of players

    return players


def get_player_stats(player_url: str, team: str) -> dict:
    """Gets the player stats for a player in a given team for the 2021-22 Regular season
    arguments:
        player_url (str) : url for the wiki page of player
        team (str) : the name of the team the player plays for
    returns:
        stats (dict) : dictionary with the keys (at least): points, assists, and rebounds keys
    """
    print(f"Fetching stats for player in {player_url}")

    # Get the table with stats
    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        table = soup.find(id="Regular_season").find_next("table", {"class": "wikitable sortable"})
    except AttributeError:
        table = soup.find(id="NBA").find_next("table", {"class": "wikitable sortable"})             # For players only having one season
    headings = table.find_all("th")
    season = "2021–22"                          # NOTE: Wikipedia use '–' and not regular dash '-' for some dumb reason.
    for j, head in enumerate(headings):
        head = head.text.strip()
        if head == "Year":
            year_indx = j
            continue
        if head == "Team":
            team_indx = j
            continue
        if head == "RPG":
            rpg_indx = j
            continue
        if head == "APG":
            apg_indx = j
            continue
        if head == "PPG":
            ppg_indx = j
            continue


    stats = {}

    rows = table.find_all("tr")
    rows = rows[1:]                 # Removes header row

    # Loop over rows and extract the stats
    for row in rows:
        cols = row.find_all("td")
        #print("team:", cols[team_indx].text.strip(), "season:", cols[year_indx].text.strip())
        year_col = cols[year_indx]
        if year_col.text.strip().strip("†") == season:
            team_col = cols[team_indx]
            # Check correct team (some players change team within season
            if team_col.text.strip() == team:
                rpg = float(cols[rpg_indx].text.strip().strip("*"))
                apg = float(cols[apg_indx].text.strip().strip("*"))
                ppg = float(cols[ppg_indx].text.strip().strip("*"))
                # load stats from columns
                # keys should be 'points', 'assists', etc.
                stats["points"] = ppg
                stats["assists"] = apg
                stats["rebounds"] = rpg

    return stats


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2022_NBA_playoffs"
    find_best_players(url)
    # s1 =get_players("https://en.wikipedia.org/wiki/2021%E2%80%9322_Miami_Heat_season")
    # s2 = get_players("https://en.wikipedia.org/wiki/2021–22_Philadelphia_76ers_season")
    # sts = get_player_stats("https://en.wikipedia.org/wiki/Sandro_Mamukelashvili", "Milwaukee")
    # s = get_players("https://en.wikipedia.org/wiki/2021%E2%80%9322_Memphis_Grizzlies_season")
    # sts = get_player_stats("https://en.wikipedia.org/wiki/Quinndary_Weatherspoon", "Golden State")
    # breakpoint()

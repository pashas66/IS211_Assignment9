#IS211 Assignment-9, Part I

'''
1. Go to the CBS NFL Stats webpage, located at http://www.cbssports.com/nfl/stats
2. Under “PLAYER STATISTICS”, click on the Touchdowns links
3. Change the drop down to regular
4. Write a script called “football_stats.py” that will:
    a) load this URL
    b) parse it using BeautiulSoup,
    c) and output the list of top 20 players,including the player’s position, team and total number of touchdowns
'''
#importing the required libraries:
import sys
import urllib.request as request
import urllib.error
from bs4 import BeautifulSoup as bs

def get_top_20_td(html):
    rows = html.findAll('tr', attrs={'class': 'TableBase-bodyTr'})[:20]
    tdstats=[]
    for row in rows:
        player_name = row.findAll('span', attrs={'class': 'CellPlayerName--long'})[0].text.split('\n\n')[1].replace('\n','').strip()
        player_position = row.findAll('span', attrs={'class': 'CellPlayerName-position'})[0].text.replace('\n','').strip()
        player_team = row.findAll('span', attrs={'class': 'CellPlayerName-team'})[0].text.replace('\n','').strip()
        player_td = row.contents[16].text.replace('\n','').strip()
        tdstats.append([player_name, player_position, player_team, player_td])
    return tdstats


#print statements for the top 20 players:
def print_td(tdstats):
    print("\nNFL Top 20 Touchdown Players' Stats:\n")
    #print statements for players position, team, and the total # of touchdowns
    print("{:<20}{:<10}{:<5}{:>4}".format('Player', 'Position', 'Team', 'Touchdowns\n'))
    for stat in tdstats:
        print("{:<20}{:<10}{:<5}{:>4}".format(stat[0], stat[1], stat[2], stat[3]))


def get_html(url):
    response = request.urlopen(url).read()
    #here we are parsing using BeautiulSoup as "bs"
    html = bs(response, 'lxml')
    return html


def main():
    #here we are loading the url 
    url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending'
    html = get_html(url)
    tdstats = get_top_20_td(html)
    print_td(tdstats)
    sys.exit()

if __name__ == '__main__':
    main() #calling the main function 

    #end of the code
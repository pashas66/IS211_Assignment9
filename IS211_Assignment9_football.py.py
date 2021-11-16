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

import urllib.request as urllib2
from bs4 import BeautifulSoup
    #here we are loading the url 
html = urllib2.urlopen('https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending')
soup = BeautifulSoup(html, 'html.parser')  #here we are parsing using BeautiulSoup 


def main():
    t_rows = soup.findAll('tr', class_="TableBase-bodyTr")
    counter = 0

    #print statements for the top 20 players:
    print("Here are the 20 players currently with the most touchdowns:")
    
    for row in t_rows:
        td = row.find_all("td")
        name = td[0].find('a').text.strip()
        position = td[0].find("span", attrs={'class': "CellPlayerName-position"}).text.strip()
        team = td[0].find("span", attrs={'class': "CellPlayerName-team"}).text.strip()
        touchdown = td[8].text.strip()
        counter += 1
            #print statements for players position, team, and the total # of touchdowns
        print(f"Name = {name} | position = {position} | team {team} | TDs = {touchdown}")
        if counter >= 20:
            break


if __name__ == '__main__':
    main()  #calling the main function 

    #end of the code
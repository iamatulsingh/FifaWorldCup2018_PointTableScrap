#  Developer -   Atul Singh
#  Github    -   https://github.com/iamatulsingh
#  Telegram  -   https://t.me/developeratul
#  @license  -   Code and contributions have 'MIT License'
#                More details: LICENSE
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software with proper credit to original author.





from bs4 import BeautifulSoup as soup
from requests import get

url = 'http://www.espn.in/football/table/_/league/fifa.world'

#opening the connection and grabbing the page
response = get(url)

#html parser
html = soup(response.text, "html.parser")

#fetch html table using class name that contains point table
html_table = html.select('.has-team-logos')

#abberviatios
print 'GP  :  Games Played'
print 'W   :  Win'
print 'D   :  Draw'
print 'L   :  Losses'
print 'F   :  Goals For'
print 'A   :  Goals Against'
print 'GD  :  Goal Difference'
print 'P   :  Points'

#fetch all data
for thead in html_table:
    heads = thead.findAll('thead', attrs = {'class':'standings-categories'})
    all_groups = thead.findAll('tr', attrs = {'class':'standings-row'})
    groups = []
    categories = []
    count_categories = 0

    #fetch categories of game
    for head in heads:
        count_group_name = 0
        for titles in head:
            count_group_name = count_group_name + 1
            count_categories = count_categories + 1
            if count_group_name == 1:
                groups.append(titles.text)
            else:
                if(count_categories > 1 and count_categories <= 9):
                    categories.append(titles.text)

    GROUPS_MAX_LENGTH = len(groups)
    GROUPS_COUNTER = 9
    DIVIDE_COUNTER = 0
    
    for group in all_groups:
        print ''
        if DIVIDE_COUNTER == 0:
            print '\n\n'
            GROUPS_COUNTER = GROUPS_COUNTER - 1
            if GROUPS_COUNTER >= 1:
                print '\t' + groups[GROUPS_MAX_LENGTH - GROUPS_COUNTER],
            for category in categories:
                print '\t' + category,
            print '\n'
        elif DIVIDE_COUNTER % 4 == 0:
            print '\n\n'
            GROUPS_COUNTER = GROUPS_COUNTER - 1
            if GROUPS_COUNTER >= 1:
                print '\t' + groups[GROUPS_MAX_LENGTH - GROUPS_COUNTER],
            for category in categories:
                print '\t' + category,
            print '\n'
        for teams in group:
            if len(teams) > 1:
                for team_sequence_numbers in teams.findAll('span',attrs={'class','number'}):
                    print team_sequence_numbers.text + '',
                for team_names in teams.findAll('span', attrs={'class','team-names'}):
                    print team_names.text + '',
                    #use spacing for better view in console using name length
                    #and give same space to every team name
                    NAME_MAX_LENGTH = 12
                    length_of_team_name = len(team_names.text)
                    diff = NAME_MAX_LENGTH - length_of_team_name
                    while diff > 0:
                        #giving space here
                        print '',
                        diff = diff - 1
                for team_abbr in teams.findAll('abbr'):
                    print '(' + team_abbr.text + ') ',
            else:
                print '\t' + teams.text + '   ',
                
        DIVIDE_COUNTER = DIVIDE_COUNTER + 1

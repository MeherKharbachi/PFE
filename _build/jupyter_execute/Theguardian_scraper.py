#!/usr/bin/env python
# coding: utf-8

# # The Guardian Scraper
# 
# > Scraping Premier League Previews from the Guardian.

# To reach the aim of our project, we have begun the first task, which is to collect football experts' comments and data from English Premier League matches.
# <br>For this task, we will use match previews from "The Guardian." It goes back far enough, from 2009 to today, to allow us to integrate deep neural networks.
# <br>Indeed, "The Guardian's" football experts publish previews every week, usually two or three days before the matches.
# <br>In this regard, we began by creating a data extraction tool that will allow us to extract this information on a regular basis.
# <br>The information to be extracted is as follows:
# 
# - The names of the competing teams.
# - The date of the game
# - The identity of the referee
# - The stadium's name
# - Sports odds that will be converted to decimal format
# - The football expert's text
# - The text's author.
# 

# ## A preliminary examination of the Guardian's website

# 
#     
# |            Issues                 |          Solutions          |
# |------------------------------     |-------------------|
# |   4 possible formats for previews(old format, new format,Cup's format and a particular format) |Select the appropriate html tags|
# |   Preview titles are not the same ( we can find Squad Sheets or match preview)|Pick only the names of the teams and eliminate the rest|
# |   The date of the match is not always available |Pick the preview date|
# |   The order of the elements and labels are not the same |Using regex patterns to get information|
# |   Missing values for betting odds |We treat the general case separately and we set up specific regex patterns for these particular cases|
# |   Odds format is different|We treat the general case separately and we set up specific regex patterns for these particular cases|
# |   We can find non-numeric values for Odds like (Evens,evens,Eve,odds-on)|Replace evens by 1-1|
# |   There are some previews that don't have author and text|For previews that have no text, we put None (not available)|
# |   The existence of previews for the FA CUP,Carabao Cup,Champions league,World Cup|Filter previews by checking if the match exists in "Opta" database, and pick only Premier League match |
# |   We are not sure if the names of the teams are the same as the ones in Opta|Set up a dictionary or check manually to map teams to their IDs|
# |When we send many requests, the guardian server blocks your IP address, which is interpreted as a DDOS attack|Do a sleep of a random x seconds between requests or change IP address and work with rotating proxy|
# 

# <b>The guardian</b> previews are spread across several pages, so our extraction tool will go through all of them, extracting the previews as it goes.
# <br>Indeed, the scraper extracts information from <b>Premier League</b> match previews using two methods:
# <br>The first method is to use the api provided by <b>The Guardian's</b> website, by introducing a connection key and a well-parsed portion of the link.
# <br>For example, a link is formatted as https://www.theguardian.com/football/2022/feb/12/newcastle-aston-villa-match-preview-premier-league, <b>the guardian</b> API only requires "football/2022/feb/12/newcastle-aston-villa-match-preview-premier-league." 
# <br>However, this method is not always reliable because the API is not always functional for some previews. So, in this case, our scraper employs its second method, which is the traditional approach of scraping the html format of the pages. 
# <br>We identified some special cases by analyzing the website; there are some changes in form and content, so we attempted to find a set of regular expressions that dealt with generic and special cases in order to locate the various information.
# <br>Following the data extraction stage, information will be normalized and cleaned, and betting odds extracted from the previews will be converted to a decimal format. 
# <br>Then, to ensure that we are only extracting <b>English Premier League</b> matches, we map the extracted preview by its equivalent in a database called <b>Opta</b> by introducing the names of the two opposing teams, the competition id, and the closest game date to the date of the preview. This mapping returns the match id and the date of the game.
# However, <b>Opta</b> is a trustworthy database provided by <b>Opta Sport</b>, the pan-European leader in the supply of sports information data.
# Moreover, prior to this phase, we were unsure of the correspondence between the names of the teams written by <b>the guardian</b> and the names of the teams in <b>Opta</b>. For example, a single team can be referred to in several ways, such as <b>Manchester United, Manchester Utd, Man United, Man Utd</b> and so on.
# <br>To address this issue, we created a dictionary containing the various possible names of <b>103 English teams</b> competing in the first and second divisions. This dataset was created in two ways: the first using <b>Opta</b>, which provides the various team aliases, and the second manually, in which we added other nicknames that were not provided.
# <br>Finally, once the mapping process is done, this information will be gradually stored in a <b>Mongodb</b> database, specifically in a collection called <b>Previews</b>.
# <br>It should be noted that when the scraper is launched, it checks the last date stored in the <b>Previews</b> collection to determine at what level it will stop.
# <br>This scraper has extracted data from 2009 to the present and is <b> operational in a production environment </b>.
# <br>Our package is <b>open source</b> and freely available to all developers on <b>Github</b> and <b>Pypi</b> (default software repository for Python developers to store created Python programming language).

# ## Example of the scraper output

# ![The scraper output!](./images/scraper_output_1.png "scraper output")

# ![The scraper output!](./images/scraper_output_2.png "scraper output")

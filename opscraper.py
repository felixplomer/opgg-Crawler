
import requests
from bs4 import BeautifulSoup
from tkinter import *

def gui():
    UserName = spieler1.get()
    UserName2 = spieler2.get()
    UserName3 = spieler3.get()
    UserName4 = spieler4.get()
    UserName5 = spieler5.get()

    player = [UserName, UserName2, UserName3, UserName4, UserName5]

    master.quit()
    return player


master = Tk()
master.geometry("300x200")


Label(master, text="Spieler 1").grid(row=0)
Label(master, text="Spieler 2").grid(row=1)
Label(master, text="Spieler 3").grid(row=2)
Label(master, text="Spieler 4").grid(row=3)
Label(master, text="Spieler 5").grid(row=4)

spieler1 = Entry(master)
spieler2 = Entry(master)
spieler3 = Entry(master)
spieler4 = Entry(master)
spieler5 = Entry(master)

spieler1.grid(row=0, column=2)
spieler2.grid(row=1, column=2)
spieler3.grid(row=2, column=2)
spieler4.grid(row=3, column=2)
spieler5.grid(row=4, column=2)





Button(master, text='Confirm', command=gui,).grid(row=6, column=2, sticky=W, pady=4)
Button(master, text='Details', command= master.quit,).grid(row=6, column=3, sticky=W, pady=5)

mainloop()


def rang_update(ranks, player):
    master = Tk()
    master.geometry("300x200")


    Label(master, text= player[0] + " : " + ranks[0]).grid(row=0, column = 3)
    Label(master, text= player[1] + " : " + ranks[1]).grid(row=1, column = 3)
    Label(master, text= player[2] + " : " + ranks[2]).grid(row=2, column = 3)
    Label(master, text= player[3] + " : " + ranks[3]).grid(row=3, column = 3)
    Label(master, text= player[4] + " : " + ranks[4]).grid(row=4, column = 3)

    mainloop()





ranks = []
for user in gui():


    URL = "https://euw.op.gg/summoner/userName=" + user
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    # player info
    solo_rank = soup.find("div", class_="TierRank")
    #flex_rank = soup.find("div", class_="sub-tier__rank-tier")

    if solo_rank.text == "\n\t\t\tUnranked\n\t\t":
        solo_rank = soup.find_all("li", class_ = "Item tip")
        for entry in solo_rank:
            if entry.find("b", string="S2020"):
                solo_rank = entry


    ranks.append(solo_rank.text)

    # print(flex_rank.text)
rang_update(ranks, gui())

'''
#Champion Info
URL = "https://euw.op.gg/summoner/champions/userName=" + gui()
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

champions_played_most = soup.find_all("tr", class_ = "Row TopRanker")
champions_played_all = soup.find_all("tr", class_ = "Row")




#for entry in champions_played_most:
    #champion = entry.find("td", class_ = "ChampionName Cell")
    #print(champion.text)
for champ_played in champions_played_all:
    champion = champ_played.find("td", class_ = "ChampionName Cell")
    if champion is not None:
        print(champion.text)
'''



'''
#last 10 games history stats und farm

game_history = soup.find("div", class_ = "GameItemList")
games = game_history.find_all("div", class_ = "GameItemWrap")

for game in games:

    champion = game.find("div", class_ = "ChampionName")
    kills = game.find("span", class_ = "Kill")
    death = game.find("span", class_ = "Death")
    assists = game.find("span", class_ = "Assist")
    farm = game.find("span", class_ = "CS")


    print(champion.text)
    print("CS: ",farm.text)
    print(kills.text, "/", death.text, "/", assists.text)
'''







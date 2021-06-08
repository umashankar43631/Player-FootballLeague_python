class Player:
    def __init__(self, matches, goals, rating, name):
        self.matches = matches
        self.goals = goals
        self.rating = rating
        self.name = name
    def playerDetails(self):
        return self.matches, self.goals, self.rating, self.name

class FootballLeague:
    # player list order is 
    # matches, goals, rating, name
    def __init__(self,leagueName,playerList):
        self.leagueName = leagueName
        self.playerList = playerList
    # func1
    def findMaximumPlayerByRating(self):
        rating = self.playerList[0][2]
        bestPlayerDetails = self.playerList[0]
        for i in range(1,len(self.playerList)):
            x = self.playerList[i][2]
            if( x > rating ):
                rating = x
                bestPlayerDetails = self.playerList[i]
        if(rating == None):
            print("No data Found")
            return
        self.getPlayerDetails(bestPlayerDetails)
        return
    def sort(self,player_Goals):
        i = 1
        while(i>=1 and i <len(player_Goals)):
            temp = player_Goals[i]
            j = i-1
            while( j>=0 and player_Goals[j]>temp ):
                player_Goals[j+1] = player_Goals[j]
                j = j-1
            player_Goals[j+1] = temp
            i = i+1
        return player_Goals

    # Func2
    def sortPlayerByGoals(self):
        player_Goals = []
        for i in range(len(self.playerList)):
            player_Goals.append(self.playerList[i][1])
        if not player_Goals:
            print("No data Found")
            return
        self.getGoals(self.sort(player_Goals))
        return
    def getGoals(self,player_Goals):
        for goal in player_Goals:
            print(goal)
    def getPlayerDetails(self,playerDetails):
        for i in playerDetails:
            print(i)


#Driver Code
if __name__ == "__main__":
    # Get the input for how many no of player details you want to enter
    n = int(input())
    # creating empty player_list each 
    player_list = []
    for i in range(n):
        matches = int(input())
        goals = int(input())
        rating = int(input())
        name = input()
        x = Player(matches,goals,rating,name)
        player_list.append(list(x.playerDetails()))
    
    #Creating object
    fl = FootballLeague('ACE',player_list) 
    
    # Finding the best player by rating and printing the player details
    fl.findMaximumPlayerByRating()
    
    # Sorting the players Goals
    fl.sortPlayerByGoals()
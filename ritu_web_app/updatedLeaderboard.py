from django.db import connections
from .models import Leaderboard, Task1Text,Task2Text,Task3Text

class Leaderboards:
    def __init__(self,username):
        self.username=username
    
    def insertDataInLeaderboard(self):
        #checking if the player is already in the leaderboard
        
        #db_cursor=connections['default'].cursor()
        
        findingPlayer=Leaderboard.objects.raw("SELECT id, player_id FROM ritu_web_app_leaderboard WHERE player_id='"+self.username+"'")
        playername=''
        for player in findingPlayer:
            playername=player.player_id
        print(f"Player name is {playername}")
        if (playername==""):
                print("Player didnt exist in leaderboard, creating one")
                #db_cursor=connections['default'].cursor()
                
                #getting points for particular user from task1 table
                task1=Task1Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task1text WHERE player_id='"+self.username+"'")
                getTask1Points=[]
                for task in task1:
                    getTask1Points.append(str(task.earnedPoints))
                
                task1points=float(max(getTask1Points))
                
                print(task1points)
                
                #getting points for particular user from task2 table
                task2=Task2Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task2text WHERE player_id='"+self.username+"'")
                getTask2Points=[]
                for task in task2:
                    getTask2Points.append(str(task.earnedPoints))
                
                task2points=float(max(getTask2Points))
                
                print(task2points)
                
                #getting points for particular user from task3 table
                task3=Task3Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task3text WHERE player_id='"+self.username+"'")
                getTask3Points=[]
                for task in task3:
                    getTask3Points.append(str(task.earnedPoints))
                
                task3points=float(max(getTask3Points))
                
                print(task3points)
                
                leaderboardPoint=(task1points+task2points+task3points)
                print(f"Leaderboard Point: {leaderboardPoint}")
                #db_cursor.execute("INSERT INTO ritu_web_app_leaderboard(player_id,points)VALUES('"+self.username+"','"++"')")
        else:
            print("player exists")           
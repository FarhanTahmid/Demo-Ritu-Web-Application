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
                
                task1=Task1Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task1text WHERE player_id='"+self.username+"'")
                task1points=0.0
                for task in task1:
                    if(task1points>task.earnedPoints):
                        task1points=float(task.earnedPoints)
                print(f"task point: {task1points}")
                #db_cursor.execute("INSERT INTO ritu_web_app_leaderboard(player_id,points)VALUES('"+self.username+"','"++"')")
        else:
            print("player exists")           
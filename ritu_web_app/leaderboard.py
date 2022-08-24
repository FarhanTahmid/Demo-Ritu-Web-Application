
from lib2to3.pytree import Leaf
from django.db import connections
from .models import Leaderboard,Task1Text,Task2Text,Task3Text

class Leaderboard:
    def __init__(self,username):
        self.username=username
    
    def insertDataInLeaderboard(self):
        #checking if the player is already in the leaderboard
        db_cursor=connections['default'].cursor()
        findingPlayer=Leaderboard.objects.raw("SELECT player_id FROM ritu_web_app_leaderboard WHERE player_id='"+self.username+"'")
        
        for player in findingPlayer:
            if (player.player_id)=='':
                print("Player didnt exist in leaderboard, creating one")
                db_cursor=connections['default'].cursor()
                task1=Task1Text.objects.raw("SELECT earnedPoints FROM ritu_web_app_leaderboard WHERE player_id='"+self.username+"'")
                for task1 in task1:
                    print(task1.earnedPoints)
                #db_cursor.execute("INSERT INTO ritu_web_app_leaderboard(player_id,points)VALUES('"+self.username+"','"++"')")
            
from .models import Players
class Player:
    def __init__(self,player):
        self.player=player
    def getInfo(self):
        playerData=Players.objects.raw("SELECT * FROM ritu_web_app_players WHERE username='"+self.player+"'")
        print(playerData)
        
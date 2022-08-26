from audioop import add
from .models import Players
class Player:
    def __init__(self,player):
        self.player=player
    def getInfo(self):
        playerData=Players.objects.raw("SELECT * FROM ritu_web_app_players WHERE username='"+self.player+"'")
        
        username=''
        name=''
        mobileNum=''
        email=''
        address=''
        picture=''
        
        for data in playerData:
            username=data.username
            name=data.fullname
            mobileNum=data.mobileNumber
            email=data.email
            address=data.address
            picture=data.picture
        data={
            'username':username,
            'name':name,
            'mobileNum':mobileNum,
            'email':email,
            'address':address,
            'picture':picture
        }    
        return data
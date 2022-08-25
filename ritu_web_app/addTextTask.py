from django.db import connections

class TextUrl: 

    def __init__(self,points='',text="", player="") :
        self.text=text
        # self.time_added=time_added
        self.player=player
        self.points=points
    
    def addTextUrl_1(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO ritu_web_app_task1text(text,player_id,earnedPoints) VALUES('"+self.text+"','"+self.player+"','"+self.points+"')")
        
    def addTextUrl_2(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO ritu_web_app_task2text(text,player_id,earnedPoints) VALUES('"+self.text+"','"+self.player+"','"+self.points+"')")
        
    def addTextUrl_3(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO ritu_web_app_task3text(text,player_id,earnedPoints) VALUES('"+self.text+"','"+self.player+"','"+self.points+"')")
        
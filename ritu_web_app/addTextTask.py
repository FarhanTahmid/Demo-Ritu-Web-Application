from django.db import connections

class TextUrl: 

    def __init__(self,text="", player="") :
        self.text=text
        # self.time_added=time_added
        self.player=player
    
    def addTextUrl_1(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO ritu_web_app_task1text(text,player) VALUES('"+self.text+"','"+self.player+"')")
        
    # def addTextUrl_2(self):
    #     db_cursor=connections['default'].cursor()
    #     db_cursor.execute("INSERT INTO ritu_web_app_task2text(text,time_added,player) VALUES('"+self.text+"','"+self.time_added+"','"+self.player+"')")
        
    # def addTextUrl_3(self):
    #     db_cursor=connections['default'].cursor()
    #     db_cursor.execute("INSERT INTO ritu_web_app_task3text(text,time_added,player) VALUES('"+self.text+"','"+self.time_added+"','"+self.player+"')")
        
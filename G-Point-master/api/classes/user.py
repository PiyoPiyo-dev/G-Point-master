import json
import os
import datetime



class getUserModel:
    def __init__(self, userId):
        with open(f"data/user/{userId}.json", "r") as f:
            self.rawJson= json.loads(f.read())
            self.userId = str(self.rawJson["userId"])
            self.point = int(self.rawJson["point"])
            self.history = self.rawJson["history"]
            self.prize = self.rawJson["prize"]
    def visit(self, clubId, point):
        return self.add(clubId, point, self.get_nowTime())
    def add(self, clubId, point, timeStamp):
        self.point += point
        self.history += [{"clubId": str(clubId), "point": int(point), "timeStamp": str(timeStamp)}]
        return {"userId":self.userId, "point":self.point, "history":self.history, "prize":self.prize}
    def get_nowTime(self):
        return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')




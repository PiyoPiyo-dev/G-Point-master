import json
import datetime


class getUserModel:
    def __init__(self, userId):
        with open(f"data/user/{userId}.json", "r") as f:
            self.rawJson = json.loads(f.read())
            self.userId = str(self.rawJson["userId"])
            self.point = int(self.rawJson["point"])
            self.history = self.rawJson["history"]
            self.prize = self.rawJson["prize"]

    def visit(self, clubId, point):
        return Save(self.add(clubId, point, self.get_nowTime()))

    def add(self, clubId, point, timeStamp):
        self.point += point
        self.history += [{"clubId": str(clubId),
                          "point": int(point), "timeStamp": str(timeStamp)}]
        return {"userId": self.userId, "point": self.point, "history": self.history, "prize": self.prize}

    def get_nowTime(self):
        return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')


class Save():
    def __init__(self, save_arr):
        self.save_arr = save_arr
        self.userId = str(self.save_arr["userId"])
        self.point = int(self.save_arr["point"])
        self.history = self.save_arr["history"]
        self.prize = self.save_arr["prize"]
        # 二回訪れたかどうかの処理を書く
        is_visited = False

    def save(self):
        # 保存に関する処理(保存しかしない)
        print(self.save_arr)

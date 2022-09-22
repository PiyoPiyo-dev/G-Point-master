import json
import os

class getUserModel:
    def __init__(self, userId):
        with open(f"data/user/{userId}.json", "r") as f:
            self.rawJson= json.loads(f.read())
            self.userId = str(self.rawJson["userId"])
            self.point = int(self.rawJson["point"])
            self.history = self.rawJson["history"]
            self.prize = self.rawJson["prize"]



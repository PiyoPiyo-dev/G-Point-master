import json

class getClubModel:
    def __init__(self, clubId):
        with open(f"data/club/{clubId}.json", "r", encoding='utf-8') as f:
            self.rawJson= json.loads(f.read())
            self.clubId = str(self.rawJson["clubId"])
            self.description = str(self.rawJson["description"])
            self.point = self.rawJson["point"]
            self.type = 0 if len(self.point)==1 else 1 if len(self.point)==0 else 2
            if self.type==0:
                self.point=int(self.point[0])
            #Type:0 通常サークル Type:1 自由入力型サークル Type:2 選択型サークル
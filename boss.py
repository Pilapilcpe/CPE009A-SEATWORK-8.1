from swordsman import swordsman
from archer import archer
from magician import magician

class boss(swordsman, archer, magician):
    def __init__(self, username):
        super().__init__(username)
        self.setStr(10)
        self.setVit(25)
        self.setInt(5)
        self.setHp(self.getHp()+self.getVit())
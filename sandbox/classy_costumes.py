class Monster:
    vampire = {2: 'scary'}
    def werewolf(self):
        print(self)
        return self.vampire[2]

class Blob(Monster):
    vampire = {2: 'night'}
    def __init__(self, ghoul):
        vampire = {2: 'frankenstein'}
        self.witch = ghoul.vampire
        self.witch[3] = self
        self.phrase = self
spooky = Blob(Monster)
another_one = Blob(Monster)




class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Creating objects of the Batsman and Bowler classes and calling the play() method
if __name__ == "__main__":
    batsman = Batsman()
    bowler = Bowler()

    batsman.play()
    bowler.play()
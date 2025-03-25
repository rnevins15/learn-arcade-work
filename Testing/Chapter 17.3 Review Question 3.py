class Monster():
    def __init__(self):
        self.name = ""
        self.health = 100

    def decrease_health(self, lost_health):
        self.health -= lost_health
        print(self.name + "is now at " +  str(self.health) + " health ")
        if(self.health) < 1:
            print("The Monster Dies")


def main():
    gorp = Monster()
    gorp.name = "Gorp"
    gorp.decrease_health(100)

main()
class Cat():


    def __init__(self):
        self.color = ""
        self.name = ""
        self.weight = 0

    def meow(self):
        print(self.name + "  says \"meow\"")

def main():
    my_cat = Cat()
    my_cat.name = "Buttercup"
    my_cat.color = "orange"
    my_cat.weight = 5
    my_cat.meow()


main()


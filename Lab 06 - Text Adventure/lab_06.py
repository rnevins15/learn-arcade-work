class Room:
    def __init__(self):
        # Define the rooms in the house with their descriptions and exits
        self.rooms = {
            'living_room': {
                'description': 'You are in the cozy living room. There is a sofa, a coffee table, and a bookshelf.',
                'exits': {'north': 'kitchen', 'east': 'bathroom'},
                'items': ['remote control']
            },
            'kitchen': {
                'description': 'You are in the kitchen. There are counters, a refrigerator, and a stove.',
                'exits': {'south': 'living_room', 'west': 'dining_room', 'east': 'bedroom'},
                'items': ['key']
            },
            'bathroom': {
                'description': 'You are in a small bathroom. There is a shower, a mirror, and a sink.',
                'exits': {'west': 'living_room'},
                'items': []
            },
            'dining_room': {
                'description': 'You are in the dining room. There is a long table with chairs around it.',
                'exits': {'east': 'kitchen'},
                'items': ['silver spoon']
            },
            'bedroom': {
                'description': 'You are in the bedroom now. There is a large bed in the middle of the room',
                'exits': {'east': 'master_bathroom', 'west': 'kitchen'},
                'items': []
            },
            'master_bathroom': {
                'description': 'You are in the master bathroom. There is a bathtub, a mirror, and a sink.',
                'exits': {'west': 'bedroom'},
                'items': []
            }
        }

        self.current_room = 'living_room'  # Start in the living room
        self.inventory = []  # Items the player has collected
        self.game_over = False  # Game flag to determine when to stop

    def show_room(self):
        """Display the current room's description and available exits."""
        room = self.rooms[self.current_room]
        print(f'\n{room["description"]}')
        print(f'Exits: {", ".join(room["exits"].keys())}')
        if room['items']:
            print(f'Items here: {", ".join(room["items"])}')

    def move(self, direction):
        """Move to another room if the exit exists."""
        room = self.rooms[self.current_room]
        if direction in room['exits']:
            self.current_room = room['exits'][direction]
            print(f'\nYou move {direction} into the {self.current_room}.')
        else:
            print("\nYou can't go that way.")

    def pick_up(self, item):
        """Pick up an item if it exists in the room."""
        room = self.rooms[self.current_room]
        if item in room['items']:
            self.inventory.append(item)
            room['items'].remove(item)
            print(f'\nYou pick up the {item}.')
        else:
            print(f"\nThere is no {item} here.")

    def check_inventory(self):
        """Display the player's inventory."""
        if self.inventory:
            print(f'\nYou have the following items: {", ".join(self.inventory)}')
        else:
            print("\nYour inventory is empty.")

    def process_command(self, command):
        """Process a player's command."""
        command = command.lower().split()

        if not command:
            return

        if command[0] == 'look':
            self.show_room()
        elif command[0] == 'move' and len(command) > 1:
            self.move(command[1])
        elif command[0] == 'pick' and len(command) > 1:
            self.pick_up(command[1])
        elif command[0] == 'inventory':
            self.check_inventory()
        elif command[0] == 'quit':
            print("\nThanks for playing!")
            self.game_over = True
        else:
            print("\nI don't understand.")

    def start(self):
        """Start the game and handle user input."""
        print("\nWelcome!")

        while not self.game_over:
            self.show_room()
            command = input("\nWhat do you want to do? ").strip()
            self.process_command(command)


# Start the game
game = Room()
game.start()

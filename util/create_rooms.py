# from django.contrib.auth.models import User
from adventure.models import Player, Room
# from util.create_rooms import room_names, room_descriptions, World

room_names = [
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine"

    "The Fort of the Fury", "The golden Turret of the Destruction", "The Lab of the Blessing", "The Apothecary of the Renewal", "The Elemental Treasury of Renewal", "The Fortress of the Reawakened", "The Green Garden of Chaos", "The Twisted Chamber of the Void", "The Disturbing Pantry", "The Alabaster Manse of War", "The Hidden Ruin of the Vanquished", "The Nest of Pain",
    "The Scorched Nursery", "The Ancient Barracks", "The Farm of Betrayal", "The Pool of Undead", "The Bleeding Manse", "The Unholy Armoury",
    "The Noxious Sepulchre of Chaos", "The Lunar Fortress of the Treasure", "The Alluring Foundry of the Primeval Enchantment",
    "The Legendary Hospital of the Misty Death", "The Spectacular Church of Dreams", "The Chaotic Mine", "The Untamed Church of Flame",
    "The Twisted Menagerie of the Flame", "The Aviary of the Power", "The Miscreant Stockade", "The Dungeon of Shadow", "The Infernal Gallery",
    "The Fiery Castle of the Unholy Imprisoned", "The Merciless Pantry", "The Foundry of Schemes", "The Fabled Caves of the Plain Schemes",
    "The Secluded Passage", "The Cathedral of the Tranquillity", "The Observatory of Eternity", "The Elder Pantry of Imprisoned", "The Miscreant Tower of the Despair",
    "The Giant Warehouse of Legends", "The Wooden Nest of Banishment", "The Fort of the Wrath", "The Private Church of the Pleasure", "The Silver Pantry of the Spirits",
    "The Phased Rift of the Warped Death", "The Lab of the Terror", "The Pagoda of Horde", "The Tavern of Terror", "The Severe Maze of the Horde",
    "The Steel Stronghold", "The Glorious Tunnel of the Gloom", "The Pantry of the War", "The Immense Nursery of the Sloth", "The Fane of Abyss",
    "The Cluttered Sanctum of the Renewal", "The Cluttered Stockade", "The Greenhouse of Frost", "The Holy Spire of the Noxious Eternity",
    "The Bleeding Catacomb of the Torture", "The Black Hall of the Ascension", "The Sliding Plaza of the Time", "The Fountain of Illusion", "The Floating Caves",
    "The Corridor of Time", "The Spire of Sloth", "The Dusty Lair of the Woe", "The Fallen Nursery of Terror", "The Monolith of the Secrets", "The Quarters of the Vanquished",
    "The Lost Stronghold", "The Obsidian Tavern of the Dirty Abyss", "The Portal of Spirits", "The Home of the Legends", "The Blue Keep of the Heavens", "The Plaza of the Worms",
    "The Rampart of Blood", "The Creepy Bedroom", "The Vault of Damnation", "The Cathedral of the Oblivion", "The Looping Pillar", "The Simple Dome of Sorcery",
    "The Insane Temple of Desire", "The Red Cellar of Curses", "The Graveyard of Wyrms", "The Unstable Dome of the Warped Mystery", "The Boring Fortress of the Phased Madness",
    "The Shrine of the Order", "The Rift of Light", "The Infinite Fortress", "The Lunar Bedroom", "The Buried Cathedral of the Screams", "The Spooky Portal of the Gods",
    "The Quarters of Light", "The Eldritch Treasury of the Cursed Sorcery", "The Infested Hideout of the White Void", "The Endless Lair of the Contaminated Mystery",
    "The Primeval Stairs of the Insanity", "The Legendary Bridge of the Amazing Dreams", "The Small Rift of Flame", "The Polluted Kennel of Mystery", "The Hellish Lab of the Ghosts"
]


room_descriptions = [
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine",
    # "The Creepy Mine"
    
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon.",
    "A short worn statue in a gloomy swamp marks the entrance to this dungeon."
]


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''
        # Initialize the grid
        Room.objects.all().delete()
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
            # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        room_count = 0
        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west
        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:
            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1
            # Create a room in the given direction
            room = Room(
                room_count, room_names[room_count], room_descriptions[room_count],  x, y)
            # Save the room in the World grid
            self.grid[y][x] = room
            # Connect the new room to the previous 
            room.save()
            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)
            # Update iteration variables
            previous_room = room
            room_count += 1
            # print(f'room: {room}')

    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''
        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"
        # The console prints top to bottom but our array is arranged
        # bottom to top.
    # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to != 0:
                    str += "  |  "
                else:
                    str += "     "
                str += "#\n"
                # PRINT ROOM ROW
                str += "#"
                for room in row:
                    if room is not None and room.w_to != 0:
                        str += "-"
                    else:
                        str += " "
                    if room is not None:
                        str += f"{room.id}".zfill(3)
                    else:
                        str += "   "
                    if room is not None and room.e_to != 0:
                        str += "-"
                    else:
                        str += " "
                str += "#\n"
                # PRINT SOUTH CONNECTION ROW
                str += "#"
                for room in row:
                    if room is not None and room.s_to != 0:
                        str += "  |  "
                    else:
                        str += "     "
                str += "#\n"
                # Add bottom border
                str += "# " * ((3 + self.width * 5) // 2) + "\n"
                # Print string
                print(str)
# w = World()
# num_rooms = 100
# width = 10
# height = 10
# w.generate_rooms(width, height, num_rooms)
# print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")

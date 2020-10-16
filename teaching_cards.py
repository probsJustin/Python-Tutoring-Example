
class card:
    suit = ""
    face_or_number = ""
    def __init__(self, function_suit, function_face_or_number):
        self.suit = function_suit
        self.face_or_number = function_face_or_number

    def set_suit(self, function_suit):
        self.suit = function_suit

    def get_suit(self):
        return self.suit

    def set_face_or_number(self, function_face_or_number):
        self.face_or_number = function_face_or_number

    def get_face_or_number(self):
        return self.face_or_number

    def print_card(self):
        print("[" + self.get_suit() + "]: " + self.get_face_or_number())

deck_of_cards = list()

def switch_suit(arg):
    switcher = {
        0: "spade",
        1: "heart",
        2: "diamond",
        3: "clubs"
    }
    return switcher[arg]

def switch_face(arg):
    switcher = {
        0: "A",
        1: "2",
        2: "3",
        3: "4",
        4: "5",
        5: "6",
        6: "7",
        7: "8",
        8: "9",
        9: "10",
        10: "J",
        11: "Q",
        12: "K"
    }
    return switcher[arg]

for x in range(0,4):
    for_suit = switch_suit(x)
    for y in range(0,13):
        for_face = switch_face(y)
        deck_of_cards.append(card(for_suit, for_face))

test_card = card("spade", "12")

for x in deck_of_cards:
    x.print_card()


from models import Room

rooms = [
    Room(id=101, category="Standard", price_per_night=35000),
    Room(id=102, category="Suite Senior", price_per_night=65000),
    Room(id=103, category="Suite Prestige", price_per_night=120000),
]

stock = {
    "gel_douche": 100,
    "papier_hygiénique": 100,
    "pantoufle": 50,
    "brosse_a_dent": 50
}

reservations = []
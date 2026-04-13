from fastapi import FastAPI, HTTPException
from models import Reservation, Room
from data import rooms, stock, reservations

app = FastAPI(title="Web Service Hôtel - BPMN")

@app.get("/")
def home():
    return {"message": "Bienvenue ! C'est le Web Service de l'hôtel"}

@app.get("/rooms")
def get_rooms():
    return {"chambres_disponibles": [r for r in rooms if r.is_clean]}

@app.post("/reservations")
def create_reservation(res: Reservation):
    room = next((r for r in rooms if r.id == res.room_id), None)
    if not room or not room.is_clean:
        raise HTTPException(400, "Chambre non disponible ou pas propre")
    
    # Consommer les articles
    for item in stock:
        stock[item] -= res.nights
    
    res.total_amount = room.price_per_night * res.nights
    res.invoice_number = f"FACT-{len(reservations)+1:04d}"
    res.id = len(reservations) + 1
    reservations.append(res)
    
    room.is_clean = False  # chambre occupée
    return {"message": "Réservation réussie !", "facture": res}

@app.post("/cleaning/{room_id}")
def cleaning_done(room_id: int):
    room = next((r for r in rooms if r.id == room_id), None)
    if room:
        room.is_clean = True
        return {"message": f"Chambre {room_id} est maintenant propre"}
    raise HTTPException(404, "Chambre non trouvée")

@app.get("/dashboard")
def dashboard():
    return {
        "chambres_vendues": len(reservations),
        "stock_restant": stock,
        "message": "Tableau de bord comptable"
    }
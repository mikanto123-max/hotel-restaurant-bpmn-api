# Hôtel & Restaurant - BPMN + Web Service

## Processus BPMN
- Client réserve sur site web ou Facebook
- Réceptionniste vérifie chambre propre
- Facture + paiement + pièce d'identité
- Client occupe la chambre
- Femme de ménage nettoie et remet : gel douche, papier hygiénique, pantoufle, brosse à dent
- Comptable vérifie stock et fait le tableau de bord
- Restaurant peut ajouter sa note sur la facture

## Comment tester le Web Service
1. Installer : pip install fastapi uvicorn
2. Lancer : uvicorn main:app --reload
3. Ouvrir dans le navigateur : http://127.0.0.1:8000/docs
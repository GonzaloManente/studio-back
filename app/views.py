from flask import jsonify, request
from app.models import Promocion

def index():
    return '<body style="background-color:#181419"><h1 style="color:orange;text-align:Center;margin-top:150px;">Back End de Pizzería Studio Pizza</h1> <br> <h2 style="color:orange;text-align:Center;">Johanna Nuñez, Gonzalo Manente, Luis Calderas</h2> <br> <h2 style="color:orange;text-align:Center;">Codo a Codo 2024</h2></body>'

def get_all_promociones():
    promociones = Promocion.get_all()
    list_promos = [promo.serialize() for promo in promociones]
    return jsonify(list_promos)

def create_promocion():
    # Recepcionando los datos enviados en la peticion en formato JSON
    data = request.json
    new_promo = Promocion(
        nombre_promocion=data['nombre_promocion'],
        detalle_pizzas=data['detalle_pizzas'],
        precio_promocion=data['precio_promocion']
    )
    new_promo.save()
    return jsonify({'message':'Promocion creada con exito'}), 201
    
def update_promocion(id_promocion):
    promo = Promocion.get_by_id(id_promocion)
    if not promo:
        return jsonify({'message': 'Promoción no encontrada'}), 404
    data = request.json
    promo.nombre_promocion = data['nombre_promocion']
    promo.detalle_pizzas = data['detalle_pizzas']
    promo.precio_promocion = data['precio_promocion']
    promo.save()
    return jsonify({'message': 'Promoción actualizada'})

def get_promocion(id_promocion):
    promo = Promocion.get_by_id(id_promocion)
    if not promo:
        return jsonify({'message': 'Promocion no encontrada'}), 404
    return jsonify(promo.serialize())

def delete_promocion(id_promocion):
    promo = Promocion.get_by_id(id_promocion)
    if not promo:
        return jsonify({'message': 'Promoción no encontrada'}), 404
    promo.delete()
    return jsonify({'message': 'Promoción borrada'})
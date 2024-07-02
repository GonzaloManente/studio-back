from app.database import get_db

class Promocion:

    #constuctor
    def __init__(self,id_promocion=None,nombre_promocion=None,detalle_pizzas=None,precio_promocion=None):
        self.id_promocion=id_promocion
        self.nombre_promocion=nombre_promocion
        self.detalle_pizzas=detalle_pizzas
        self.precio_promocion=precio_promocion

    def serialize(self):
        return {
            'id_promocion': self.id_promocion,
            'nombre_promocion': self.nombre_promocion,
            'detalle_pizzas': self.detalle_pizzas,
            'precio_promocion': self.precio_promocion
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM promociones ORDER BY id_promocion"
        cursor.execute(query)
        rows = cursor.fetchall()

        promos = []
        for row in rows:
            new_promo = Promocion(id_promocion=row[0], nombre_promocion=row[1], detalle_pizzas=row[2], precio_promocion=row[3])
            promos.append(new_promo)

        cursor.close()
        return promos
        
    @staticmethod
    def get_by_id(id_promocion):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM promociones WHERE id_promocion = %s", (id_promocion,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Promocion(id_promocion=row[0], nombre_promocion=row[1], detalle_pizzas=row[2], precio_promocion=row[3])
        return None
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_promocion:
            cursor.execute("""
                UPDATE promociones SET nombre_promocion = %s, detalle_pizzas = %s, precio_promocion = %s
                WHERE id_promocion = %s
            """, (self.nombre_promocion, self.detalle_pizzas, self.precio_promocion, self.id_promocion))
        else:
            cursor.execute("""
                INSERT INTO promociones (nombre_promocion, detalle_pizzas, precio_promocion) VALUES (%s, %s, %s)
            """, (self.nombre_promocion, self.detalle_pizzas, self.precio_promocion))
            self.id_promocion = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM promociones WHERE id_promocion = %s", (self.id_promocion,))
        db.commit()
        cursor.close()

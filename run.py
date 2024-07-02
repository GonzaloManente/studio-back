from flask import Flask
from flask_cors import CORS
from app.views import *
from app.database import init_app

#inicializacion del proyecto Flask
app = Flask(__name__)
CORS(app)

init_app(app)

app.route('/', methods=['GET'])(index)
app.route('/api/promos/', methods=['GET'])(get_all_promociones)
app.route('/api/promos/<int:id_promocion>', methods=['GET'])(get_promocion)
app.route('/api/promos/', methods=['POST'])(create_promocion)
app.route('/api/promos/<int:id_promocion>', methods=['PUT'])(update_promocion)
app.route('/api/promos/<int:id_promocion>', methods=['DELETE'])(delete_promocion)

if __name__=='__main__':
    app.run(debug=True)
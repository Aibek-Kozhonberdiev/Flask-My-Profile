from flask import send_file

from webapp import app


@app.get('/')
def index():
    return send_file('static/pdf/Aibek_Kozhonberdiev.pdf', mimetype='application/pdf')


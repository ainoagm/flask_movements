from movements import app

@app.route('/')
def listaMovimientos():
    return render_template ("movementsList.html", miTexto="Ya veremos si hay movimientos o no")


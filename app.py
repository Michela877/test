from flask import Flask, request, render_template

app = Flask(__name__)

nomi = []
nomi2 = []
@app.route('/', methods=['GET', 'POST'])
def index():
    global nomi, nomi2  # Aggiungi questa riga per utilizzare la variabile globale nomi
    if request.method == 'POST':
        nome = request.form.get('nome')
        if request.form.get('action2') == 'salva':
            nomi.append(nome)
        elif request.form.get('action1') == 'Cancella':
            nomi.clear()
            nomi2.clear()# Modifica questa riga per svuotare la lista nomi
        elif request.form.get('action3') == 'Ordina':
            nomi2 = sorted(nomi)  # Modifica questa riga per svuotare la lista nomi
    return render_template("index.html", nomi=nomi, nomi2=nomi2)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

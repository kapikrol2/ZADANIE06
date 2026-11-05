from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

KSIAZKI = [
    {"id": 1, "tytul": "Wiedźmin: Ostatnie życzenie", "autor": "Andrzej Sapkowski", "rokwydania": 1993, "dostepna": True},
    {"id": 2, "tytul": "Hobbit", "autor": "J.R.R. Tolkien", "rokwydania": 1937, "dostepna": False},
    {"id": 3, "tytul": "Rok 1984", "autor": "George Orwell", "rokwydania": 1949, "dostepna": True},
    {"id": 4, "tytul": "Diuna", "autor": "Frank Herbert", "rokwydania": 1965, "dostepna": True},
    {"id": 5, "tytul": "Nowy wspaniały świat", "autor": "Aldous Huxley", "rokwydania": 1932, "dostepna": False},
]


@app.route("/")
def index():
    nazwa_projektu = "Biblioteka Szkolna 4TP"
    imie_autor = "Jan Kowalski"
    return render_template("index.html", nazwa_projektu=nazwa_projektu, imie=imie_autor)


@app.route("/lista")
def lista():
    return render_template("lista.html", ksiazki=KSIAZKI)


@app.route("/element/<int:id>")
def szczegoly(id):
    ksiazka = next((k for k in KSIAZKI if k["id"] == id), None)
    if ksiazka is None:
        abort(404)
    return render_template("szczegoly.html", ksiazka=ksiazka)


@app.route("/szukaj")
def szukaj():
    q = request.args.get("q", "")
    wyniki = [k for k in KSIAZKI if q.lower() in k["tytul"].lower() or q.lower() in k["autor"].lower()]
    return render_template("szukaj.html", q=q, wyniki=wyniki)


@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        nowe_id = max([k["id"] for k in KSIAZKI], default=0) + 1
        nowa_ksiazka = {
            "id": nowe_id,
            "tytul": request.form.get("tytul"),
            "autor": request.form.get("autor"),
            "rokwydania": int(request.form.get("rokwydania", 0)),
            "dostepna": request.form.get("dostepna") == "on"
        }
        KSIAZKI.append(nowa_ksiazka)
        return redirect(url_for("lista"))
    return render_template("dodaj.html")

if __name__ == "__main__":
    app.run(debug=True)
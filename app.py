from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__)

KSIAZKI = [
    {"id": 1, "tytul": "Wiedźmin: Ostatnie życzenie", "autor": "Andrzej Sapkowski", "rokwydania": 1993, "dostepna": True},
    {"id": 2, "tytul": "Hobbit", "autor": "J.R.R. Tolkien", "rokwydania": 1937, "dostepna": False},
    {"id": 3, "tytul": "Rok 1984", "autor": "George Orwell", "rokwydania": 1949, "dostepna": True},
    {"id": 4, "tytul": "Diuna", "autor": "Frank Herbert", "rokwydania": 1965, "dostepna": True},
    {"id": 5, "tytul": "Nowy wspaniały świat", "autor": "Aldous Huxley", "rokwydania": 1932, "dostepna": False},
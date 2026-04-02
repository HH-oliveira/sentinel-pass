from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Minha função de lógica de segurança (Backend)
def validar_senha(senha):
    score = 0
    if len(senha) >= 8: score += 1
    if re.search(r"[A-Z]", senha): score += 1
    if re.search(r"[0-9]", senha): score += 1
    if re.search(r"[@$!%*?&#]", senha): score += 1
    return score

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    nome = None
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        score = validar_senha(senha)
    
    return render_template("index.html", score=score, nome=nome)

if __name__ == "__main__":
    app.run(debug=True)
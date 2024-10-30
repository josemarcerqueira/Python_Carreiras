from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

VAGAS = [
    {
        'id:': 1,
        'titulo': 'Desenvolvedor Web',
        'localidade': 'Rio de Janeiro, Brasil',
        'salario': 'R$ 3.000,00'
    },
    {
        'id': 2,
        'titulo': 'Desenvolvedor Python',
        'localidade': 'São Paulo, Brasil',    
        'salario': 'R$ 4.000,00'
    },
    {
        'id': 3,
        'titulo': 'Analista de Dados',
        'localidade': 'Salvador, Brasil',
        'salario': 'R$ 3.000,00'
    },
    {
        'id': 4,
        'titulo': 'Desenvolvedor Backend',
        'localidade': 'Curitiba, Brasil',
        'salario': 'R$ 5.000,00'   
    },
{
        'id': 5,
        'titulo': 'Estatístico',
        'localidade': 'São Paulo, Brasil',
        'salario': 'R$ 6.000,00'   
    
}
]

@app.route("/")
def hello_world():
    return render_template("home.html", vagas=VAGAS)

@app.route("/vagas")
def lista_vagas():
    return jsonify(VAGAS)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
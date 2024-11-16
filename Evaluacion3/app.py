from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = request.form.get('nota1')
        nota2 = request.form.get('nota2')
        nota3 = request.form.get('nota3')
        asistencia = request.form.get('asistencia')
        # Procesar los datos aquí
        return f"Notas: {nota1}, {nota2}, {nota3} - Asistencia: {asistencia}%"
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')
        nombre3 = request.form.get('nombre3')
        # Procesar los datos aquí
        return f"Nombres: {nombre1}, {nombre2}, {nombre3}"
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)

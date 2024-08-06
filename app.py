from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_plan(weight, exercise_hours, goal, ideal_weight, commitment):
    if goal == 'esteticos':
        if float(exercise_hours) >= 1:
            return "Plan A: Dieta alta en proteínas con ejercicio regular."
        else:
            return "Plan B: Dieta balanceada con ejercicio moderado."
    elif goal == 'salud':
        if float(weight) > float(ideal_weight) and commitment == 'yes':
            return "Plan C: Dieta baja en carbohidratos con ejercicio diario."
        else:
            return "Plan B: Dieta balanceada con ejercicio moderado."
    else:
        return "Plan B: Dieta balanceada con ejercicio moderado."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        weight = request.form.get('weight')
        exercise_hours = request.form.get('exercise_hours')
        goal = request.form.get('goal')
        ideal_weight = request.form.get('ideal_weight')
        commitment = request.form.get('commitment')
        
        plan = get_plan(weight, exercise_hours, goal, ideal_weight, commitment)
        return redirect(url_for('result', plan=plan))
    
    return render_template('questions.html')

@app.route('/result')
def result():
    plan = request.args.get('plan')
    return render_template('result.html', plan=plan)

if __name__ == "__main__":
    app.run(debug=True)

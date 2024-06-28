from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    return render_template('static_index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_description = request.form['task']
        new_task = Task(description=task_description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('display_tasks'))
    return render_template('add_task.html')

@app.route('/tasks', methods=['GET'])
def display_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/<int:task_id>/update', methods=['GET'])
def update_task(task_id):
    task_to_update = Task.query.get_or_404(task_id)
    return render_template('update_task.html', task=task_to_update)

@app.route('/tasks/<int:task_id>/update', methods=['PUT'])
def update_task_put(task_id):
    task_to_update = Task.query.get_or_404(task_id)
    data = request.get_json()
    new_task_description = data['new_task']
    task_to_update.description = new_task_description
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'})

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    if task_to_delete:
        db.session.delete(task_to_delete)
        db.session.commit()
    return redirect(url_for('display_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
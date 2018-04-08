#!flask/bin/python3

from flask import Flask, jsonify, abort, request,send_from_directory
from itung import lapista
#import os
UPLOAD_FOLDER = '/uploads/'
app = Flask(__name__,static_folder='uploads')

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]



@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
@app.route('/todo/lone/<int:task_value>', methods=['GET'])

@app.route('/todo/lone/', methods=['GET','POST'])
def get_task3():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save('files/'+filename)    
    return jsonify({'message':'send done'})

@app.route('/uploads/<path:filename>/<int:passs>', methods=['GET', 'POST'])
def download(filename,passs):
    if passs == 12345:
        are = send_from_directory(directory='uploads', filename=filename)
        return are
    
if __name__ == '__main__':
    app.run(debug=True)
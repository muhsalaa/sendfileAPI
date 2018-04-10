#!flask/bin/python3
import os
from flask import Flask, jsonify, request,send_from_directory
import server3, client3
#from itung import lapista
#import os
UPLOAD_FOLDER = '/uploads/'
app = Flask(__name__,static_folder='uploads')

@app.route('/')
@app.route('/cihuy/')
def cihuy():
    return "Hello World"

@app.route('/todo/lone/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save('uploads/'+filename)
            server3.encrypt_file('1234567812345678', filename, filename+".enc")
            os.remove(filename)
            os.remove('uploads/'+filename)
    return jsonify({'message':'send done'})

@app.route('/uploads/<path:filename>/<int:passs>', methods=['GET', 'POST'])
def download(filename,passs):
    if passs == 12345:
        t = client3.decrypt_file('1234567812345678', filename+".enc")
        os.remove('uploads/'+filename+".enc")
        are = send_from_directory(directory='uploads', filename=filename)
        os.remove('uploads/'+filename)        
        return are
      
'''
@app.route('/uploads/encrypt/<path:filename>/<int:passs>', methods=['GET', 'POST'])
def download(filename,passs):
    if passs == 12345:
        are = send_from_directory(directory='uploads', filename=filename)
        return are
'''    
if __name__ == '__main__':
    app.run(debug=True)
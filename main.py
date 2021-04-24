from flask import Flask, render_template, request, jsonify
import socket

#ip = socket.gethostbyname(socket.getfqdn())
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi!'
    #ip = soket.gethostbyname(socket.getfqdn())
    #print(ip)@app.route('/news', methods=['GET'])
def news():
    #return render_template("index.html", ip=ip)

@app.route('/about')
def about():
    return 'About me <BR> <a href="/">Назад</a>'
@app.route('/post/<int:post_id>')
def post(post_id):
    return f'Номер этого поста: {post_id}'

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return render_template('calc.html')
    if request.method == 'POST':
        a = float(request.form.get('nomber_one'))
        b = float(request.form.get('nomber_tow'))

        if request.form['calc'] == 'Сумма':
            c = a + b
        if request.form['calc'] == 'Разность':
            c = a-b
        return render_template('calc.html', c=c)
@app.route('/rest', methods=['GET'])
def rest():
    b = 5
    a = {'one': 1, "two": 2,}
    user = {"name": "nick", 'email': 'dsd@dfsf', 'tel:': ['+79999199991', '+723241241234']}
    return user



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
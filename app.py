from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish/<name>')
def wish(name):
    return f'<h1>welcome to you {name} <h1>'

if __name__=='__main__':
    FAI.run(debug=True)

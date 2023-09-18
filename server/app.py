#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    x = range(parameter)
    return "\n".join([str(n) for n in x])
    
@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1,operation,num2):
    x = 0
    if operation == '+':
        x= num1 + num2
        return f'<p>{x}</p>'
    elif operation == '-':
        x= num1 - num2
        return f'<p>{x}</p>'
    elif operation == '*':
        x= num1 * num2
        return f'<p>{x}</p>'
    elif operation == 'div':
        x= num1 / num2
        return f'<p>{x}</p>'
    elif operation == '%':
        x= num1 % num2
        return f'<p>{x}</p>'
    else:
        return f'<p>Improper operation</p>'
    













if __name__ == '__main__':
    app.run(port=5555, debug=True)



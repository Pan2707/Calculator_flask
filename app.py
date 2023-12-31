from flask import Flask, render_template request, jsonify
import json


obj = Flask(__name__)



@obj.route('/')
def welcome():
    return 'Welcome'

#code for calculator
@obj.route('/cal', methods=['GET'])
def math_operator():
    operation = request.json['operation'] #json means 
    num1 = request.json['num1']
    num2 = request.json['num2']


    if operation == 'add':
        result = int(num1) + int(num2)
    elif operation =='subtract':
        result = int(num1) - int(num2)
    elif operation =='multiply':
        result = int(num1) * int(num2)
    else:
        result = int(num1) / int(num2)
    return jsonify(result)


print(__name__)
if __name__ == '__main__':
    obj.run(debug=True)



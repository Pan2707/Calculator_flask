from flask import Flask, render_template, request


obj = Flask(__name__)



@obj.route('/')
def welcome():
    return 'Welcome'

#code for calculator
@obj.route('/cal', methods=['GET'])
def math_operator():
    operator = reuest.json['operator'] #json means 
    num1 = request.json['num1']
    num2 = request.json['num2']
    

if operator == 'add':
    result = num1 + num2
elif operator =='subtract':
    result = num1 - num2
elif operator =='multiply':
    result = num1 * num2
else:
    result = num1 / num2
    return result


print(__name__)
if __name__ == '__main__':
    obj.run(debug=True)



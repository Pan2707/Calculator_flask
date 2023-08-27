from flask import Flask, request # import statememt where we import Flask



obj = Flask(__name__)


#creating a home route 
@obj.route('/')
def welcome():
    return 'Welcome'


#creating a main route  for calculator
@obj.route('/cal', methods=['GET'])
def math_operator():
    operation = request.json['operation'] #requesting in the form of jasonjson means 
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
    return "The operation is {} and the result is {}". format(operation, result)


print(__name__)
if __name__ == '__main__':
    obj.run(debug=True)



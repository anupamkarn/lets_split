from flask import Flask, request
from calculate_transaction import optimize_transaction

app = Flask(__name__)

@app.route('/split', methods=['GET','POST'])
def split(): 
    if request.method == 'GET':
        return "lets split"
    else:
        reduced_transaction_list = optimize_transaction(request.get_json())
        return reduced_transaction_list
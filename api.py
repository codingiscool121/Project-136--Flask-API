from flask import Flask, json,jsonify, request
from data import data
app=Flask(__name__)

@app.route('/')
def index():
    return jsonify({"stardata":data})


@app.route('/starinfo', methods=['GET'])

def starinfo():
    star=request.args.get('star')
    try:
        star = next(item for item in data if item['name'] == star)
        return jsonify(star)
    except:
        return jsonify({"error":"star not found"})
if __name__ == '__main__':
    app.run(debug=True)

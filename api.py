from flask import Flask, json,jsonify, request
from starsData import data
app=Flask(__name__)

@app.route('/')
def index():
    return jsonify({"stardata":data})


@app.route('/starinfo', methods=['GET'])

def starinfo():
    star=request.args.get('star')
    
    star2 = next(item for item in data if item['Name'] == star) 
    return jsonify({
            "stardata": star2
        })

if __name__ == '__main__':
    app.run(debug=True)

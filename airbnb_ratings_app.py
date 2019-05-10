from flask import Flask, request, render_template, jsonify, request, abort
from airbnb_ratings_api import predict_ratings

app = Flask(__name__)
amenities = ['24-hour check-in', 'Air conditioning', 'BBQ grill', 'Bed linens',
             'Cable TV', 'Coffee maker', 'Dishwasher', 'Elevator',
             'Extra pillows and blankets', 'Family/kid friendly',
             'Fire extinguisher', 'First aid kit', 'Gym', 'Indoor fireplace',
             'Internet', 'Keypad', 'Lock on bedroom door', 'Lockbox',
             'Long term stays allowed', 'Luggage dropoff allowed',
             'Pack ’n Play/travel crib', 'Patio or balcony', 'Pets allowed',
             'Private entrance', 'Private living room', 'Refrigerator',
             'Safety card', 'Self check-in']


@app.route("/predict", methods=['POST'])
def make_prediction():
    if not request.json:
        abort(400)
    data = request.json
    response = predict_ratings(data)

    return jsonify(response)
    # return render_template("result.html", response=jsonify(response))


@app.route("/")
def front():
    return render_template("front.html")


@app.route("/rate")
def index():
    amenity_list = [{'id': amenity.replace(' ', '_').replace('-', '_').replace('/', '_'),
                     'label': amenity} for amenity in amenities]
    return render_template("index.html", amenities=amenity_list)


if __name__ == "main":
    app.run(debug=False)

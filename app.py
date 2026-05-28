from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/plan-trip", methods=["POST"])
def plan_trip():

    data = request.json

    destination = data["destination"]
    budget = data["budget"]
    days = int(data["days"])
    interest = data["interest"]

    activities = {

        "Adventure": [
            "Trekking",
            "River Rafting",
            "sky diving",
            "Paragliding",
            "Mountain Biking"
        ],

        "Food": [
            "Try local street food",
            "Visit famous restaurants",
            "Food festival visit",
            "Cafe hopping",
            "Traditional dinner"
        ],

        "Nature": [
            "Visit waterfalls",
            "visit beach",
            "Sunrise viewpoint",
            "Forest walk",
            "Lake visit"
        ],

        "Shopping": [
            "Visit local markets",
            "Mall shopping",
            "Buy souvenirs",
            "Street shopping",
            "Night market visit"
        ]
    }

    places = [
        "Museum",
        "Beach",
        "Temple",
        "Park",
        "Historic Fort",
        "Zoo",
        "Palace",
        "Garden"
    ]

    itinerary = ""

    for day in range(days):

        activity =activities[interest][day % len(activities[interest])]

        place =places[day % len(places)]

        itinerary += f"""
Day {day + 1}:
- Visit {place} in {destination}
- Enjoy {activity}
- Try local food
- Evening relaxation and sightseeing

"""

    itinerary += f"""
Estimated Budget:
₹{budget}

Trip Duration:
{days} days
"""

    return jsonify({
        "trip": itinerary
    })

@app.route("/")
def home():
    return "AI Trip Planner Backend Running"

app.run(debug=True)
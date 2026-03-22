from flask import Blueprint, request, jsonify, render_template
from app.services.ai_service import (
    crop_advisory,
    soil_health,
    weather_advisory,
    pest_detection_info,
    market_advisory,
    get_ad_chat
)

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/chat")
def dashboard():
    return render_template("dashboard.html")


@main.route("/advanced-chat")
def ad_chat():
    return render_template("chat.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/crop")
def crop_page():
    return render_template("crop.html")


@main.route("/soil")
def soil_page():
    return render_template("soil.html")


@main.route("/weather")
def weather_page():
    return render_template("weather.html")


@main.route("/pest")
def pest_page():
    return render_template("pest.html")


@main.route("/market")
def market_page():
    return render_template("market.html")


@main.route("/api/crop", methods=["POST"])
def crop_api():
    data = request.get_json()
    return jsonify({
        "response": crop_advisory(
            data.get("location"),
            data.get("soil_type"),
            data.get("crop"),
            data.get("language")
        )
    })

@main.route("/api/chat", methods=["POST"])

def chat_api():
    message = request.form.get("message", "").lower()
    lang = request.form.get("language", "en")

    image_file = request.files.get("image")
    pdf_file = request.files.get("pdf")

    ai_response = get_ad_chat(
        msg=message,
        lang=lang,
        image=image_file,
        pdf=pdf_file
    )

    return jsonify({
        "response": ai_response
    })


@main.route("/api/soil", methods=["POST"])
def soil_api():
    data = request.get_json()
    return jsonify({
        "response": soil_health(
            data.get("soil_type"),
            data.get("ph"),
            data.get("language", "en")
        )
    })


@main.route("/api/weather", methods=["POST"])
def weather_api():
    data = request.get_json()
    return jsonify({
        "response": weather_advisory(
            data.get("location"),
            data.get("language", "en")
        )
    })


@main.route("/api/pest", methods=["POST"])
def pest_api():
    data = request.get_json()
    return jsonify({
        "response": pest_detection_info(
            data.get("crop"),
            data.get("problem"),
            data.get("language", "en")
        )
    })


@main.route("/api/market", methods=["POST"])
def market_api():
    data = request.get_json()
    return jsonify({
        "response": market_advisory(
            data.get("crop"),
            data.get("location"),
            data.get("language", "en")
        )
    })
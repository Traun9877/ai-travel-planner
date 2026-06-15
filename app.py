from flask import Flask, render_template, request, send_file
from services.gemini_service import generate_itinerary

from fpdf import FPDF
import sqlite3
import os

app = Flask(__name__)

latest_itinerary = ""
latest_destination = ""


# -------------------------
# DATABASE
# -------------------------

def init_db():

    conn = sqlite3.connect("travel.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        destination TEXT,
        days INTEGER,
        travelers INTEGER,
        traveler_type TEXT,
        budget TEXT,
        interests TEXT,
        itinerary TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


# -------------------------
# HOME
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# GENERATE ITINERARY
# -------------------------

@app.route("/generate", methods=["POST"])
def generate():

    global latest_itinerary
    global latest_destination

    destination = request.form["destination"]
    days = request.form["days"]
    travelers = request.form["travelers"]
    traveler_type = request.form["traveler_type"]
    budget = request.form["budget"]
    interests = request.form["interests"]

    itinerary = generate_itinerary(
        destination,
        days,
        travelers,
        traveler_type,
        budget,
        interests
    )

    latest_itinerary = itinerary
    latest_destination = destination

    conn = sqlite3.connect("travel.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO trips(
        destination,
        days,
        travelers,
        traveler_type,
        budget,
        interests,
        itinerary
    )
    VALUES(?,?,?,?,?,?,?)
    """,
    (
        destination,
        days,
        travelers,
        traveler_type,
        budget,
        interests,
        itinerary
    ))

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        destination=destination,
        itinerary=itinerary
    )


# -------------------------
# HISTORY PAGE
# -------------------------

@app.route("/history")
def history():

    conn = sqlite3.connect("travel.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT id,destination,days,budget
    FROM trips
    ORDER BY id DESC
    """)

    trips = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        trips=trips
    )


# -------------------------
# VIEW OLD TRIP
# -------------------------

@app.route("/trip/<int:trip_id>")
def view_trip(trip_id):

    conn = sqlite3.connect("travel.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT destination,itinerary
    FROM trips
    WHERE id=?
    """, (trip_id,))

    trip = cursor.fetchone()

    conn.close()

    return render_template(
        "result.html",
        destination=trip[0],
        itinerary=trip[1]
    )


# -------------------------
# PDF DOWNLOAD
# -------------------------

@app.route("/download-pdf")
def download_pdf():

    global latest_itinerary
    global latest_destination

    if not os.path.exists("generated_pdfs"):
        os.makedirs("generated_pdfs")

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(
        200,
        10,
        txt=f"Travel Itinerary - {latest_destination}",
        ln=True
    )

    pdf.ln(10)

    clean_text = latest_itinerary.encode(
        "latin-1",
        "replace"
    ).decode("latin-1")

    pdf.multi_cell(
        0,
        8,
        clean_text
    )

    filename = f"generated_pdfs/{latest_destination}.pdf"

    pdf.output(filename)

    return send_file(
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
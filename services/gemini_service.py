import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_itinerary(
    destination,
    days,
    travelers,
    traveler_type,
    budget,
    interests
):
    prompt = f"""
You are an expert travel planner.

Create a detailed travel itinerary.

Destination: {destination}
Number of Days: {days}
Number of Travelers: {travelers}
Traveler Type: {traveler_type}
Budget: {budget}
Interests: {interests}

Requirements:

1. Day-wise itinerary
2. Morning activities
3. Afternoon activities
4. Evening activities
5. Food recommendations
6. Transportation suggestions
7. Estimated budget breakdown
8. Hotel recommendations
9. Local tips

Format nicely with headings.
"""

    response = model.generate_content(prompt)

    return response.text
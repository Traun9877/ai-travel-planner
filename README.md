# AI Travel Planner


AI Travel Planner is a web application that generates personalized travel itineraries using Google's Gemini AI.
Users can input their travel preferences, and the application creates a detailed, day-by-day plan, which can be saved, revisited, and downloaded as a PDF.

## Features

- **Personalized Itineraries**: Generates travel plans based on destination, duration, budget, traveler type, and interests.
- **AI-Powered**: Utilizes the Google Gemini API to create detailed and relevant travel suggestions.
- **Trip History**: Automatically saves all generated itineraries to a local SQLite database for future reference.
- **PDF Export**: Allows users to download their generated travel plan as a PDF document.
- **Simple Web Interface**: A clean and user-friendly interface for a seamless experience.

## Tech Stack

- **Backend**: Python, Flask
- **AI Model**: Google Gemini (`gemini-2.5-flash`)
- **Database**: SQLite
- **PDF Generation**: FPDF2
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Gunicorn, Render

## Local Setup and Installation

Follow these steps to run the project on your local machine.

**1. Clone the Repository**

```bash
git clone https://github.com/traun9877/ai-travel-planner.git
cd ai-travel-planner
```

**2. Create and Activate a Virtual Environment**

It's recommended to use a virtual environment to manage dependencies.

- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Set Up Environment Variables**

You need a Google Gemini API key to run this application.

- Create a file named `.env` in the root directory of the project.
- Add your API key to the `.env` file:

  ```
  GEMINI_API_KEY=your_google_gemini_api_key
  ```

**5. Run the Application**

The Flask application will initialize the SQLite database automatically on the first run.

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000`.

## Usage

1.  Navigate to the home page.
2.  Fill in the form with your travel details:
    - Destination
    - Number of Days
    - Number of Travelers
    - Traveler Type (Solo, Couple, etc.)
    - Budget (Low, Medium, Luxury)
    - Interests (Adventure, Food, Culture, etc.)
3.  Click the **"Generate Itinerary"** button.
4.  The application will display the AI-generated travel plan on the results page.
5.  From the results page, you can **download the itinerary as a PDF** or go back to create a new trip.
6.  To see previously generated trips, click the **"View Trip History"** button on the home page.

## Deployment

This project includes a `render.yaml` file for easy deployment on [Render](https://render.com/). You can fork this repository and create a new Web Service on Render, which will automatically use the configuration file to build and start the application. Remember to set the `GEMINI_API_KEY` as an environment variable in your Render service settings.

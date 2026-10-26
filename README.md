# Geospatial AI Assistant

## Overview
The **Geospatial AI Assistant** is a web application designed to answer natural language queries related to geospatial data. It integrates advanced AI models, geospatial services and interactive maps to provide an intuitive way for users to interact with geospatial information.

---

## Features and Functionalities

### **Backend Features**
- **Qdrant Integration**: Uses a vector database for managing embeddings of geospatial data.
- **LLM Integration**: Processes natural language queries with an LLM 
- **Geospatial Processing**: Handles coordinate-based calculations and geospatial analytics.
- **Geocoding Service**: Converts addresses into latitude/longitude and vice versa.

### **Frontend Features**
- **Interactive Chat**: Provides a bot-like interface for users to ask questions.
- **Dynamic Map Rendering**: Displays locations and data points on an interactive map.
- **Responsive Design**: Optimized for both desktop and mobile use.
- **Real-Time Updates**: Fetches and displays responses and maps dynamically.

---

## Tech Stack

### **Backend**
- **Programming Language**: Python
- **Framework**: Flask 
- **Database**: Qdrant (Vector Database)
- **APIs**: Gemini, Geocoding 
- **Environment Management**: Python `venv`

### **Frontend**
- **Library**: React,leaflet
- **Styling**: CSS
- **Environment Management**: dotenv for managing environment variables.

---

## Setup and Installation

### **1. Backend Setup**

#### Navigate to the `backend` directory:
```bash
cd backend
```

#### Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

#### Install dependencies:
```bash
pip install -r requirements.txt
```

#### Add environment variables:
Create a `.env` file in the `backend` directory with the following:
```env
FLASK_APP=app.py
FLASK_ENV=development
OPENAI_API_KEY=your_openai_api_key
GEOCODING_API_KEY=your_geocoding_api_key
QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION_NAME=your_collection_name
```

#### Running the Backend:
1. **Scraping Data**: 
   - Place your scraped geospatial data files in the `backend/data/` folder.
   - Ensure the data is in the correct format (e.g.PDF).
   
2. **Ingesting Data into Qdrant**:
   - Use the `ingestion.py` script to send the data to the Qdrant database.
   
   Run the following command:
   ```bash
   python ingestion.py
   ```

   This will process the data from the `data/` folder and send it to the Qdrant database.

3. **Run the Backend Server**:
   ```bash
   flask run
   ```
   The server will run at **`http://localhost:5000`**.

---

### **3. Frontend Setup**

#### Navigate to the `frontend` directory:
```bash
cd frontend
```

#### Install dependencies:
```bash
npm install
```

#### Add environment variables:
Create a `.env` file in the `frontend` directory with the following:
```env
REACT_APP_API_URL=http://localhost:5000/ask
```

#### Start the frontend:
```bash
npm start
```
The React app will run at **`http://localhost:3000`**.

---

## Usage

1. Start both the backend and frontend servers as described above.
2. Open **`http://localhost:3000`** in your browser.
3. Use the chat interface to ask questions, such as:
   - "What is the latitude and longitude of Pune?"
   - "Show all locations near Mumbai within 50 km."
   - "Convert this address into coordinates: Shivaji Nagar, Pune."
4. View the results dynamically on the map.

---

## Tools Used

- **Qdrant**: For vector embeddings of geospatial data.
- **OpenAI GPT**: For natural language processing.
- **Geocoding APIs**: To convert addresses into coordinates.
- **Flask**: Backend framework to handle API requests.
- **React**: Frontend framework for building the user interface.
- **dotenv**: For managing environment variables.
- **npm**: For managing frontend dependencies.

---

## How the Services Work

1. **LLM Service** (`llm_service.py`):
   - Sends queries to an LLM (like GPT) to process natural language.
   - Returns structured data (e.g., location names, coordinates).

2. **Geospatial Service** (`geospatial_service.py`):
   - Calculates distances, checks for nearby locations, and handles spatial queries.

3. **Geocoding Service** (`geocoding_service.py`):
   - Converts addresses to coordinates and vice versa using APIs like Google Maps or OpenStreetMap.

4. **Qdrant Service** (`qdrant_service.py`):
   - Handles embeddings and similarity searches using a vector database.

5. **Ingestion Service** (`ingestion.py`):
   - Ingests scraped data (from the `data/` folder) into the Qdrant database for indexing and querying.


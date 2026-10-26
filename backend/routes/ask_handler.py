from flask import Blueprint, request, jsonify
from services.qdrant_service import search_query
from services.llm_service import generate_response
from services.geospatial_service import extract_entities_from_text
from services.geocoding_service import fetch_geocoding_data

ask_handler = Blueprint("ask_handler", __name__)

@ask_handler.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"response": "Invalid request: 'query' is required."}), 400

        query = data["query"]

        # Step 1: Use embeddings for search
        search_results = search_query(query, collection_name="EDIproject")
        relevant_content = ""
        for doc in search_results:
            page_content = doc.payload.get('page_content', "No page content available")
            if doc.score > 0.5:
                relevant_content += page_content + "\n\n"

        # Step 2: Use Gemini to generate chat response
        template_chat = """
        You are a geography expert from India. Analyze the question and return concise, clear insights in bullet points.
        Query:
        {query}
        Page Content:
        {page_content}
        Response:
        """
        response = generate_response(template_chat, ["query", "page_content"], {"query": query, "page_content": relevant_content}) if relevant_content else "No relevant content found."

        # Step 3 (Optional): Extract geospatial entities from Gemini's response
        template_entity = """
        Extract important geospatial entities from the provided text. Return them in a comma-separated format.
        Text:
        {text}
        Entities:
        """
        entities = extract_entities_from_text(generate_response(template_entity, ["text"], {"text": response}))

        # Step 4: Fetch geocoding data
        locations = [fetch_geocoding_data(entity) for entity in entities if fetch_geocoding_data(entity)]

        return jsonify({"response": response, "locations": locations})
    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"}), 500

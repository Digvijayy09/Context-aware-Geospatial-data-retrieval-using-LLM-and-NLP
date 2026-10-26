def extract_entities_from_text(chain_entity, text):
    response = chain_entity.run({"text": text})
    return [entity.strip() for entity in response.split(",") if entity.strip()]

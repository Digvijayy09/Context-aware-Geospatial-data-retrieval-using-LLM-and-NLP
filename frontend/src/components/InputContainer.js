import React, { useState } from "react";
import { askQuery } from "../utils/apiService";

const InputContainer = ({ setLocations }) => {
  const [query, setQuery] = useState("");

  const handleSubmit = async () => {
    if (!query.trim()) return;

    const response = await askQuery(query);
    if (response) {
      setLocations(response.locations || []);
    }
    setQuery("");
  };

  return (
    <div className="input-container">
      <input
        type="text"
        placeholder="Ask me something..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSubmit}>Send</button>
    </div>
  );
};

export default InputContainer;

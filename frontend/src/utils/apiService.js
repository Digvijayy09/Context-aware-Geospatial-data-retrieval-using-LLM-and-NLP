const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000/ask";

export const askQuery = async (query) => {
  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
    });
    return await res.json();
  } catch (error) {
    console.error("Error while fetching response:", error);
    return null;
  }
};

export const formatResponse = (response) => {
    if (!response || !response.response) return [];
    return response.response.split("\n").map((line) => line.trim());
  };
  
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const analyzeAttack = async (attack) => {
  const response = await axios.post(
    `${API_BASE_URL}/api/analyze`,
    {
      attack,
    }
  );

  return response.data;
};
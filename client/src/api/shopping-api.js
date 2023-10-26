import axios from "axios";

export const getAllShopping = () => {
  return axios.get("http://localhost:8000/shopping/api/v1/shopping/");
};

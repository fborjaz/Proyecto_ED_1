import { useEffect, useState } from "react";
import { getAllShopping } from "../api/shopping-api";

export function TasksList() {
  const [shopping, setShopping] = useState([]);

  useEffect(() => {
    async function loadShopping() {
      const res = await getAllShopping();
    setShopping(res.data);
    }
    loadShopping();
  }, []);

  return <div>
    
    {shopping.map(shopping => (
      <div key={shopping.id}>
        <h1>{shopping.name}</h1>
        <p>{shopping.description}</p>
      </div>
    ))}

  </div>;
}

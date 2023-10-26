import { useEffect, useState } from "react";
import { getAllShopping } from "../api/shopping-api";
import { ShoppingCard } from "./ShoppingCard";

export function TasksList() {
  const [shopping, setShopping] = useState([]);

  useEffect(() => {
    async function loadShopping() {
      const res = await getAllShopping();
      setShopping(res.data);
    }
    loadShopping();
  }, []);

  return (
    <div>
      {shopping.map((shopping) => (
        <ShoppingCard key={shopping.id} shopping={shopping} />
      ))}
    </div>
  );
}

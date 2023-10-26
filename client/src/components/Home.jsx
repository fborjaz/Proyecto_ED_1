import React, { useState } from 'react';

const Home = () => {
  const [showStore, setShowStore] = useState(false);

  const handleArrowClick = () => {
    setShowStore(!showStore);
  };

  return (
    <div className="home-container">
      <h1>Simulador de Lista de Compras</h1>
      <p>En este proyecto, los estudiantes crearán un simulador de lista de compras...</p>
      <button onClick={handleArrowClick}>↓</button>
      {showStore ? (
        <div className="store">
          {/* Contenido de la tienda */}
        </div>
      ) : null}
    </div>
  );
};

export default Home;

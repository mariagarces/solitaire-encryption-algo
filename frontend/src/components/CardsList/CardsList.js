import React from "react";
import { useState } from "react";
import { getKeyCards } from "../../services/encryptionService";
import "./CardsList.css";

const CardsList = () => {
  const [cards, setCards] = useState([]);

  const handleClick = () => {
    getKeyCards().then((result) => {
      setCards(result);
    });
  };

  return (
    <div className="cards-list">
      <button onClick={handleClick}>Create deck</button>
      <div className="hand hhand active-hand">
        {cards &&
          cards.map((card) => {
            const image = `/images/cards/${card.value}${card.suit}.svg`;
            return <img className="card" src={image} />;
          })}
      </div>
    </div>
  );
};

export default CardsList;
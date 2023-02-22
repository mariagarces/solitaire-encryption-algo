import React from "react";
import { useState } from "react";
import { getKeyCards, getKeyCardsShuffle } from "../../services/encryptionService";
import "./CardsList.css";

const CardsList = ({ enabled, cards, handleCreateClick, handleShuffleClick }) => {

  return (
    <div className="cards-list">
      {enabled && <button onClick={handleCreateClick}>Create deck</button>}
      {!enabled && <button onClick={handleShuffleClick}>Shuffle</button>}
      <div className="hand hhand active-hand">
        {cards &&
          cards.map((card) => {
            const image = `/images/cards/${card.value}${card.suit}.svg`;
            return <img key={`${card.value}-${card.suit}`} className="card" src={image} />;
          })}
      </div>
    </div>
  );
};

export default CardsList;
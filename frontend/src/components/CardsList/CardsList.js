import React from "react";
import { useState, useEffect } from "react";
import "./CardsList.css";

const CardsList = ({
  cards,
  handleCreateClick,
  handleShuffleClick,
  swapCards,
  handleSubmitCards,
}) => {
  const [list, setList] = useState([]);

  useEffect(() => {
    if (list.length === 2) {
      swapCards(list[0].index, list[1].index);
      setList([]);

      const elements = document.querySelectorAll(".selected");
      setTimeout(() => {
        elements.forEach((element) => {
          element.classList.remove("selected");
        });
      }, 1000);
    }
  }, [list]);

  const handleClick = (event) => {
    event.target.classList.add("selected");
    const index = cards.findIndex((card) => {
      const split = event.target.id.split(/(\d+)/);
      return card.value == split[1] && card.suit == split[2];
    });
    setList((prevItems) => [...prevItems, { index, card: event.target.id }]);
  };

  return (
    <div className="cards-list">
      <div className="cards-list-buttons">
        <button className="btn-restart" onClick={handleCreateClick}>
          Restart deck
        </button>
        <button className="btn-shuffle" onClick={handleShuffleClick}>
          Shuffle
        </button>
      </div>
      <div className="hand hhand active-hand">
        {cards &&
          cards.map((card) => {
            const id = card.value + card.suit;
            const image = `/images/cards/${id}.svg`;
            return (
              <img
                id={id}
                onClick={handleClick}
                key={id}
                className="card"
                src={image}
              />
            );
          })}
      </div>
      <button className="btn-submit" onClick={handleSubmitCards}>
        Submit cards
      </button>
    </div>
  );
};

export default CardsList;

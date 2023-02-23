import "./App.css";
import { useState, useEffect } from "react";
import {
  getEncryptedMessage,
  postMessage,
  getDecryptedMessage,
  postCards,
  getCardsCurrentState
} from "./services/encryptionService";

import Deck from "./models/Deck";
import CardsList from "./components/CardsList/CardsList";
import MessageForm from "./components/MessageForm/MessageForm";

function App() {
  const [message, setMessage] = useState([]);
  const [disabledE, setDisabledE] = useState(true);
  const [disabledD, setDisabledD] = useState(true);
  const [msgValue, setMsgValue] = useState("");
  const [cards, setCards] = useState([]);
  const [messageLoaded, setMessageLoaded] = useState(false);
  const [decMessage, setDecMessage] = useState([]);
  const [currentMessage, setCurrentMessage] = useState("");
  const [hasSubmittedCards, setHasSubmittedCards] = useState(false);
  const [hasSubmittedMsg, setHasSubmittedMsg] = useState(false);
  const deck = new Deck();

  useEffect(() => {
    setCards(deck.getDeck());
  }, []);

  useEffect(() => {
    if (msgValue !== "" && cards.length !== 0 && hasSubmittedCards && hasSubmittedMsg) setDisabledE(false);
    else setDisabledE(true);
  }, [cards, msgValue, hasSubmittedCards, hasSubmittedMsg]);

  const handleChangeMessage = (event) => {
    setMsgValue(event.target.value);
  };

  const handleEncryptClick = () => {
    getEncryptedMessage().then((result) => {
      setMessage(result);
      setMsgValue("");
      setDisabledD(false);
      setHasSubmittedCards(false);
    });

    getCardsCurrentState().then((result) => {
      setCards(result);
    });
  };

  const handleDecryptClick = () => {
    getDecryptedMessage().then((result) => {
      setDecMessage(result);
      setDisabledD(true);
    });
  };

  const handlePostClick = () => {
    postMessage(msgValue).then(() => {
      setMessageLoaded(true);
      setMessage("");
      setDecMessage("");
      setCurrentMessage(msgValue.toUpperCase());
      setHasSubmittedMsg(true);
    });
  };

  const handleCreateClick = () => {
    deck.build();
    const newDeck = deck.getDeck();
    setCards(newDeck);
  };

  const handleShuffleClick = () => {
    deck.shuffle();
    const newDeck = deck.getDeck();
    setCards(newDeck);
  };

  const swapCards = (from, to) => {
    const newCards = [...cards];
    [newCards[from], newCards[to]] = [newCards[to], newCards[from]];
    setCards(newCards)
  }

  const handleSubmitCards = () => {
    postCards(cards).then(() => {
      setHasSubmittedCards(true);
    });
  }

  return (
    <div className="App">
      <MessageForm
        handleChange={handleChangeMessage}
        handleClick={handlePostClick}
        message={msgValue}
      />
      {messageLoaded && <p>Message loaded: {currentMessage}</p>}
      <CardsList
        cards={cards}
        handleCreateClick={handleCreateClick}
        handleShuffleClick={handleShuffleClick}
        swapCards={swapCards}
        handleSubmitCards={handleSubmitCards}
      />
      <button disabled={disabledE} onClick={handleEncryptClick}>
        Encrypt message
      </button>
      {message}
      <button disabled={disabledD} onClick={handleDecryptClick}>
        Decrypt message
      </button>
      {decMessage}
    </div>
  );
}

export default App;

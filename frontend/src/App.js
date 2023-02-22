import "./App.css";
import { useState, useEffect } from "react";
import {
  getEncryptedMessage,
  postMessage,
  getKeyCards,
  getKeyCardsShuffle,
  getDecryptedMessage,
  getCardsCurrentState,
} from "./services/encryptionService";

import CardsList from "./components/CardsList/CardsList";
import MessageForm from "./components/MessageForm/MessageForm";

function App() {
  const [message, setMessage] = useState([]);
  const [disabledE, setDisabledE] = useState(true);
  const [disabledD, setDisabledD] = useState(true);
  const [msgValue, setMsgValue] = useState("");
  const [cards, setCards] = useState([]);
  const [enabledButtons, setEnabledButtons] = useState(true);
  const [messageLoaded, setMessageLoaded] = useState(false);
  const [decMessage, setDecMessage] = useState([]);
  const [currentMessage, setCurrentMessage] = useState("");

  useEffect(() => {
    if (msgValue !== "" && cards.length !== 0) setDisabledE(false);
    else setDisabledE(true);
  }, [cards, msgValue]);

  const handleChangeMessage = (event) => {
    setMsgValue(event.target.value);
  };

  const handleEncryptClick = () => {
    getEncryptedMessage().then((result) => {
      setMessage(result);
      setMsgValue("");
      setDisabledD(false);
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
    });
  };

  const handleCreateClick = () => {
    getKeyCards().then((result) => {
      setCards(result);
      setEnabledButtons(false);
    });
  };

  const handleShuffleClick = () => {
    getKeyCardsShuffle().then((result) => {
      setCards(result);
    });
  };

  return (
    <div className="App">
      <MessageForm
        handleChange={handleChangeMessage}
        handleClick={handlePostClick}
        message={msgValue}
      />
      {messageLoaded && <p>Message loaded: {currentMessage}</p>}
      <CardsList
        enabled={enabledButtons}
        cards={cards}
        handleCreateClick={handleCreateClick}
        handleShuffleClick={handleShuffleClick}
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

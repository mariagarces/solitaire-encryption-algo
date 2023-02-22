import "./App.css";
import { useState, useEffect } from "react";
import {
  getEncryptedMessage,
  postMessage,
  getKeyCards,
  getKeyCardsShuffle,
} from "./services/encryptionService";

import CardsList from "./components/CardsList/CardsList";
import MessageForm from "./components/MessageForm/MessageForm";

function App() {
  const [message, setMessage] = useState([]);
  const [disabled, setDisabled] = useState(true);
  const [msgValue, setMsgValue] = useState("");
  const [cards, setCards] = useState([]);
  const [enabledButtons, setEnabledButtons] = useState(true);
  const [messageLoaded, setMessageLoaded] = useState(false);

  useEffect(() => {
    if (msgValue !== "" && cards.length !== 0) setDisabled(false);
    else setDisabled(true);
  }, [cards, msgValue]);

  const handleChangeMessage = (event) => {
    setMsgValue(event.target.value);
  };

  const handleEncryptClick = () => {
    getEncryptedMessage().then((result) => {
      setMessage(result);
      setMsgValue("");
    });
  };

  const handlePostClick = () => {
    postMessage(msgValue).then(() => {
      setMessageLoaded(true);
      setTimeout(() => {
        setMessageLoaded(false);
      }, 1500);
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
      {messageLoaded && <p>Message loaded</p>}
      <CardsList
        enabled={enabledButtons}
        cards={cards}
        handleCreateClick={handleCreateClick}
        handleShuffleClick={handleShuffleClick}
      />
      <button disabled={disabled} onClick={handleEncryptClick}>
        Encrypt message
      </button>
      {message}
    </div>
  );
}

export default App;

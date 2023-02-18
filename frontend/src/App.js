import "./App.css";
import { useState } from "react";
import { getEncryptedMessage } from "./services/encryptionService";

import CardsList from "./components/CardsList/CardsList";
import MessageForm from "./components/MessageForm/MessageForm";

function App() {
  const [message, setMessage] = useState([]);

  const handleClick = () => {
    getEncryptedMessage().then((result) => {
      setMessage(result);
    });
  };
  return (
    <div className="App">
      <MessageForm />
      <CardsList />
      <button onClick={handleClick}>Encrypt message</button>
      {message}
    </div>
  );
}

export default App;

import React from "react";
import { useState } from "react";
import { postMessage } from "../../services/encryptionService";

const MessageForm = () => {
  const [message, setMessage] = useState("");

  const handleClick = () => {
    postMessage(message).then((result) => {
      console.log(result);
    });
  };

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  return (
    <div className="message-form">
        <label>
          Write message
          <input type="text" onChange={handleChange} />
        </label>
        <button click="submit" onClick={handleClick}>Submit</button>
    </div>
  );
};

export default MessageForm;

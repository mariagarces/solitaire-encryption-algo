import React from "react";
import { useState, useEffect } from "react";

const MessageForm = ({ message, handleChange, handleClick }) => {
  const [disabled, setDisabled] = useState(true);

  useEffect(() => {
    if (message === "") setDisabled(true);
    else setDisabled(false);
  }, [message]);

  return (
    <div className="message-form">
      <label>
        Write message
        <input value={message} type="text" onChange={handleChange} />
      </label>
      <button disabled={disabled} click="submit" onClick={handleClick}>
        Submit
      </button>
    </div>
  );
};

export default MessageForm;

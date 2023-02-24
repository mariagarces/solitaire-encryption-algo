import React from "react";
import { useState, useEffect } from "react";
import './MessageForm.css';

const MessageForm = ({ message, handleChange, handleClick }) => {
  const [disabled, setDisabled] = useState(true);

  useEffect(() => {
    if (message === "") setDisabled(true);
    else setDisabled(false);
  }, [message]);

  return (
    <div className="message-form">
      <label className="label-form">
        Message
        <input className="input-form" value={message} type="text" onChange={handleChange} />
      </label>
      <button disabled={disabled} click="submit" onClick={handleClick}>
        Submit
      </button>
    </div>
  );
};

export default MessageForm;

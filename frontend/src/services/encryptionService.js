import axios from "axios";

const URL = "http://localhost:8000";

const getKeyCards = async () => {
  const { data } = await axios.get(URL + "/cards");
  return data.cards;
};

const getKeyCardsShuffle = async () => {
  const { data } = await axios.get(URL + "/cards/shuffle");
  return data.cards;
};

const getCardsCurrentState = async () => {
  const { data } = await axios.get(URL + "/cards/current-state");
  return data.cards;
};

const postMessage = async (message) => {
  const { data } = await axios.post(URL + "/message", {
    message,
  });
  return data.response;
};

const getEncryptedMessage = async () => {
  const { data } = await axios.get(URL + "/message/encrypt");
  return data.message;
};

const getDecryptedMessage = async () => {
  const { data } = await axios.get(URL + "/message/decrypt");
  return data.message;
};

export {
  getKeyCards,
  postMessage,
  getEncryptedMessage,
  getKeyCardsShuffle,
  getDecryptedMessage,
  getCardsCurrentState
};

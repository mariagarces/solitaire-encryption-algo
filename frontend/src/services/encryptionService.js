import axios from "axios";

const URL = "http://localhost:8000"

const getKeyCards = async () => {
    const { data } = await axios.get(URL+"/cards");
    return data.cards;
}

const postMessage = async (message) => {
    const { data } = await axios.post(URL+"/message", {
      message,
    })
    return data.response;
}

const getEncryptedMessage = async () => {
    const { data } = await axios.get(URL+"/message/encrypt");
    return data.message;
}

export {getKeyCards, postMessage, getEncryptedMessage}
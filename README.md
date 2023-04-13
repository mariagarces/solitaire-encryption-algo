# Solitaire Cipher
This project is an implementation of the Solitaire Cipher algorithm created by Bruce Schneier. The algorithm is based on a deck of cards, and it uses a series of steps to shuffle the deck and generate a key stream, which is then used to encrypt and decrypt messages.

## Getting Started
To get started with this project, you will need to have Python 3 and Node.js installed on your computer. You can download Python from the official website (https://www.python.org/downloads/) and Node.js from the Node.js website (https://nodejs.org/en/download/).

Once you have Python and Node.js installed, you can clone this repository to your local machine:
```
git clone https://github.com/mariagarces/solitaire-encryption-algo.git
```

Next, navigate to the project directory and install the required dependencies for both the Python and React components:
```
cd backend
pip install -r requirements.txt

cd frontend
npm install
```

Finally, you can start the FastAPI server and the React app:
```
cd backend
uvicorn src.api:app --reload

cd frontend
npm run start

## Usage
Once the server and the React app are running, you can use the Solitaire Cipher to encrypt and decrypt messages. Simply type in your message, choose the order of the card and click the "Submit" button for each area. Whether you want to encrypt or decrypt it click the corresponding button, and the app will generate a key stream using the Solitaire Cipher algorithm and use it to encrypt or decrypt your message.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

import Card from "./Card";

export default class Deck {
  constructor(cards = []) {
    this.cards = cards;
    if (cards.length === 0) this.build();
  }

  build() {
    this.cards = [];
    const suits = ["C", "D", "H", "S"];
    const values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
    for (const s of suits) {
      for (const v of values) {
        this.cards.push(new Card(s, v));
      }
    }
    this.cards.push(new Card("BJ", 53));
    this.cards.push(new Card("RJ", 53));
  }

  shuffle() {
    for (let i = this.cards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.cards[i], this.cards[j]] = [this.cards[j], this.cards[i]];
    }
  }

  getDeck() {
    return this.cards;
  }
}

import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";

import CardsList from "./CardsList";

describe("<CardsList />", () => {
  it("should render buttons", () => {
    render(<CardsList />);

    const buttons = screen.getAllByRole("button");

    expect(buttons.length).toBe(3);

    expect(buttons[0].textContent).toBe("Restart deck");
    expect(buttons[1].textContent).toBe("Shuffle");
    expect(buttons[2].textContent).toBe("Enregistrer les cartes");
  });

  it("should render cards", () => {
    const list_cards = [{suit: "C", value: 10},{suit: "C", value: 11}]
    const url = (suit, value) => `/images/cards/${value + suit}.svg`;
    render(<CardsList cards={list_cards}/>);

    const cards = screen.getAllByRole("img");

    expect(cards.length).toBe(2);

    expect(cards[0]).toHaveAttribute('src', url(list_cards[0].suit, list_cards[0].value))
    expect(cards[1]).toHaveAttribute('src', url(list_cards[1].suit, list_cards[1].value))
  });

  it("should click save button", () => {
    const handleSubmitCards = jest.fn();
    render(<CardsList handleSubmitCards={handleSubmitCards}/>);

    const buttons = screen.getAllByRole("button");

    fireEvent.click(buttons[2]);
    expect(handleSubmitCards).toHaveBeenCalledTimes(1);
  });
});
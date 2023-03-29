import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";

import MessageForm from "./MessageForm";

describe("<MessageForm />", () => {
  it("should render component", () => {
    render(<MessageForm />);

    const button = screen.getAllByRole("button");
    const label = screen.getByLabelText("Message");

    expect(button.length).toBe(1);
    expect(button[0].textContent).toBe("Submit");
    expect(label).toBeInTheDocument();
  });

  it("should click button", () => {
    const handleChange = jest.fn();
    render(<MessageForm message="" handleChange={handleChange}/>);

    const button = screen.getAllByRole("button");
    const input = screen.getByLabelText("Message")

    expect(button[0]).toHaveAttribute("disabled");
    fireEvent.change(input, {target: {value: 'test'}});
    fireEvent.click(button[0]);
    expect(handleChange).toHaveBeenCalledTimes(1);
  });
});
#!/usr/bin/env python3
# Coffee class represents a product sold in a bookstore café
# It handles size validation and price updates when a tip is added

class Coffee:
    # pass
  def __init__(self, size, price):
        # Store coffee size and price when object is created
        # Size must be validated through the setter
        self.size = size
        self.price = price

  @property
  def size(self):
        # Returns the current coffee size
        return self._size

  @size.setter
  def size(self, value):
        # Ensures only valid coffee sizes are allowed
        # Prevents invalid menu items from being assigned
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

  def tip(self):
        # Simulates a customer tipping after good service
        # Increases price to reflect added tip value
        print("This coffee is great, here’s a tip!")
        self.price += 1
   # Cafe Management System

Welcome to the **Cafe Management System**! This Python script allows you to simulate a simple cafe order-taking process, where users can choose items from a menu and get a total bill based on their selections.

## Features

- **Menu Display**: The cafe offers a variety of drinks, each with a specific price.
- **Order Taking**: Users can place an order by selecting an item from the menu.
- **Order Confirmation**: The system confirms the user's order and asks if they would like to place an additional order.
- **Bill Calculation**: The total bill is calculated based on the user's selections.

## Menu

The current menu items and their prices are:

- **Latte**: ₹90
- **Mocha**: ₹79
- **Espresso**: ₹69
- **Doppio**: ₹57
- **Tea**: ₹37

## How to Use

1. Run the script.
2. Enter your name when prompted.
3. View the menu and place your order by typing the name of the drink.
4. If you want to place another order, type "yes" when asked.
5. The system will confirm your orders and display the total bill.

## Example

```python
# Example interaction with the script:
# Enter ur name:
# --> Azad
# Welcome to Azad Cafe, Azad
# Our cafe menu is: {'latte': 90, 'mocha': 79, 'espresso': 69, 'doppio': 57, 'tea': 37}
# What would you like to order? latte
# Your order latte is confirmed.
# Do you want to order something else? yes
# What do you want for your second order? tea
# Your second order is confirmed. Your total bill is ₹127.
```

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cafe-management.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cafe-management
   ```
3. Run the script:
   ```bash
   python cafe_management.py
   ```

## Contributing

Feel free to fork this project, submit issues, and contribute by submitting pull requests. Let's make this cafe management system even better!

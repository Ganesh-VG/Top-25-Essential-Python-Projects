# Coffee Making Machine OOP Project

## Overview

This project simulates a coffee-making machine using Object-Oriented Programming (OOP) principles in Python. The program models the various components and functionalities of a coffee machine, allowing users to interact with it by selecting different types of coffee, managing resources, and handling transactions.

## Features

- **Coffee Menu:** The machine offers multiple types of coffee (e.g., espresso, latte, cappuccino), each with specific resource requirements.
- **Resource Management:** The machine tracks the availability of ingredients (water, milk, coffee, etc.) and updates the inventory as coffee is made.
- **Transaction Handling:** The machine processes payments and provides change if necessary.
- **Maintenance:** The machine can be refilled with ingredients and turned off for maintenance.

## Class Structure

### 1. `CoffeeMachine`
- Manages the overall state of the machine.
- Handles user interactions, such as selecting coffee and processing payments.
- Interfaces with other classes to manage resources and transactions.

### 2. `MenuItem`
- Represents an individual coffee option.
- Stores the name, cost, and ingredient requirements for each coffee type.

### 3. `Menu`
- Contains a list of available coffee options (`MenuItem` instances).
- Provides functionality to display the menu and find coffee by name.

### 4. `Resources`
- Manages the inventory of ingredients.
- Provides methods to check if resources are sufficient for a selected coffee.
- Updates the inventory as ingredients are used or refilled.

### 5. `Transaction`
- Handles monetary transactions.
- Calculates and processes the total cost, payments, and change.

## Example Usage

1. **Displaying the Menu:**
   ```python
   menu = Menu()
   menu.display()
   ```

2. **Selecting a Coffee:**
   ```python
   selected_coffee = menu.find_coffee("latte")
   ```

3. **Checking Resources:**
   ```python
   resources = Resources()
   if resources.is_sufficient(selected_coffee):
       # Proceed with making coffee
   ```

4. **Processing Payment:**
   ```python
   transaction = Transaction()
   if transaction.process_payment(selected_coffee.cost):
       # Complete the transaction
   ```

5. **Updating Resources:**
   ```python
   resources.use_ingredients(selected_coffee)
   ```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/coffee-machine-oop.git
   cd coffee-machine-oop
   ```

2. **Run the Program:**
   ```bash
   python main.py
   ```

## Conclusion

This project demonstrates the use of OOP principles to model a real-world system. It effectively encapsulates different functionalities into classes, providing a clean and modular approach to building a coffee-making machine simulation. The project can be expanded with additional features such as user authentication, more coffee options, and advanced inventory management.

![1719367433432](https://github.com/user-attachments/assets/7a44f673-a55f-40fe-adf9-3256e611c283)

## Future Enhancements

- Add more coffee types and customizations.
- Implement user authentication for personalized experiences.
- Enhance the user interface with a graphical front-end.

# Supermarket Billing System 🛒

This is a **Supermarket Billing System** built using Python and Tkinter. It provides a graphical interface for managing items, processing customer purchases, and generating detailed bills. The system integrates MySQL to store and manage item information and track inventory.

---

## Features ✨

- **Add Items**: Users can add new items to the inventory with details like name, price, and quantity.
- **Purchase Items**: Users can input item names and quantities to calculate the total bill, automatically updating the inventory.
- **Print Bill**: Generates a detailed bill with purchased items and total amount.
- **Real-Time Inventory Update**: Reduces item quantity in real-time after a purchase.
- **Error Handling**: Validates item availability and quantity before proceeding with a purchase.

---

## Technologies Used 💻

- **Frontend**: Python (Tkinter for GUI)
- **Backend**: MySQL (pymysql for database integration)

---

## Setup Instructions ⚙️

1. **Install Required Libraries**:
   - Install Python (v3.7 or above).
   - Install MySQL and ensure it's running on your system.
   - Install the `pymysql` library using the command:
     ```bash
     pip install pymysql
     ```

2. **Database Configuration**:
   - Create a MySQL database named `billdb`.
   - Create a table named `item` with the following structure:
     ```sql
     CREATE TABLE item (
         item_name VARCHAR(255),
         item_price FLOAT,
         item_quant INT
     );
     ```

3. **Run the Application**:
   - Clone this repository:
     ```bash
     git clone https://github.com/your-username/supermarket-billing-system.git
     cd supermarket-billing-system
     ```
   - Execute the script:
     ```bash
     python supermarket_billing_system.py
     ```

---

## How It Works 🔧

1. **Launch the Application**:
   - The main screen displays options to manage items, make purchases, and print bills.

2. **Add Items**:
   - Users can add new items to the inventory with their name, price, and quantity.

3. **Purchase Items**:
   - Users input the item name and quantity to calculate the total cost and update inventory.

4. **Print Bill**:
   - The system generates and displays the bill with the total amount and purchased items.

5. **Inventory Update**:
   - The quantity of items in the inventory is updated after every purchase.

6. **Error Handling**:
   - The system validates whether the required quantity of an item is available before a purchase.

---

## Screenshots 🖼️

*Include screenshots of the application, such as the item management screen, purchase screen, and bill generation.*

---

## Future Enhancements 🚀

- Add a feature to print bills as PDFs.
- Improve the user interface for better experience and usability.
- Add the ability to edit or delete items from the inventory.
- Implement a login system for multiple users with different access levels.

---

## License 📜

This project is open-source and available under the [MIT License](LICENSE).

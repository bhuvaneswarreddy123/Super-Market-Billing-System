# Super Market Billing System 🛒

This is a Super Market Billing System built using Python and Tkinter. It provides an easy-to-use graphical interface for managing items, tracking inventory, and generating customer bills.

Features ✨

Add New Items: Add items to the inventory with their name, price, and quantity.
Purchase Items: Enter the item name and quantity to calculate the total price and update inventory.
Real-Time Inventory Update: Automatically reduces item quantity after each purchase.
Print Bill: Displays a detailed bill with all purchased items and the total amount.

Technologies Used 🛠️

Python: For backend logic and functionality.
Tkinter: To create a graphical user interface (GUI).
MySQL: For storing and managing inventory data.

How to Run 🚀

1.Install Python and MySQL on your system.
2.Clone this repository to your local machine.
3.Create a database named billdb in MySQL and add a table named item with the following columns:
  .item_name (VARCHAR)
  .item_price (FLOAT)
  .item_quant (INT)
4.Run the Below code to establish connection between mysql and python code

  con = pymysql.connect(host="localhost",user="root",passwd="your_password",database="billdb")

5.Run the Python file to launch the application

  python your_file_name.py






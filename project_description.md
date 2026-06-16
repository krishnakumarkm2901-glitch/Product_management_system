# Product Management System

## Description

The **Product Management System** is a console-based application developed using **Python Object-Oriented Programming (OOP)** concepts. The system stores product information in a **JSON file**, allowing data to be saved permanently between program executions.

It provides complete **CRUD (Create, Read, Update, Delete)** operations through a simple menu-driven interface, making it easy to manage product records.

## Features

* Add new products
* View all product details in a formatted table
* Search products using Product ID
* Update existing product information
* Delete products by Product ID
* Store product records in a JSON file
* Menu-driven console application
* Implemented using Python classes and objects

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON File Handling
* OS Module

## Product Details

Each product contains the following information:

* Product ID
* Product Name
* Category
* Price
* Stock Quantity

## Project Structure

```text
Product_Management_System/
│── product_management.py
│── Product.json
└── README.md
```

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Run the Python file:

```bash
python product_management.py
```

4. Choose an option from the menu:

   * Add Product
   * View Products
   * Search Product
   * Update Product
   * Delete Product
   * Exit

## Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Methods
* Object Serialization using JSON
* File Handling
* Lists and Dictionaries
* Conditional Statements
* Loops

## Future Improvements

* Prevent duplicate Product IDs
* Add input validation
* Auto-generate Product IDs
* Search by Product Name or Category
* Sort products by Price or Name
* Improve exception handling

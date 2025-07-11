# 🏦 Python Banking System

## Overview

The **Python Banking System** is a console-based application designed to simulate the basic functionalities of a bank. This system supports both administrative and customer-level operations, including account management, secure logins, financial transactions, and data persistence.

## Features

### 🔐 Admin Features

* Secure login system for administrators.
* Admin permissions (full rights or limited).
* Customer account management:

  * View, edit, or delete customer profiles.
  * Manage customer transactions.
* Bank-wide financial overview:

  * Total customer count.
  * System-wide balance and interest reports.
  * Overdraft tracking.

### 👥 Customer Features

* Normal and saving account types.
* Balance inquiries.
* Deposits and withdrawals.
* Personal information updates.

### 🔄 Data Persistence

* Reads from `bank_information_storage.json`.
* Saves updates to `updated_bank_info.json`.
* All customer and admin information is stored and retrieved using JSON.

## Project Structure

```
├── bank_system.py               # Main application logic
├── customer_account.py         # Customer account classes and operations
├── admin.py                    # Admin class and permissions
├── person.py                   # Base class for common personal details
├── bank_information_storage.json  # Original dataset
├── updated_bank_info.json      # Updated dataset after any operation
├── README.md                   # Project documentation
```

## Getting Started

### 📦 Requirements

* Python 3.6 or higher

### 🚀 Running the Application

```bash
python bank_system.py
```

Once the program is executed, follow the command-line prompts to:

* Log in as an admin.
* Access account management tools.
* Perform banking operations.

## 📁 Data Format

### Customer Example:

```json
{
  "fname": "Adam",
  "lname": "Smith",
  "address": ["14", "Wilcot Street", "Bath", "B5 5RT"],
  "account_no": 1234,
  "balance": 5000.00,
  "account_type": "normal_account"
}
```

### Admin Example:

```json
{
  "fname": "Julian",
  "lname": "Padget",
  "address": ["12", "London Road", "Birmingham", "B95 7TT"],
  "user_name": "id1188",
  "password": "1441",
  "full_rights": true
}
```

## ⚙️ Object-Oriented Structure

* Inherits from a common `Personal_details` class.
* Two main account types: `saving_account` and `normal_account`.
* Admins managed via the `Admin` class with role-based access control.

## 📈 Reporting Capabilities

* Calculates interest on saving accounts.
* Tracks total and overdraft balances.
* Generates real-time system reports for administrative insight.

## 🧪 Sample Use Cases

* Transferring money between accounts.
* Deleting customer accounts (admin only).
* Updating personal details.
* Viewing customer data summaries.

## 🔐 Security

* Admin login required for sensitive operations.
* Role-based access limits destructive actions.



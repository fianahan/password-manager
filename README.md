# Password Manager

A simple Python-based password manager that allows users to securely store, retrieve, and manage login credentials for different websites.

## Overview

This project was created to practice core Python programming concepts, including file handling, JSON storage, functions, and menu-driven user interaction. It helps users save credentials for multiple sites and quickly retrieve them when needed.

## Features

- Save a website name, username, and password
- Retrieve saved credentials for a specific site
- Store data in a JSON file
- Simple command-line interface
- Beginner-friendly and easy to extend

## Tech Stack

- Python 3
- JSON
- OS module

## Project Structure

```text
password-manager/
├── password_manager.py
├── passwords.json
├── README.md

## How It Works
The program stores passwords in a dictionary format and saves them to a JSON file. Each entry contains:
- site name
- username
- password
When the user wants to retrieve a password, the program reads the saved data and displays the credentials for the selected site.

## Run the Project
python password_manager.py

## Example Menu
**Password Manager**
1. Save Password
2. Get Password
3. Exit

## Example Flow
Enter your choice: 1
Enter site name: Gmail
Enter username: exampleuser
Enter password: mypassword123
Password saved successfully!

Then:
Enter your choice: 2
Enter site name: Gmail
Site: Gmail
Username: exampleuser
Password: mypassword123

## What I Learned
- Writing reusable functions in Python
- Using dictionaries to store structured data
- Working with JSON files for data persistence
- Handling user input through a command-line menu
- Implementing basic CRUD-style functionality in a small project

## Project Purpose
This project demonstrates foundational software development skills, including logic building, data management, and practical Python programming. It is a simple but effective example of a real-world utility application.

Author
Fiana Han



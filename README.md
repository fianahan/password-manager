# password-manager
## A simple, beginner‑friendly Python password manager that stores login credentials locally in a JSON file. This project demonstrates core Python fundamentals, file handling, and simple data persistence.

## Features
- Save passwords for any website or service
- Retrieve stored login credentials
- JSON-based storage (easy to read and modify)
- Lightweight and beginner-friendly

## Project Structure
password-manager/
│
├── main.py          # Core logic for saving and retrieving passwords
├── passwords.json   # Local storage file
└── README.md        # Project documentation

## How It Works
The program checks whether `passwords.json` exists. If not, it creates an empty JSON file.
When saving a password, it updates the JSON with a new entry containing the username and password.
When retrieving, it loads the JSON and prints the stored credentials.

## Usage
1. Clone the repository:
   git clone https://github.com/fianahan/password-manager.git

2. Run the script:
   python main.py

3. Follow the prompts to save or retrieve passwords.

## Future Improvements
- Add encryption for stored passwords
- Add a GUI (Tkinter or PyQt)
- Add password generation
- Add delete or search functionality

## Author
Created by Fiana Han



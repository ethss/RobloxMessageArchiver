# 📜 Roblox Message Archiver

This script automates the process of archiving private messages on Roblox using the Roblox API. It continuously fetches and archives messages, updating the console with the current status. 

## 🚀 Features

- Automatically fetch and archive private messages from Roblox.
- Displays the total number of messages archived.
- Shows the most recent message ID archived.
- Provides the total time spent archiving messages.
- Color-coded console output for better readability.

## 🛠️ Setup

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Install dependencies**:
    ```bash
    pip install requests termcolor
    ```

3. **Set your Roblox Security Cookie**:
    - Open the `main.py` file.
    - Replace the placeholder in the `cookie` variable with your actual Roblox security cookie.

## 📝 Usage

1. **Run the script**:
    ```bash
    python main.py
    ```

2. The script will continuously archive messages and update the console with the current status.

## 📊 Console Output

- **Yellow**: CSRF Token
- **Cyan**: Total Messages Archived & Most Recent Message ID Archived
- **Green**: Successfully Archived Message IDs
- **Red**: No messages to archive or failed to retrieve messages
- **Final Message**: Total Time Spent archiving messages

## ⚠️ Warning

🔒 **Do not share your Roblox security cookie**. Sharing this will allow someone to log in as you and potentially steal your ROBUX and items.

## 🛠️ Troubleshooting

- Ensure you have a stable internet connection.
- Verify that your Roblox security cookie is valid.
- Make sure the Roblox API endpoints are accessible.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](#).

## 🙏 Acknowledgements

- [Roblox API Documentation](https://developer.roblox.com/en-us/api-reference)
- [Requests Library](https://docs.python-requests.org/en/master/)
- [Termcolor Library](https://pypi.org/project/termcolor/)

---

Made with ❤️ by ETHS

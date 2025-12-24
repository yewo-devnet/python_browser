# PyQt5 Web Browser

## Project Overview

This project is a **general-purpose desktop web browser** built using **PyQt5** and **Qt WebEngine**. It demonstrates how Python can be used to create a functional graphical web browser with core navigation features similar to modern browsers.

---

## Key Features

- General web browsing using Qt WebEngine
- Back and forward navigation
- Page refresh (reload)
- Home button (Google homepage)
- Unified address/search bar
  - Automatically detects URLs
  - Treats plain text or incomplete input as a Google search
- Dynamic URL bar updates as pages change

---

## Technologies Used

- **Python 3**
- **PyQt5** (GUI framework)
- **PyQtWebEngine** (Chromium-based web rendering engine)

---

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.7 or higher
- PyQt5
- PyQt5 WebEngine

Install dependencies using:

```bash
pip install PyQt5 PyQt5-WebEngine
```

---

## Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/yewo-devnet/python_browser.git
cd python_browser
```

2. **Install Dependencies**:

```bash
pip install PyQt5 PyQt5-WebEngine
```

---

## Project Structure

```
python_browser/
├── browser.py
└── README.md
```

---

## Usage

1. **Run the Application**:

```bash
python browser.py
```

2. **Browsing the Web**:

- Enter a full URL (e.g., `https://www.wikipedia.org`) and press **Enter**
- Enter a domain without protocol (e.g., `google.com`) and it will be resolved automatically
- Enter a search query (e.g., `computer networks`) and the browser will perform a Google search

3. **Navigation Controls**:

- `<` : Go back to the previous page
- `>` : Go forward
- `⟳` : Reload the current page
- `⌂` : Navigate to the Google homepage

---

## How URL Handling Works

- If the input contains spaces or does not resemble a domain, it is treated as a Google search
- If the input looks like a domain but lacks a protocol, `http://` is automatically added
- Valid URLs are loaded directly in the browser

This logic provides a smooth, browser-like user experience similar to mainstream browsers.

---

## Future Improvements

- Tabbed browsing
- Bookmarks and history management
- Download manager
- Dark mode / custom themes
- Improved URL validation and error handling

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DevNet Web Browser")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Top Navigation Bar
        self.top_bar = QHBoxLayout()

        # Navigation Buttons
        self.btn_back = QPushButton("<")
        self.btn_forward = QPushButton(">")
        self.btn_refresh = QPushButton("⟳") # Refresh symbol or text
        self.btn_home = QPushButton("⌂")    # House symbol or text

        self.btn_back.clicked.connect(self.go_back)
        self.btn_forward.clicked.connect(self.go_forward)
        self.btn_refresh.clicked.connect(self.reload_page)
        self.btn_home.clicked.connect(self.load_homepage)

        # Search/URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search Google or enter URL")
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Add widgets to top bar
        self.top_bar.addWidget(self.btn_back)
        self.top_bar.addWidget(self.btn_forward)
        self.top_bar.addWidget(self.btn_refresh)
        self.top_bar.addWidget(self.btn_home)
        self.top_bar.addWidget(self.url_bar)

        self.layout.addLayout(self.top_bar)

        # Web Browser View
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        # Update URL bar when page changes
        self.browser.urlChanged.connect(self.update_url_bar)

        self.load_homepage()

    def load_homepage(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        text = self.url_bar.text().strip()
        if not text:
            return

        # Simple check if it's a URL or a search query
        # If it contains spaces or doesn't look like a domain, treat as search
        if " " in text or "." not in text:
             url = f"https://www.google.com/search?q={text}"
        else:
            if not text.startswith("http://") and not text.startswith("https://"):
                url = "http://" + text
            else:
                url = text
        
        self.browser.setUrl(QUrl(url))

    def go_back(self):
        self.browser.back()

    def go_forward(self):
        self.browser.forward()

    def reload_page(self):
        self.browser.reload()

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.resize(1024, 768)
    browser.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to their respective API call methods
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def _show_message_box(self, title, message, icon=QMessageBox.Information):
        """Helper function to display a QMessageBox."""
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def _handle_api_error(self, endpoint, error):
        """Helper function to handle API request exceptions."""
        print(f"Error connecting to {endpoint}: {error}")
        self._show_message_box(
            "Connection Error",
            f"Could not connect to the RSA API at {endpoint}. Please ensure the server is running.",
            QMessageBox.Critical
        )

    def call_api_gen_keys(self):
        """Calls the API to generate RSA keys."""
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self._show_message_box("Key Generation", data.get("message", "Keys generated successfully!"))
            else:
                error_message = response.json().get("message", "Unknown error during key generation.")
                self._show_message_box("API Error", f"Error generating keys: {error_message}", QMessageBox.Warning)
                print(f"Error while calling API for key generation: Status {response.status_code}, Response: {response.text}")
        except requests.exceptions.RequestException as e:
            self._handle_api_error(url, e)

    def call_api_encrypt(self):
        """Calls the API to encrypt a message."""
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data.get("encrypted_message", ""))
                self._show_message_box("Encryption Status", "Message encrypted successfully!")
            else:
                error_message = response.json().get("message", "Unknown error during encryption.")
                self._show_message_box("API Error", f"Error encrypting message: {error_message}", QMessageBox.Warning)
                print(f"Error while calling API for encryption: Status {response.status_code}, Response: {response.text}")
        except requests.exceptions.RequestException as e:
            self._handle_api_error(url, e)

    def call_api_decrypt(self):
        """Calls the API to decrypt a message."""
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data.get("decrypted_message", ""))
                self._show_message_box("Decryption Status", "Message decrypted successfully!")
            else:
                error_message = response.json().get("message", "Unknown error during decryption.")
                self._show_message_box("API Error", f"Error decrypting message: {error_message}", QMessageBox.Warning)
                print(f"Error while calling API for decryption: Status {response.status_code}, Response: {response.text}")
        except requests.exceptions.RequestException as e:
            self._handle_api_error(url, e)

    def call_api_sign(self):
        """Calls the API to sign a message."""
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setText(data.get("signature", ""))
                self._show_message_box("Signing Status", "Message signed successfully!")
            else:
                error_message = response.json().get("message", "Unknown error during signing.")
                self._show_message_box("API Error", f"Error signing message: {error_message}", QMessageBox.Warning)
                print(f"Error while calling API for signing: Status {response.status_code}, Response: {response.text}")
        except requests.exceptions.RequestException as e:
            self._handle_api_error(url, e)

    def call_api_verify(self):
        """Calls the API to verify a message signature."""
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data.get("is_verified", False):
                    self._show_message_box("Verification Status", "Signature verified successfully!")
                else:
                    self._show_message_box("Verification Status", "Signature verification failed!", QMessageBox.Warning)
            else:
                error_message = response.json().get("message", "Unknown error during verification.")
                self._show_message_box("API Error", f"Error verifying signature: {error_message}", QMessageBox.Warning)
                print(f"Error while calling API for verification: Status {response.status_code}, Response: {response.text}")
        except requests.exceptions.RequestException as e:
            self._handle_api_error(url, e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
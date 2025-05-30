from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKey"])
    cipher = CaesarCipher()
    result = cipher.encrypt_text(text, key)
    return f"Encrypted: {result}"

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKey"])
    cipher = CaesarCipher()
    result = cipher.decrypt_text(text, key)
    return f"Decrypted: {result}"

# Vigenère Cipher
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKey"]
    cipher = VigenereCipher()
    result = cipher.encrypt_text(text.upper(), key.upper())
    return f"Encrypted: {result}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKey"]
    cipher = VigenereCipher()
    result = cipher.decrypt_text(text.upper(), key.upper())
    return f"Decrypted: {result}"

# Playfair Cipher
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKey"]
    cipher = PlayfairCipher()
    result = cipher.encrypt_text(text, key)
    return f"Encrypted: {result}"

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKey"]
    cipher = PlayfairCipher()
    result = cipher.decrypt_text(text, key)
    return f"Decrypted: {result}"

# Rail Fence Cipher
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKey"])
    cipher = RailFenceCipher()
    result = cipher.encrypt_text(text, key)
    return f"Encrypted: {result}"

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKey"])
    cipher = RailFenceCipher()
    result = cipher.decrypt_text(text, key)
    return f"Decrypted: {result}"

# Transposition Cipher
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKey"]
    cipher = TranspositionCipher()
    result = cipher.encrypt_text(text, key)
    return f"Encrypted: {result}"

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKey"]
    cipher = TranspositionCipher()
    result = cipher.decrypt_text(text, key)
    return f"Decrypted: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

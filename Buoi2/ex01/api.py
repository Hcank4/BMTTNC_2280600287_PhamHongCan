from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# CIPHERCIPHER
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# VIGENERE
vigenere = vigenere_cipher.VigenereCipher()

@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.get_json()
    return jsonify({"encrypted_text": vigenere.vigenere_encrypt(data["plain_text"], data["key"])})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.get_json()
    return jsonify({"decrypted_text": vigenere.vigenere_decrypt(data["cipher_text"], data["key"])})

# RAILFENCE
railfence = railfence_cipher.RailFenceCipher()

@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.get_json()
    return jsonify({"encrypted_text": railfence.rail_fence_encrypt(data["plain_text"], int(data["key"]))})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.get_json()
    return jsonify({"decrypted_text": railfence.rail_fence_decrypt(data["cipher_text"], int(data["key"]))})

# PLAYFAIR
playfair = playfair_cipher.PlayFairCipher()

@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_create():
    data = request.get_json()
    return jsonify({"playfair_matrix": playfair.create_playfair_matrix(data["key"])})

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.get_json()
    matrix = playfair.create_playfair_matrix(data["key"])
    return jsonify({"encrypted_text": playfair.playfair_encrypt(data["plain_text"], matrix)})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.get_json()
    matrix = playfair.create_playfair_matrix(data["key"])
    return jsonify({"decrypted_text": playfair.playfair_decrypt(data["cipher_text"], matrix)})

# TRANSPOSITION
trans = transposition_cipher.TranspositionCipher()

@app.route("/api/transposition/encrypt", methods=["POST"])
def trans_encrypt():
    data = request.get_json()
    return jsonify({"encrypted_text": trans.encrypt(data["plain_text"], int(data["key"]))})

@app.route("/api/transposition/decrypt", methods=["POST"])
def trans_decrypt():
    data = request.get_json()
    return jsonify({"decrypted_text": trans.decrypt(data["cipher_text"], int(data["key"]))})

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

class TranspositionCipher:
    def encrypt(self, text, key):
        key = int(key)
        ciphertext = [''] * key
        for column in range(key):
            pointer = column
            while pointer < len(text):
                ciphertext[column] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

    def decrypt(self, text, key):
        key = int(key)
        num_rows = len(text) // key
        if len(text) % key != 0:
            num_rows += 1
        
        num_shaded_boxes = (num_rows * key) - len(text)
        plaintext = [''] * num_rows

        col = 0
        row = 0

        for symbol in text:
            plaintext[row] += symbol
            row += 1
            if (row == num_rows) or (row == num_rows - 1 and col >= key - num_shaded_boxes):
                row = 0
                col += 1

        return ''.join(plaintext)

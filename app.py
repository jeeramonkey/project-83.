from flask import Flask, render_template, request, redirect
import os
# Import encrypt, decrypt, generateKeys from encrypt.py
from encrypt import encrypt, decrypt, generateKeys

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}

# Generate public and private keys using generateKeys function
publicKey, privateKey = generateKeys()

@app.route("/", methods= ["GET", "POST"])
def home():
     return render_template('signup.html')
     
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global blockData
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Excrypt 'password' with encrypt() function and store it back in 'password variable
        password = encrypt(password, publicKey)

        blockData = {
            'username': username,
            'email': email,
            'password': password
        }
        
        
        return redirect('/signin')
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global blockData
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Create plainPasswrod by decrypting blockData['password] with decrypt() function   
        plainPassword = decrypt(blockData['password'], privateKey)

        # Use plainpasswrod to match the passwords instead of blockData['password']
        if blockData['username'] == username and blockData['password'] == password:
                    return render_template('profile.html', block= blockData)

        return "Invalid credentials!"
    return render_template('signin.html')


capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'

def cipher(plaintext, n):
    global  capitalLetters, lowerLetters, numbers
    cipherText = ''

    for char in plaintext:
        if char in numbers:
            currentPosition = numbers.find(char)
            cipherText += numbers[(currentPosition + n ) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            cipherText += lowerLetters[(currentPosition + n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            cipherText += capitalLetters[(currentPosition + n) % 26] 
        else:
            cipherText += char

    return cipherText
        
def decipher(ciphertext, n):
    global capitalLetters, lowerLetters, numbers
    plaintext = ""

    for char in ciphertext:
        if char in numbers:
            currentPosition = numbers.find(char)
            plaintext += numbers[(currentPosition - n) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            plaintext += lowerLetters[(currentPosition - n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            plaintext += capitalLetters[(currentPosition - n) % 26] 
        else:
            plaintext += char

    return(plaintext)
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)
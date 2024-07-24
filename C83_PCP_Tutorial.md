Encrypt the Password 
===================


In this activity, you will learn to encrypt the password by taking the data from the signup form and storing it. You will also decrypt the stored password and verify it with the password entered while logging in.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10644544/C83PCP.gif" width = "720" height = "440">


Follow the given steps to complete this activity.


* Open the file app.py.


* Import the encrypt, decrypt, and generateKeys functions from encrypt.py file. 


     `from encrypt import encrypt, decrypt, generateKeys`


* Initialize the prime to x for checking the prime number from the start of the range. 


    ` prime = x`
    	    
* Generate public and private keys using the generateKeys() function.


    ` publicKey, privateKey = generateKeys()`   


* Encrypt the “password” with the encrypt() function and store it back in the “password” variable.


    ` password = encrypt(password, publicKey)`


* Create the plainPassword by decrypting the encrypted password with the decrypt() function using the password stored within the “blockData” and the private key.	


    ` plainPassword = decrypt(blockData['password'], privateKey) `


* Use the plainpassword to match the password entered while logging in instead of the encrypted password within the blockData.


    ` if blockData['username'] == username and plainPassword == password: `
    `

* Save and run the code to check the output.




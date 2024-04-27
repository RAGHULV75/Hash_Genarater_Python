# Hash_Genarater_Python
Python Based Hash Generator for Secure Communication

Explanation:

Initialization:

Sets a to 1 to enter the main loop.
Welcome Message:

Prints a welcome message explaining the program's functionality.
Menu:

Prints a menu offering three options:
Press 1: Get hash value of a user input.
Press 2: Validate a value with a previously stored hash.
Press 3: Exit the program.
User Input:

Prompts the user to select an operation (1, 2, or 3).
Hashing Operation (if op == 1):

Prompts the user to enter a value.
Calculates the hash value of the input using the hash() function and converts it to a string.
Prints the calculated hash value.
Opens the file "hash.txt" in append mode ("a").
Writes the calculated hash value followed by a comma (",") to the file.
Closes the file.
Exit Operation (if op == 3):

Exits the program.
Validation Operation (if op == 2):

Prompts the user to enter a value for validation.
Calculates the hash value of the input using hash() and converts it to a string.
Opens the file "hash.txt" in read mode ("r").
Reads the entire content of the file into a variable content.
Checks if the calculated hash value (hsv) exists within the file content.
If found, prints "string exist".
If not found, prints "string does not exist".
Improvements:

Error Handling: The code can be improved by adding error handling for file operations (e.g., handling cases where "hash.txt" doesn't exist).
Security: Storing raw hash values in a plain text file is not secure. Consider using a more secure method for storing and comparing hash values.
Functionality: The program currently only stores hash values, not the original data. You could enhance it to store both the hash and the original data (if appropriate) for more functionalities.


![image](https://github.com/RAGHULV75/Hash_Genarater_Python/assets/168255383/8b40c02f-14bb-432f-9eb5-b2745b6c25ac)

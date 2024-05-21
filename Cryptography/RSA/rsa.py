from math import sqrt

# Function to check if the numbers are prime.
def isprime(n):
        if (n > 1):
                for i in range (2, int(sqrt(n)) + 1):
                        if (n % i == 0):
                                return False
                return True
        return False

def check_primes():
        if(isprime(P) and isprime(Q)):
                print("Numbers accepted \n")
        else:
                print("One of the input is not a prime number")

# Input for two prime numbers to generate keys.

P = int(input("Enter the first prime number (P): "))
Q = int(input("Enter the second prime number (Q): "))

check_primes()

# Calculate Product (N) and Totient (Phi / T):
N = P * Q
print("Product of P and Q is N:", N)

T = (P-1) * (Q-1)
print("Euler's Totient T or Phi:", T)
print("\n")

# Input a public key:
print("Conditions to be satisfied when selecting a public key: \n 1. Chosen public key must be a prime number. \n 2. Public key must be less than Totient. \n 3. Public key must not be a factor of Totient. \n")
E = int(input("Enter a public key: "))
if (isprime(E) and E < T and (T%E)!=0 ):
        print("Public Key accepted \n")

else:
        print("Public key is not accepted")

# Input a private key:
print("Conditions to be satisfied when selecting a private key: \n D * E mod T = 1 \n")
D = int(input("Enter a private key: "))
if (D * E % T == 1):
        print("Private key is accepted \n")
else:
        print("Private key is not accepted")

# Input the message
message = input("Enter the message: ")

if not message:
        raise ValueError("Message cannot be empty")

#Encypting the message:
try:
        encrypted_message = ""
        for char in message:
                ascii_value = ord(char)
                ciphertext = (ascii_value ** E) % N
                encrypted_message += chr(ciphertext)
        print(f"Encrypted message using {E} public key: {encrypted_message}")

except ValueError as e:
        print(f"Error: {e}")

#Decrypting the message:
try:
        decrypted_message = ""
        for char in encrypted_message:
                ascii_value = ord(char)
                plaintext = (ascii_value ** D) % N
                decrypted_message += chr(plaintext)
        print(f"Decrypted message using {D} private key: {decrypted_message}")

except ValueError as e:
        print(f"Error: {e}")


# openssl commands and methods

openssl verion # check version
openssl list -cipher-commands # list all commands

# SYMMETRIC

# (use -pbkdf2 in command to avoid warning message)

openssl enc -aes-256-cbc -base64 -pbkdf2 -in msg.txt # file encryption no output
openssl enc [encryption-method] -base64 -in msg.txt -out [filename] # file encryption output
openssl enc -aes-256-cbc -d -base64 -in [filename] # file decryption
openssl enc -aes-256-cbc -base64 -in [filename] -out enc -k # specify key for encryption

---

# ASSYMETRIC

# Generate a public and private key for each

# 1) A and B pub/priv key generate

openssl genrsa -out keypairA.pem 2048
openssl genrsa -out keypairB.pem 2048

sudo cat filename. pem # view private key

# modulus, pubExponent, privExponent, prime 1-2, exponent1-3, coefficient

openssl rsa -in keypairA.pem -text # view all contents of keypair
openssl rsa -in keypairB.pem -text -noout # view all without private key

# 2) create public key for A & B from key pair

openssl rsa -in keypairA.pem -pubout -out pubkeyA.pem
openssl rsa -in keypairB.pem -pubout -out pubkeyB.pem

# 3) share pubkey (A to B) & (B to A) (link to public key)

In -s /home/kali/A/publicA.pem
In -s /home/kali/B/publicB.pem

# 4) A encrypts with B's pubkey

# using pubkeyB.pem

openssl rsautl -encrypt -in msg -out enc -inkey publicB.pem -pubin # encrypts msg with B's public key (deprecated)
openssl pkeyutl -encrypt -in msga.txt -out enc_pkB -inkey pubkeyB.pem -pubin # encrypts msg with B's public key

# send encrypted file to B/A

cp enc_pkB [rename-file]

# 5) decrypt A's message

openssl pkeyutl -decrypt -in fromA -out filename -inkey keypairB.pem

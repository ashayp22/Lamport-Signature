import hashlib
import math
import secrets
import sys

#source: https://www.geeksforgeeks.org/lamport-one-time-signature-scheme/

#Key Generation - generates a public and private key
def keygen():
    #start out with 2 lists (list comprehension)
    sk = [[0 for _ in range(256)] for _ in range(2)]
    pk = [[0 for _ in range(256)] for _ in range(2)]

    #generate secret (private) and public key
    for i in range(256):
        #a pair of numbers with 256 bits or 32 bytes
        sk[0][i] = secrets.token_bytes(32) #random byte string containing 32 number of bytes - https://docs.python.org/3/library/secrets.html
        sk[1][i] = secrets.token_bytes(32)

        #hash each of the numbers (requires that
        pk[0][i] = hashlib.sha256(sk[0][i]).digest() #requires the input be an array of bytes - http://coders-errand.com/hash-functions-without-mistakes-part-2/
        pk[1][i] = hashlib.sha256(sk[1][i]).digest()

    return sk, pk

#Signature Generaton - gets digital signature of message
def sign(message, sk):
    #start out with our signature
    sig = [0 for _ in range(256)]

    #get the SHA256 hash of our message
    hashed = hashlib.sha256(message.encode("utf-8")).digest() #message needs to be encoded before hashing

    #convert the hash (array of bytes) to its integer representation
    hashed = int.from_bytes(hashed, byteorder=sys.byteorder)

    #For each bit in the 256-bit digest, pick the corresponding number
    #from our private key. This is why this is a one-time signature.
    for i in range(256):
        # Shift our number to the right by i places, which is the same as dividing by 2^i
        # With this, we can determine if the RIGHTMOST bit is a 0 or 1.
        # source: https://wiki.python.org/moin/BitwiseOperators
        l = hashed >> i
        l = l & 1
        sig[i] = sk[l][i]

    return sig

#Signature Verification
def verify(sig, message, pk):
    # get the SHA256 hash of our message
    hashed = hashlib.sha256(message.encode("utf-8")).digest()

    # convert the hash (array of bytes) to its integer representation
    hashed = int.from_bytes(hashed, byteorder=sys.byteorder) #native byte order of the host system - https://docs.python.org/3/library/stdtypes.html

    #For each bit, pick the corresponding number from our public key.
    #Then, if we compare this to a hash of each number in the signature
    #and there is a difference, then we know that the signature is not valid
    for i in range(256):
        l = hashed >> i
        l = l & 1

        other = hashlib.sha256(sig[i]).digest()

        if pk[l][i] != other:
            return False

    return True

#Example 1 - good signature

sk, pk = keygen()
message = "Rob can have 5 of my bitcoin."
sig = sign(message, sk)

if verify(sig, message, pk):
    print("You good son")
else:
    print("You got caught")

#Example 2 - bad signature

good_sk, good_pk = keygen()
message = "John will give you the deed to my house"
good_sig = sign(message, good_sk)

bad_sk, bad_pk = keygen()
bad_sig = sign(message, good_sk)

if verify(bad_sig, message, good_sk):
    print("You good son")
else:
    print("You got caught")

# Lamport-Signature in Python

The Lamport One Time Signature is a method for constructing a digital signature. It normally involves the use of a cryptographic hash function, like SHA-256. It can only be used to securely sign one message. 

## Running

Key Generation
```
good_sk, good_pk = keygen()
```

Signature Generation

```
sig = sign(message, sk)
```

Signature Verification

```
if verify(sig, message, pk):
    print("You good son")
else:
    print("You got caught")
```

## Sources

- https://www.geeksforgeeks.org/lamport-one-time-signature-scheme/
- https://docs.python.org/3/library/secrets.html
- http://coders-errand.com/hash-functions-without-mistakes-part-2/
- https://docs.python.org/3/library/stdtypes.html

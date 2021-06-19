# Lamport-Signature
Lamport One Time Signature Scheme in Python

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

import hashlib

secret = "ckczppom"
nonce = 1

while True:
    h = hashlib.md5(f"{secret}{nonce}".encode()).hexdigest()
    num_zeroes = 5
    starting_zeroes = '0' * num_zeroes
    starting=h[0:num_zeroes]
    if starting == starting_zeroes:
        print(nonce)
        break
    nonce += 1


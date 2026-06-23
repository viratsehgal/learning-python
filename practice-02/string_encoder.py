def encode(msg):
    forward = str.maketrans("aeiouAEIOU", "eiouaEIOUA")
    return msg.translate(forward)
def decode(msg):
    reverse = str.maketrans("eiouaEIOUA", "aeiouAEIOU")
    return msg.translate(reverse)

message = input("Enter a message: ")

encoded = encode(message)
print(f"Encoded: {encoded}")

decoded = decode(encoded)
print(f"Decoded: {decoded}")

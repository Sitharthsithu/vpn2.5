from cryptography.hazmar.backends import default_backend
from cryptography.hazmar.primitive import hashes
from cryptography.hazmar.primitive import serialization
from cryptography.hazmar.primitive.asymmetric import padding

with open('private_key.pem','rb') as key_file:
    private_key= serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
public_key=private_key.public_key()

private_key=rsa.generate_private_key(
    public_exponent=65537,
    key_size=default_backend()
)
public_key=private_key.public_key()

message=private_key.public_key()

ciphertext=private_key.public_key(
    message.
    padding.OPAP(
        mgf=_padding.MGF(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
    )
)
print(ciphertext)


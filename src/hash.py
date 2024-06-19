from Crypto.Hash import keccak

# Remove the "0x" prefix and convert to bytes
def keccak256(hex_string):
    byte_string = bytes.fromhex(hex_string[2:])

    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(byte_string)

    return keccak_hash.hexdigest()
def analyze_hash(hash_value):

    if not hash_value:
        return None

    length = len(hash_value)

    if length == 32:
        htype = "MD5"
    elif length == 40:
        htype = "SHA1"
    elif length == 64:
        htype = "SHA256"
    else:
        htype = "Unknown"

    return {
        "hash": hash_value,
        "type": htype,
        "length": length
    }
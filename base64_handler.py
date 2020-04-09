from base64 import b64encode, b64decode


def data_to_base64(data_string):
    data_bytes = data_string.encode('utf-8')  # Convert string to bytes-like object
    data_b64_bytes = b64encode(data_bytes)  # Base64 encode the data bytes-like object
    data_b64_string = data_b64_bytes.decode('utf-8')  # Convert the base64 bytes-like object to string
    return data_b64_string


def base64_to_data(base64_string):
    base64_bytes = base64_string.encode('utf-8')
    data_bytes = b64decode(base64_bytes)
    data_string = data_bytes.decode('utf-8')
    return data_string

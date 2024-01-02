import jwt
from datetime import datetime, timedelta

# for using jwt: pip install PyJWT


def generate_jwt(payload, secret):
    expiration_time = datetime.utcnow() + timedelta(minutes=15)
    payload.update({'exp': expiration_time})
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token


def verify_jwt(token, secret):
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

    return payload


secret = 'your_secret_key'
generated_token = generate_jwt({'name': 'mahdi'}, secret)
decoded_payload = verify_jwt(generated_token, secret)

print("Generated Token:", generated_token)
print("Decoded Payload:", decoded_payload)

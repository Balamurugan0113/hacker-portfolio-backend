import jwt
import datetime

SECRET = "SUPER_SECRET_KEY"

def generate_token(username):

    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=5)
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    return token


def verify_token(token):

    try:

        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])

        return decoded

    except:

        return None
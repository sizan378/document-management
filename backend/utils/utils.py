from rest_framework.authentication import get_authorization_header
import jwt

def tokenValidation(request):
    token_header = get_authorization_header(request).decode("utf-8")
    token_header_split = token_header.split(" ")
    jwt_key = "JWT_SECRET_KEY"
    if token_header_split[0] == "Bearer":
        token = token_header_split[1]
        payload = jwt.decode(
            jwt=token, key=jwt_key, algorithms=["HS256"]
        )
        return payload
    else:
        return None

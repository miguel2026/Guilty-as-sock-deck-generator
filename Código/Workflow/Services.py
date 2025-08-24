from Model import models
import jwt
import passlib.context
from datetime import datetime, timedelta, timezone
import dotenv


SECRET_KEY = dotenv.get_key(".env","SECRET_KEY")
ALGORITHM = dotenv.get_key(".env","ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(dotenv.get_key(".env","ACCESS_TOKEN_EXPIRE_MINUTES"))
    
crypt = passlib.context.CryptContext(schemes=["bcrypt"], deprecated="auto")

def fake_user(id):

    return models.User(
        id=1,
        username="string",
        email="test@email.com",
        password="$2b$12$OacEbvp1ahX2NROtUFLu6e0DjVnoeLQSuNMVToEv43SwmOO13o6ee",
        decks=[
            models.Deck(
                id=1,
                user_id=1,
                name="Test Deck",
                description="A test deck for unit testing.",
                cards=[
                    models.Card(
                        id=1,
                        deck_id=1,
                        name="Test Card 1",
                        description="This is a test card.",
                        image_url="http://example.com/image1.png"
                    ),
                    models.Card(
                        id=2,
                        deck_id=1,
                        name="Test Card 2",
                        description="This is another test card.",
                        image_url="http://example.com/image2.png"
                    )
                ]
            )])

def id_from_name(name: str) -> int:
    # This function is a placeholder for whatever logic you need to extract an ID from a name.
    # For now, it just returns a fixed ID.
    return 1

def hash_password(password: str) -> str:
    return crypt.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return crypt.verify(plain_password, hashed_password)


def create_access_token(user: dict) -> str:
    payload = {}
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload["sub"] = str(id_from_name(user["username"]))

    encoded_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)

    return models.Token(access_token= encoded_token, token_type="bearer")

def id_from_token(token: str) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
        return payload.get("sub")
    except jwt.PyJWTError:
        return None
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(pwd: str):
    return pwd_cxt.hash(pwd)

from app import models
import pytest  # type: ignore
from app.oauth2 import create_access_token
from tests.database import client, session


@pytest.fixture
def test_user(client):
    user_data = {"email": "anc@example.com", "password": "password123"}
    res = client.post("/users", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture
def test_user2(client):
    user_data = {"email": "sanjeev123@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}

    return client


@pytest.fixture
def test_posts(test_user, test_user2, session):
    posts_data = [
        {"title": "1st title", "content": "1st content", "user_id": test_user["id"]},
        {"title": "2nd title", "content": "2nd content", "user_id": test_user["id"]},
        {"title": "3rd title", "content": "3rd content", "user_id": test_user["id"]},
        {"title": "4th title", "content": "4th content", "user_id": test_user2["id"]},
    ]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    # session.add_all([models.Post(title="first title", content="first content", user_id=test_user['id']),
    #                 models.Post(title="2nd title", content="2nd content", user_id=test_user['id']), models.Post(title="3rd title", content="3rd content", user_id=test_user['id'])])
    session.commit()

    posts = session.query(models.Post).all()
    return posts

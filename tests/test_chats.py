from fastapi.testclient import TestClient
from chat_test_task.main import app

client = TestClient(app)


def test_create_chat():
    response = client.post(
        "/chats/",
        json={"title": "Test chat"}
    )

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["title"] == "Test chat"
    assert "created_at" in data


def test_create_message_in_chat():
    # create chat
    chat_resp = client.post(
        "/chats/",
        json={"title": "Chat for messages"}
    )
    chat_id = chat_resp.json()["id"]

    # add message
    msg_resp = client.post(
        f"/chats/{chat_id}/messages/",
        json={"text": "Hello world"}
    )

    assert msg_resp.status_code in (200, 201)

    msg = msg_resp.json()
    assert msg["text"] == "Hello world"
    assert msg["chat_id"] == chat_id
    assert "created_at" in msg


def test_get_chat_with_messages():
    # create chat
    chat_resp = client.post(
        "/chats/",
        json={"title": "Chat with history"}
    )
    chat_id = chat_resp.json()["id"]

    # add message
    client.post(
        f"/chats/{chat_id}/messages/",
        json={"text": "First message"}
    )

    # get chat
    get_resp = client.get(f"/chats/{chat_id}?limit=10")
    assert get_resp.status_code == 200

    data = get_resp.json()
    assert data["id"] == chat_id
    assert data["title"] == "Chat with history"
    assert "messages" in data
    assert len(data["messages"]) == 1
    assert data["messages"][0]["text"] == "First message"


def test_delete_chat():
    # create chat
    chat_resp = client.post(
        "/chats/",
        json={"title": "Chat to delete"}
    )
    chat_id = chat_resp.json()["id"]

    # delete chat
    del_resp = client.delete(f"/chats/{chat_id}")
    assert del_resp.status_code == 204

    # ensure chat is gone
    get_resp = client.get(f"/chats/{chat_id}")
    assert get_resp.status_code == 404


def test_create_chat_validation_error():
    response = client.post(
        "/chats/",
        json={"title": ""}
    )

    assert response.status_code == 422

def test_create_book(client):
    response = client.post(
        "/api/v1/books/",
        json={"title": "Test Book", "author": "Test Author", "quantity": 1}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"
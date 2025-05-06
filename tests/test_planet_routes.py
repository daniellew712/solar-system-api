

def test_get_all_test(client):
    response = client.get("/planets")

    assert response.status_code == 200
    assert response.get_json() == []




def test_get_one_test_with_fixture(client, one_planet):
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["size"] == one_planet.size


def test_get_one_test_not_found(client):
    response = client.get(f"/planets/1")
    assert response.status_code == 404

def test_create_planet(client):
    Expected_planet = {

        "name" : "Saturn",
        "description" : "beige",
        "size" : 3333
    }
    response = client.post("/planets",json=Expected_planet)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["id"] == 1
    assert response_body["name"] == Expected_planet["name"]
    assert response_body["description"] == Expected_planet["description"]
    assert response_body["size"] == Expected_planet["size"]
import pytest
from fastapi.testclient import TestClient
from app.app import api  # Adjust the import according to your project structure


class CollectionForTestCheck:
    def __init__(self):
        self.collected = []

    def pytest_collection_modifyitems(self, items):
        for item in items:
            self.collected.append(item.nodeid)


client = TestClient(api)

@pytest.fixture(scope="module")
def test_client():
    yield client

def test_create_user(test_client):
    response = test_client.post("/users", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_read_user(test_client):
    response = test_client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_update_user(test_client):
    response = test_client.put("/users/1", json={"name": "John Smith", "email": "johnsmith@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Smith"
    assert response.json()["email"] == "johnsmith@example.com"

def test_delete_user(test_client):
    response = test_client.delete("/users/1")
    assert response.status_code == 204

    # Verify the user is deleted
    response = test_client.get("/users/1")
    assert response.status_code == 404

def test_create_medication(test_client):
    response = test_client.post("/medications", json={"name": "Aspirin", "dosage": "100mg"})
    assert response.status_code == 201
    assert response.json()["name"] == "Aspirin"
    assert response.json()["dosage"] == "100mg"

def test_read_medication(test_client):
    response = test_client.get("/medications/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Aspirin"
    assert response.json()["dosage"] == "100mg"

def test_update_medication(test_client):
    response = test_client.put("/medications/1", json={"name": "Ibuprofen", "dosage": "200mg"})
    assert response.status_code == 200
    assert response.json()["name"] == "Ibuprofen"
    assert response.json()["dosage"] == "200mg"

def test_delete_medication(test_client):
    response = test_client.delete("/medications/1")
    assert response.status_code == 204

    # Verify the medication is deleted
    response = test_client.get("/medications/1")
    assert response.status_code == 404

# Appointments
def test_create_appointment(test_client):
    response = test_client.post("/appointments", json={"title": "Doctor Visit", "date": "2023-10-10"})
    assert response.status_code == 201
    assert response.json()["title"] == "Doctor Visit"
    assert response.json()["date"] == "2023-10-10"

def test_read_appointment(test_client):
    response = test_client.get("/appointments/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Doctor Visit"
    assert response.json()["date"] == "2023-10-10"

def test_update_appointment(test_client):
    response = test_client.put("/appointments/1", json={"title": "Dentist Visit", "date": "2023-11-11"})
    assert response.status_code == 200
    assert response.json()["title"] == "Dentist Visit"
    assert response.json()["date"] == "2023-11-11"

def test_delete_appointment(test_client):
    response = test_client.delete("/appointments/1")
    assert response.status_code == 204

    # Verify the appointment is deleted
    response = test_client.get("/appointments/1")
    assert response.status_code == 404

# Reminders
def test_create_reminder(test_client):
    response = test_client.post("/reminders", json={"message": "Take medication", "time": "08:00"})
    assert response.status_code == 201
    assert response.json()["message"] == "Take medication"
    assert response.json()["time"] == "08:00"

def test_read_reminder(test_client):
    response = test_client.get("/reminders/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Take medication"
    assert response.json()["time"] == "08:00"

def test_update_reminder(test_client):
    response = test_client.put("/reminders/1", json={"message": "Take vitamins", "time": "09:00"})
    assert response.status_code == 200
    assert response.json()["message"] == "Take vitamins"
    assert response.json()["time"] == "09:00"

def test_delete_reminder(test_client):
    response = test_client.delete("/reminders/1")
    assert response.status_code == 204

    # Verify the reminder is deleted
    response = test_client.get("/reminders/1")
    assert response.status_code == 404

# Notifications
def test_create_notification(test_client):
    response = test_client.post("/notifications", json={"content": "New message", "type": "info"})
    assert response.status_code == 201
    assert response.json()["content"] == "New message"
    assert response.json()["type"] == "info"

def test_read_notification(test_client):
    response = test_client.get("/notifications/1")
    assert response.status_code == 200
    assert response.json()["content"] == "New message"
    assert response.json()["type"] == "info"

def test_update_notification(test_client):
    response = test_client.put("/notifications/1", json={"content": "Updated message", "type": "warning"})
    assert response.status_code == 200
    assert response.json()["content"] == "Updated message"
    assert response.json()["type"] == "warning"

def test_delete_notification(test_client):
    response = test_client.delete("/notifications/1")
    assert response.status_code == 204

    # Verify the notification is deleted
    response = test_client.get("/notifications/1")
    assert response.status_code == 404

# Contacts
def test_create_contact(test_client):
    response = test_client.post("/contacts", json={"name": "Jane Doe", "phone": "1234567890"})
    assert response.status_code == 201
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["phone"] == "1234567890"

def test_read_contact(test_client):
    response = test_client.get("/contacts/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["phone"] == "1234567890"

def test_update_contact(test_client):
    response = test_client.put("/contacts/1", json={"name": "Jane Smith", "phone": "0987654321"})
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Smith"
    assert response.json()["phone"] == "0987654321"

def test_delete_contact(test_client):
    response = test_client.delete("/contacts/1")
    assert response.status_code == 204

    # Verify the contact is deleted
    response = test_client.get("/contacts/1")
    assert response.status_code == 404

# Procedures
def test_create_procedure(test_client):
    response = test_client.post("/procedures", json={"name": "Blood Test", "description": "Routine blood test"})
    assert response.status_code == 201
    assert response.json()["name"] == "Blood Test"
    assert response.json()["description"] == "Routine blood test"

def test_read_procedure(test_client):
    response = test_client.get("/procedures/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Blood Test"
    assert response.json()["description"] == "Routine blood test"

def test_update_procedure(test_client):
    response = test_client.put("/procedures/1", json={"name": "X-Ray", "description": "Chest X-Ray"})
    assert response.status_code == 200
    assert response.json()["name"] == "X-Ray"
    assert response.json()["description"] == "Chest X-Ray"

def test_delete_procedure(test_client):
    response = test_client.delete("/procedures/1")
    assert response.status_code == 204

    # Verify the procedure is deleted
    response = test_client.get("/procedures/1")
    assert response.status_code == 404

# Allergies
def test_create_allergy(test_client):
    response = test_client.post("/allergies", json={"name": "Peanuts", "severity": "High"})
    assert response.status_code == 201
    assert response.json()["name"] == "Peanuts"
    assert response.json()["severity"] == "High"

def test_read_allergy(test_client):
    response = test_client.get("/allergies/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Peanuts"
    assert response.json()["severity"] == "High"

def test_update_allergy(test_client):
    response = test_client.put("/allergies/1", json={"name": "Dust", "severity": "Medium"})
    assert response.status_code == 200
    assert response.json()["name"] == "Dust"
    assert response.json()["severity"] == "Medium"

def test_delete_allergy(test_client):
    response = test_client.delete("/allergies/1")
    assert response.status_code == 204

    # Verify the allergy is deleted
    response = test_client.get("/allergies/1")
    assert response.status_code == 404

# Medical Conditions
def test_create_medical_condition(test_client):
    response = test_client.post("/medical_conditions", json={"name": "Diabetes", "description": "Chronic condition"})
    assert response.status_code == 201
    assert response.json()["name"] == "Diabetes"
    assert response.json()["description"] == "Chronic condition"

def test_read_medical_condition(test_client):
    response = test_client.get("/medical_conditions/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Diabetes"
    assert response.json()["description"] == "Chronic condition"

def test_update_medical_condition(test_client):
    response = test_client.put("/medical_conditions/1", json={"name": "Hypertension", "description": "High blood pressure"})
    assert response.status_code == 200
    assert response.json()["name"] == "Hypertension"
    assert response.json()["description"] == "High blood pressure"

def test_delete_medical_condition(test_client):
    response = test_client.delete("/medical_conditions/1")
    assert response.status_code == 204

    # Verify the medical condition is deleted
    response = test_client.get("/medical_conditions/1")
    assert response.status_code == 404


def test_check_all_endpoints_for_test_function():
    endpoints_response=client.get("/openapi.json").json()
    endpoint_paths=endpoints_response['paths']
    api_endpoint_functions=[]
    for endpoint in endpoint_paths:
        for endpoint_method in endpoint_paths[endpoint]:
            endpoint_slug=endpoint[1:].replace("/","_")
            length_of_suffix=len(f"_{endpoint_slug}_{endpoint_method}")
            api_endpoint_functions.append(endpoint_paths[endpoint][endpoint_method]['operationId'][:-length_of_suffix])
    coll = CollectionForTestCheck()
    pytest.main(['--collect-only'], plugins=[coll])
    test_functions=[]
    for test_coll in coll.collected:
        test_functions.append(str(test_coll).split("::")[-1])

    for api_endpoint_function in api_endpoint_functions:
        assert "test_"+str(api_endpoint_function) in test_functions, f"Test function of {api_endpoint_function} couldn't found"

def test_check_all_endpoints_for_success_response_model():
    endpoints=client.get("/openapi.json").json()['paths']
    for endpoint in endpoints:
        for endpoint_method in endpoints[endpoint]:
            assert "$ref" in endpoints[endpoint][endpoint_method]['responses']['200']['content']['application/json'][
                'schema'] \
                   or "title" in \
                   endpoints[endpoint][endpoint_method]['responses']['200']['content']['application/json'][
                       'schema'], f"response_model isn't defined for method: {endpoint_method} endpoint: {endpoint} "

from falcon import testing
import falcon_sample.app as App

def client():
    """Initialize application configuration and create server
    """
    return testing.TestClient(App.api)

def test_user_module():
  result =  client().simulate_get("/users")
  assert result.json["message"] == "User modules is running successfully."


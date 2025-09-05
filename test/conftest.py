import pytest
from app.core.app_factory import create_app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
app = create_app()
return TestClient(app)
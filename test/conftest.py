import pytest
from app.core.app_factory import create_app
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    """
    Provides a TestClient for the FastAPI app.
    Scope set to 'module' for efficiency.
    """
    app = create_app()
    return TestClient(app)

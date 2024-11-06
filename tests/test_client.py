from fastapi.testclient import TestClient
from app.main import app, Cell

client = TestClient(app)

def create_grid(rows, cols, barriers=[]):
    """Helper function to create a grid for testing."""
    return [[{"x": x, "y": y, "isBarrier": (x, y) in barriers, "isStart": False, "isEnd": False}
            for y in range(cols)] for x in range(rows)]

def test_path_exists():
    grid = create_grid(5, 5, barriers=[(2, 2)])
    start = (0, 0)
    end = (4, 4)

    response = client.post("/find-path", json={"grid": grid, "start": start, "end": end})
    assert response.status_code == 200
    assert "path" in response.json()

def test_path_not_found():
    grid = create_grid(5, 5, barriers=[(x, y) for x in range(5) for y in range(1, 5)])  # Block path to end
    start = (0, 0)
    end = (4, 4)

    response = client.post("/find-path", json={"grid": grid, "start": start, "end": end})
    assert response.status_code == 200
    assert response.json() == {"message": "No path found"}

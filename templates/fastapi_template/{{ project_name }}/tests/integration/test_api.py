"""Integration tests for API endpoints."""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.integration
class TestAPIIntegration:
	"""Integration tests for API endpoints."""

	@pytest.mark.asyncio
	async def test_api_endpoints_accessible(self, client: TestClient) -> None:
		"""Test that API endpoints are accessible."""
		# Test OpenAPI endpoints
		response = client.get("/api/openapi.json")
		assert response.status_code == 200

		response = client.get("/docs")
		assert response.status_code == 200

	@pytest.mark.asyncio
	async def test_cors_headers(self, client: TestClient) -> None:
		"""Test CORS headers are properly set."""
		response = client.options("/", headers={"Origin": "http://localhost:3000"})
		assert "access-control-allow-origin" in response.headers

	@pytest.mark.asyncio
	async def test_json_responses(self, client: TestClient) -> None:
		"""Test that responses are valid JSON."""
		response = client.get("/api/openapi.json")
		assert response.headers["content-type"] == "application/json"

		data = response.json()
		assert isinstance(data, dict)

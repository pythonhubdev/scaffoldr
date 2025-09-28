"""Integration tests for API endpoints."""

import pytest
from httpx import AsyncClient


@pytest.mark.integration
class TestAPIIntegration:
	"""Integration tests for API endpoints."""

	@pytest.mark.asyncio
	async def test_api_endpoints_accessible(self, client: AsyncClient) -> None:
		"""Test that API endpoints are accessible."""
		# Test OpenAPI endpoints
		response = await client.get("/openapi.json")
		assert response.status_code == 200

		response = await client.get("/docs")
		assert response.status_code == 200

	@pytest.mark.asyncio
	async def test_cors_headers(self, client: AsyncClient) -> None:
		"""Test CORS headers are properly set."""
		response = await client.options("/", headers={"Origin": "http://localhost:3000"})
		assert "access-control-allow-origin" in response.headers

	@pytest.mark.asyncio
	async def test_json_responses(self, client: AsyncClient) -> None:
		"""Test that responses are valid JSON."""
		response = await client.get("/openapi.json")
		assert response.headers["content-type"] == "application/json"

		data = response.json()
		assert isinstance(data, dict)

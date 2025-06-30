# client/utils/api_client.py
import os
import httpx
from typing import Dict, Any, Optional
from dotenv import load_dotenv
load_dotenv()

class APIClient:
    def __init__(self):
        self.base_url = os.getenv('BACKEND_URL', 'http://localhost:8000')
        self.timeout = 10.0
    
    async def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generic POST request handler"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}{endpoint}",
                json=data,
                timeout=self.timeout
            )
            return {
                'status_code': response.status_code,
                'data': response.json() if response.content else {},
                'success': response.status_code < 400
            }
    
    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generic GET request handler"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}{endpoint}",
                params=params,
                timeout=self.timeout
            )
            return {
                'status_code': response.status_code,
                'data': response.json() if response.content else {},
                'success': response.status_code < 400
            }

# Singleton instance
api_client = APIClient()

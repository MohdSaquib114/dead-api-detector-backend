import httpx
import time

async def check_api(url: str):
    start = time.time()
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5)

        response_time = time.time() - start

        return {
            "status_code": response.status_code,
            "response_time": response_time,
            "is_success": response.status_code < 400
        }

    except Exception:
        return {
            "status_code": 0,
            "response_time": 0,
            "is_success": False
        }
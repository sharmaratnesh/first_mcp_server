from aiohttp import web
import json

class MathHandler:
    async def handle(self, request: web.Request) -> web.Response:
        try:
            data = await request.json()
            if data.get("method") == "add":
                try:
                    # Get numbers from the request body
                    body = data.get("body", {})
                    num1 = float(body.get("num1", 0))
                    num2 = float(body.get("num2", 0))
                    
                    # Calculate the sum
                    result = num1 + num2
                    
                    # Return success response
                    return web.json_response({
                        "status": 200,
                        "body": {"result": result}
                    })
                except (ValueError, TypeError) as e:
                    return web.json_response({
                        "status": 400,
                        "body": {"error": "Invalid numbers provided"}
                    }, status=400)
            else:
                return web.json_response({
                    "status": 400,
                    "body": {"error": "Method not supported"}
                }, status=400)
        except json.JSONDecodeError:
            return web.json_response({
                "status": 400,
                "body": {"error": "Invalid JSON"}
            }, status=400)
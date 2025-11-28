import asyncio
from aiohttp import web
from handlers.math_handler import MathHandler
from handlers.employee_handler import EmployeeHandler

async def handle_request(request: web.Request) -> web.Response:
    try:
        data = await request.json()
        handler_name = data.get("handler")
        
        if handler_name == "math":
            return await math_handler.handle(request)
        elif handler_name == "employee":
            return await employee_handler.handle(request)
        else:
            return web.json_response({
                "status": 400,
                "body": {"error": f"Handler '{handler_name}' not found"}
            }, status=400)
    except Exception as e:
        return web.json_response({
            "status": 500,
            "body": {"error": str(e)}
        }, status=500)

async def init_app():
    app = web.Application()
    app.router.add_post('/', handle_request)
    return app

if __name__ == '__main__':
    math_handler = MathHandler()
    employee_handler = EmployeeHandler()
    app = asyncio.run(init_app())
    web.run_app(app, host='localhost', port=8080)
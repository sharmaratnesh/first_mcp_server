from aiohttp import web
import csv
from pathlib import Path


class EmployeeHandler:
    async def handle(self, request: web.Request) -> web.Response:
        try:
            data = await request.json()
            if data.get("method") == "get_name":
                body = data.get("body", {})
                empid = body.get("empid")
                if empid is None:
                    return web.json_response({
                        "status": 400,
                        "body": {"error": "Missing 'empid' in request body"}
                    }, status=400)

                empid_str = str(empid).strip()

                # employee_details.csv is located at the repository root.
                csv_path = Path(__file__).resolve().parents[3] / 'employee_details.csv'
                if not csv_path.exists():
                    return web.json_response({
                        "status": 500,
                        "body": {"error": f"Employee file not found: {csv_path}"
                                 }
                    }, status=500)

                with csv_path.open(newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # Normalize keys/values (CSV has spaces in header)
                        normalized = {k.strip(): (v.strip() if v is not None else '') for k, v in row.items()}
                        if normalized.get('empid') == empid_str:
                            return web.json_response({
                                "status": 200,
                                "body": {"name": normalized.get('name')}
                            })

                return web.json_response({
                    "status": 404,
                    "body": {"error": "Employee not found"}
                }, status=404)
            else:
                return web.json_response({
                    "status": 400,
                    "body": {"error": "Method not supported"}
                }, status=400)
        except Exception as e:
            return web.json_response({
                "status": 500,
                "body": {"error": str(e)}
            }, status=500)

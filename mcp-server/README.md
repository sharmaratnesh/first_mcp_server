# MCP Server

This project is a basic MCP server implemented in Python. It provides an HTTP endpoint to return the sum of two numbers.

## Project Structure

- `src/server.py`: Entry point of the application.
- `src/handlers/math_handler.py`: Contains the logic for summing two numbers.
- `src/utils/__init__.py`: Utility functions and constants.
- `tests/test_server.py`: Unit tests for the server functionality.
- `requirements.txt`: Lists the dependencies required for the project.
- `README.md`: Documentation for the project.

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd mcp-server
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

To run the server, execute the following command:
```
python src/server.py
```

The server will start and listen for requests.

## Testing (Ignore this)

To run the tests, use the following command:
```
pytest tests/test_server.py
```

## To run the add function using the MCP server. call it using either curl or using a simple python command

curl -X POST http://localhost:8080/ -H "Content-Type: application/json" -d '{ "handler":"math", "method":"add", "body": { "num1": 2, "num2": 3 } }'


or otherwise use python script like this

```
python - <<'PY'
import requests
payload = {"handler":"math","method":"add","body":{"num1":2,"num2":3}}
r = requests.post("http://localhost:8080/", json=payload)
print(r.status_code, r.json())
PY
```

```
import requests
payload = {"handler":"employee","method":"get_name","body":{"empid":1}}
r = requests.post("http://localhost:8080/", json=payload)
print(r.status_code, r.json())
```

>>> import requests
>>> payload = {"handler":"employee","method":"get_name","body":{"empid":1}}
>>> r = requests.post("http://localhost:8080/", json=payload)
>>> print(r.status_code, r.json())
200 {'status': 200, 'body': {'name': 'john'}}
>>>
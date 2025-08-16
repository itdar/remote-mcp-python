import requests
import json

# FastMCP 서버가 실행 중이어야 함 (localhost:8080)
base_url = "http://localhost:8000"
# base_url = "https://ecda4d2de6fe.ngrok-free.app"

def test_endpoint(method, params=None):
  payload = {
    "jsonrpc": "2.0",
    "method": method,
    "params": params or {},
    "id": 1
  }

  # FastMCP 필수 헤더
  headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream"
  }

  try:
    response = requests.post(base_url, json=payload, headers=headers)
    print(f"\n=== {method} ===")
    print(f"Status: {response.status_code}")
    if response.headers.get('content-type', '').startswith('application/json'):
      print(f"Response: {json.dumps(response.json(), indent=2)}")
    else:
      print(f"Response: {response.text}")
    return True
  except Exception as e:
    print(f"\n=== {method} FAILED ===")
    print(f"Error: {e}")
    return False

# 필수 엔드포인트들 테스트
print("Testing MCP required endpoints...")

# 1. Initialize (가장 중요)
test_endpoint("initialize", {
  "protocolVersion": "2024-11-05",
  "capabilities": {},
  "clientInfo": {"name": "test-client", "version": "1.0.0"}
})

# 2. Ping
test_endpoint("ping")

# 3. Tools list
test_endpoint("tools/list")

# 4. Resources list
test_endpoint("resources/list")

# 5. Prompts list
test_endpoint("prompts/list")

# 6. Health check (일반적인 HTTP GET)
try:
  health = requests.get(f"{base_url}/health")
  print(f"\n=== Health Check ===")
  print(f"Status: {health.status_code}")
  if health.status_code == 200:
    print(f"Response: {health.text}")
except:
  print("Health endpoint not available")

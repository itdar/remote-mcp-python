# PPYY - FastMCP HTTP Server

FastAPI를 사용한 HTTP 인터페이스 MCP (Model Context Protocol) 서버입니다.

## 프로젝트 구조

```
src/com.gino.mcp/
├── main.py                 # 메인 진입점 (FastMCP)
├── tools/                  # FastMCP 인스턴스 및 도구 등록
│   └── sample.py           
├── api/
│   └── routes.py           # FastAPI 라우터 (수동 MCP 프로토콜 처리)
├── handlers/
│   └── default.py          # MCP 프로토콜 기본
```

## 아키텍처

### 기본 방식: FastMCP
- `main.py:1`에서 `tools/sample.py`의 FastMCP 인스턴스 import
- `mcp.run(transport="streamable-http")`로 HTTP 서버 시작
- `@mcp.tool()` 데코레이터로 도구 등록

### 보조 방식: 수동 FastAPI 구현
- `api/routes.py`에서 MCP 프로토콜 직접 구현
- JSON-RPC 2.0 형식으로 `initialize`, `ping`, `notification` 메서드 처리

## 새 도구 추가 방법

### 1. 간단한 도구 추가
`src/com.gino.mcp/tools/sample.py`에 함수 또는 스크립트 추가:

```python
@mcp.tool()
async def your_new_tool(param: str) -> str:
    """도구 설명"""
    return f"결과: {param}"
```

### 2. 복잡한 도구 추가 (별도 모듈)
1. `src/com.gino.mcp/tools/` 디렉터리에 새 모듈 생성
2. 도구 함수 구현
3. `tools/sample.py`에서 import 후 등록:

```python
from tools.your_module import your_function

@mcp.tool()
async def your_tool(param: str) -> str:
    """도구 설명"""
    return await your_function(param)
```

## 새 리소스 추가 방법

`src/com/gino.mcp/tools/sample.py` 참고해서 함수나 스크립트 등 추가:

```python
@mcp.resource("uri://your-namespace/{resource_id}")
async def your_resource(resource_id: str) -> str:
    """리소스 설명"""
    return f"리소스 내용: {resource_id}"
```

## 서버 실행

```bash
python src/com.gino.mcp/main.py
python3 src/com.gino.mcp/main.py
```

## 현재 등록된 도구

- `hello`: 간단한 인사 도구 (`tools/sample.py`)

## 의존성

- fastmcp
- httpx
- mcp[cli]

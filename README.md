# PPYY - Python MCP Server

FastMCP, FastAPI 사용한 python MCP (Model Context Protocol) 서버
> streamable-http

## 프로젝트 구조

- FastMCP: Tool, Resource 등을 데코레이터로 처리
- FastAPI: initialize, ping 등 기본 연결 호출 응답을 처리

```
src/com.gino.mcp/
│
├── api/
│   └── routes.py           # FastAPI 라우터 (수동 MCP 프로토콜 처리)
│
├── dto/
│   └── api_response.py     # api response dto 샘플
│
├── handlers/               # FastAPI 핸들러
│   └── default.py          ## MCP 프로토콜 기본
│
├── tools/                  # FastMCP 인스턴스 및 도구 등록
│   └── sample.py           ## 단순 툴, 외부 호출 툴 등 샘플
│
├── main.py                 # 메인 진입점 (FastMCP)
```

## 아키텍처

### 기본 방식: FastMCP
- `main.py` 에서 FastMCP 인스턴스 생성
- `mcp.run(transport="streamable-http")`로 HTTP 서버 시작
- `register_sample_tools()` 에서 `@mcp.tool()` 데코레이터로 도구 등록

### 보조 방식: 수동 FastAPI 구현
- `api/routes.py`에서 MCP 프로토콜 직접 구현
- JSON-RPC 2.0 형식으로 `initialize`, `ping`, `notification` 등 메서드 처리

## 새 도구 추가 방법

### 1. 간단한 도구 추가
`src/com.gino.mcp/tools/register_sample_tools.py`에 함수 추가:

```python
@mcp.tool()
async def your_new_tool(param: str) -> str:
    """도구 설명"""
    return f"결과: {param}"
```

### 2. 복잡한 도구 추가 (별도 모듈)
1. `src/com.gino.mcp/tools/` 디렉터리에 새 모듈 생성
2. 도구 함수 구현
3. `main.py` 에서 `register_another_tools()` 호출로 등록 (예시)

```python
from tools.your_module import your_function

@mcp.tool()
async def your_tool(param: str) -> str:
    """도구 설명"""
    return await your_function(param)
```

## 새 리소스 추가 방법 (추후에 상세내용 추가 예정)

`src/com/gino.mcp/tools/register_sample_tools.py` 참고해서 
아래 리소스 형식에 맞게 함수나 스크립트 등 추가:

1. `src/com.gino.mcp/resources/` 디렉터리 생성 및 새 모듈 생성
2. 위 리소스 함수 구현
3. `main.py` 에서 `register_default_resources()` 호출로 등록 (예시)

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

- `hello`: 간단한 인사 도구 (`tools/register_sample_tools.py`)

## 의존성

- fastmcp
- httpx
- mcp[cli]
... 등

명령어로 한 번에 설치하려면
```bash
   uv pip install -r requirements.txt
   uv pip3 install -r requirements.txt
```


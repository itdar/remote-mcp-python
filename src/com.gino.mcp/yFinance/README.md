# Financial Information Integration [Python MCP Server]

This is a Model Context Protocol (MCP) server that provides comprehensive financial data. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

## MCP Tools

The server exposes the following tools through the Model Context Protocol:

### Stock Information

| Tool | Description |
|------|-------------|
| `get_historical_stock_prices` | Get historical OHLCV data for a stock with customizable period and interval |
| `get_stock_info` | Get comprehensive stock data including price, metrics, and company details |
| `get_finance_news` | Get latest news articles for a stock |
| `get_stock_actions` | Get stock dividends and splits history |

### Financial Statements

| Tool | Description |
|------|-------------|
| `get_financial_statement` | Get income statement, balance sheet, or cash flow statement (annual/quarterly) |
| `get_holder_info` | Get major holders, institutional holders, mutual funds, or insider transactions |

### Options Data

| Tool | Description |
|------|-------------|
| `get_option_expiration_dates` | Get available options expiration dates |
| `get_option_chain` | Get options chain for a specific expiration date and type (calls/puts) |

### Analyst Information

| Tool | Description |
|------|-------------|
| `get_recommendations` | Get analyst recommendations or upgrades/downgrades history |

## Real-World Use Cases

With this MCP server, you can use Claude to:

### Stock Analysis

- **Price Analysis**: "Show me the historical stock prices for AAPL over the last 6 months with daily intervals."
- **Financial Health**: "Get the quarterly balance sheet for Microsoft."
- **Performance Metrics**: "What are the key financial metrics for Tesla from the stock info?"
- **Trend Analysis**: "Compare the quarterly income statements of Amazon and Google."
- **Cash Flow Analysis**: "Show me the annual cash flow statement for NVIDIA."

### Market Research

- **News Analysis**: "Get the latest news articles about Meta Platforms."
- **Institutional Activity**: "Show me the institutional holders of Apple stock."
- **Insider Trading**: "What are the recent insider transactions for Tesla?"
- **Options Analysis**: "Get the options chain for SPY with expiration date 2024-06-21 for calls."
- **Analyst Coverage**: "What are the analyst recommendations for Amazon over the last 3 months?"

### Investment Research

- "Create a comprehensive analysis of Microsoft's financial health using their latest quarterly financial statements."
- "Compare the dividend history and stock splits of Coca-Cola and PepsiCo."
- "Analyze the institutional ownership changes in Tesla over the past year."
- "Generate a report on the options market activity for Apple stock with expiration in 30 days."
- "Summarize the latest analyst upgrades and downgrades in the tech sector over the last 6 months."

## Requirements

- Python 3.11 or higher
- Dependencies as listed in `pyproject.toml`, including:
  - mcp
  - yfinance
  - pandas
  - pydantic
  - and other packages for data processing

## Setup


Create and activate a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

## Usage

### Development Mode

You can test the server with MCP Inspector by running:

```bash
uv run server.py
```

This will start the server and allow you to test the available tools.

### Integration with Claude for Desktop

To integrate this server with Claude for Desktop:

1. Install Claude for Desktop to your local machine.
2. Install VS Code to your local machine. Then run the following command to open the `claude_desktop_config.json` file:
   - MacOS: `code ~/Library/Application\ Support/Claude/claude_desktop_config.json`
   - Windows: `code $env:AppData\Claude\claude_desktop_config.json`

3. Edit the Claude for Desktop config file, located at:
   - macOS: 
     ```json
     {
       "mcpServers": {
         "yfinance": {
           "command": "uv",
           "args": [
             "--directory",
             "/ABSOLUTE/PATH/TO/PARENT/FOLDER/yahoo-finance-mcp",
             "run",
             "server.py"
           ]
         }
       }
     }
     ```
   - Windows:
     ```json
     {
       "mcpServers": {
         "yfinance": {
           "command": "uv",
           "args": [
             "--directory",
             "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\yahoo-finance-mcp",
             "run",
             "server.py"
           ]
         }
       }
     }
     ```

   - **Note**: You may need to put the full path to the uv executable in the command field. You can get this by running `which uv` on MacOS/Linux or `where uv` on Windows.

4. Restart Claude for Desktop

## License

MIT

---

### Google Cloud Run script
```shell
#!/bin/bash

# --- 1. gcloud CLI 설치 (이미 설치했다면 건너뛰어도 됩니다) ---
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# --- 2. gcloud 초기 설정 및 인증 (이미 설정했다면 건너뛰어도 됩니다) ---
gcloud init

# --- 3. GCP API 활성화 및 Docker 인증 ---
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
gcloud auth configure-docker asia-northeast3-docker.pkg.dev

# --- 4. Artifact Registry 저장소 생성 (이미 생성했다면 건너뛰어도 됩니다) ---
gcloud artifacts repositories create mcp-servers \
    --repository-format=docker \
    --location=asia-northeast3 \
    --description="MCP Server Images"

# --- 5. Docker 이미지 빌드 (amd64 플랫폼 지정) 및 GCP로 푸시 ---
export GIN_PROJECT_ID=$(gcloud config get-value project)
docker build --platform linux/amd64 -t asia-northeast3-docker.pkg.dev/$GIN_PROJECT_ID/mcp-servers/gino-mcp:latest .
docker push asia-northeast3-docker.pkg.dev/$GIN_PROJECT_ID/mcp-servers/gino-mcp:latest

# --- 6. Google Cloud Run 배포 ---
gcloud run deploy gino-mcp-service \
    --image=asia-northeast3-docker.pkg.dev/$GIN_PROJECT_ID/mcp-servers/gino-mcp:latest \
    --port=8080 \
    --region=asia-northeast3 \
    --allow-unauthenticated \
    --platform=managed
```
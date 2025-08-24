import sys, os
from fastmcp import FastMCP
from tools.tool import register_sample_tools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    mcp = FastMCP("Financial Information Integration",
        instructions="""
        This server is used to get information about a given ticker symbol.
        
        Available tools:
        - get_historical_stock_prices: Get historical stock prices for a given ticker symbol. Include the following information: Date, Open, High, Low, Close, Volume, Adj Close.
        - get_stock_info: Get stock information for a given ticker symbol. Include the following information: Stock Price & Trading Info, Company Information, Financial Metrics, Earnings & Revenue, Margins & Returns, Dividends, Balance Sheet, Ownership, Analyst Coverage, Risk Metrics, Other.
        - get_finance_news: Get news for a given ticker symbol.
        - get_stock_actions: Get stock dividends and stock splits for a given ticker symbol.
        - get_financial_statement: Get financial statement for a given ticker symbol. You can choose from the following financial statement types: income_stmt, quarterly_income_stmt, balance_sheet, quarterly_balance_sheet, cashflow, quarterly_cashflow.
        - get_holder_info: Get holder information for a given ticker symbol. You can choose from the following holder types: major_holders, institutional_holders, mutualfund_holders, insider_transactions, insider_purchases, insider_roster_holders.
        - get_option_expiration_dates: Fetch the available options expiration dates for a given ticker symbol.
        - get_option_chain: Fetch the option chain for a given ticker symbol, expiration date, and option type.
        - get_recommendations: Get recommendations or upgrades/downgrades for a given ticker symbol. You can also specify the number of months back to get upgrades/downgrades for, default is 12.
        """
    )

    register_sample_tools(mcp)

    mcp.run(host="0.0.0.0",
            port=8080,
            transport="streamable-http"
    )


if __name__ == "__main__":
    main()

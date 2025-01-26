from phi.agent import Agent
from phi.model.groq import Groq 
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()



finance_agent= Agent(
    name="Finance Agent",
    role="Get Financial Data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True,company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True
     
)

finance_agent.print_response("Get me the stock price of Apple Inc")


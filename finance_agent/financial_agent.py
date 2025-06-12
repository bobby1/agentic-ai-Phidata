from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from os import getenv
from dotenv import load_dotenv

load_dotenv()


## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,
)

## Financial agent - agentic ai
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    name='A Stock Market Agent',
    role='A comprehensive assistant specializing in stock market analysis by combining financial insights with real-time web searches to deliver accurate, up-to-date information',
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Nvidia.",stream=True)
# multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for qbts.",stream=True)
# multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for IBM.",stream=True)
# multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for qbts.",stream=True)

### Added by BSW to customize the agent for user input

# if __name__ == "__main__":
#     symbol = input("Enter a stock symbol (e.g., IBM): ").strip()
#     if symbol:
#         prompt = f"Summarize analyst recommendation and share the latest news for {symbol}."
#         multi_ai_agent.print_response(prompt, stream=True)
#     else:
#         print("No symbol entered.")

if __name__ == "__main__":
    while True:
        symbol = input("Enter a stock symbol (e.g., IBM) or press Enter to exit: ").strip().upper()
        if not symbol:
            print("No symbol entered. Exiting.")
            break
        prompt = f"Summarize analyst recommendation and share the latest news for {symbol}."
        multi_ai_agent.print_response(prompt, stream=True)
        # response = multi_ai_agent.print_response(prompt, stream=True)
        # response = multi_ai_agent.run(prompt, stream=True)
        # print(response)

# if __name__ == "__main__":
#     while True:
#         symbol = input("Enter a stock symbol (e.g., IBM) or press Enter to exit: ").strip()
#         if not symbol:
#             print("No symbol entered. Exiting.")
#             break
#         prompt = f"Summarize analyst recommendation and share the latest news for {symbol}."
#         response = multi_ai_agent.run(prompt)
#         # print(response)
#         print("\n" + "="*60)
#         print(f"📈 Analysis for {symbol.upper()}")
#         print("="*60)
#         print(response.strip())
#         print("="*60 + "\n")
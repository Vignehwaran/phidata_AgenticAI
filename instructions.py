from phi.agent import Agent 
from phi.tools.hackernews import HackerNews
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from phi.model.google import Gemini


hn_research = Agent(
    name="hackerNews researcher",
    role="gets top news from hacketnews",
    tools=[HackerNews()],
    description="get news upto date",
    instraction="get info of the hackerNews",
    markdown= True,
    debug_mode=True,
    task="fech the information about pongal festival on 2025 ",
    expected_output="The pongal festival in 2025 and key terms and starting",
    prvent_hallucinations=True,
    sytem_message_role="the system about the festival 2025",
    system_prompt_template="pongal festival session information ",
)

hn_gemini = Agent(
    name="Ai sereach agent",
    role="get ai imforation about the for pongal session",
    model=Gemini(id="gemini-1.5-flash"),
    description="get the information about pongal festival 2025",
    instraction=["get the information about pongal festival 2025"],
    markdown=True,
    api_key="AIzaSyAkdQMUDJQu_um1g0dz96LpR_5jYmwOH04",
    provider="Gemini"


)

hn_newspaper4K = Agent(
    name="newspaper4k agent",
    role="get news from newspaper4k about pongal festival 2025",
    tools=[Newspaper4k],
    description="fech deatils about the pongal festival",
    instraction=["get the information about pongal festival 2025"],
    markdown=True,
)

hn_search = Agent(
    name="duckduckgo search agent",
    role="search for specific task for recent news",
    tools=[DuckDuckGo],
    description="get the information about pongal festival 2025",
    instraction=["fetch deatils about the yeats of tamil festival of 2025"],
    search=True,
    News=True,
    headers="Recent news",
    markdown=True,
    
    )

hn_team = Agent(
    name="team agent",
    team=[hn_research ,hn_gemini,hn_newspaper4K,hn_search],
    instruction=["tamil news covers the tamil famous deatils recent news",
    "important news: today to indian","indian today festiva to add news info to user"
    "Then, ask the web searcher to search for each story to get more information.",
    "Finally, provide a thoughtful and engaging summary."],
)

show_tool_calls=True,
hn_team.print_resspnse("the top news of the pongal festival 2025")


    



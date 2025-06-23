# Browser Automation Tool using browser-use

def browser_demo(task="Open Google and search for AI"):
    try:
        import asyncio
        from browser_use import Agent
        from langchain_openai import ChatOpenAI
    except ImportError:
        print("[Browser Tool] browser-use or langchain_openai not installed.")
        return
    async def run_agent():
        agent = Agent(
            task=task,
            llm=ChatOpenAI(model="gpt-4o"),
        )
        await agent.run()
    print(f"[Browser Tool] Running browser automation for task: {task}")
    asyncio.run(run_agent())

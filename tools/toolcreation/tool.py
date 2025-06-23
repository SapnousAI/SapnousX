def scaffold_tool(name):
    import os
    tool_dir = f'tools/{name}'
    os.makedirs(tool_dir, exist_ok=True)
    with open(f'{tool_dir}/tool.py', 'w') as f:
        f.write(f'def {name}_demo():\n    return "{name} tool ready!"\n')
    return f'Tool scaffolded at {tool_dir}'

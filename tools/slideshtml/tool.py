def create_html_slide(title, content, filename='slide.html'):
    html = f"""
    <html><head><title>{title}</title></head><body>
    <h1>{title}</h1>
    <div>{content}</div>
    </body></html>
    """
    with open(filename, 'w') as f:
        f.write(html)
    return f'Slide saved to {filename}'

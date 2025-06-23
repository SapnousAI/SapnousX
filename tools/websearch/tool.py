try:
    from webscout import WEBS
    webscout_available = True
except ImportError:
    webscout_available = False

def web_search(query, max_results=5):
    if not webscout_available:
        return 'Webscout not installed.'
    with WEBS() as webs:
        results = webs.text(query, max_results=max_results)
        return [
            {'title': r.get('title'), 'url': r.get('url'), 'body': r.get('body', '')}
            for r in results
        ]

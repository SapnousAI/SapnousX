try:
    import qdrant_client
    memory_available = True
except ImportError:
    memory_available = False

def store_vector(collection, vector, payload=None):
    if not memory_available:
        return 'qdrant-client not installed.'
    client = qdrant_client.QdrantClient()
    client.upsert(collection_name=collection, points=[{'vector': vector, 'payload': payload or {}}])
    return 'Vector stored.'

def search_vector(collection, query_vector, top=3):
    if not memory_available:
        return 'qdrant-client not installed.'
    client = qdrant_client.QdrantClient()
    hits = client.search(collection_name=collection, query_vector=query_vector, limit=top)
    return hits

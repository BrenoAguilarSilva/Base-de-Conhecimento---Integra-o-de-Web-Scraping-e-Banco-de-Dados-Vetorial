from pymilvus import Collection, connections
from sentence_transformers import SentenceTransformer
from .handlingText import cleanText, normalizeCharacters
from model import finopsPages


finopsPages.conectionMilvusDB()
collection = finopsPages.create_or_get_collection()

# Modelo de Aprendizado de máquina utilizado no embeddings da base de dados.
model = SentenceTransformer('all-MiniLM-L6-v2')

def generateQueryEmbedding(query):
    handlingQuery = cleanText(query)
    normalizedQuery = normalizeCharacters(handlingQuery)
    print(f'Pergunta Normalizada: {normalizedQuery}\n')
    return model.encode(normalizedQuery)

def searchSimilarDocuments(queryEmbedding, top_k=5):
    # Realiza a busca vetorial
    search_params = {
        "metric_type": "IP",
        "params": {"nprobe": 10},
    }
    results = collection.search(
        data=[queryEmbedding],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["title", "link", "documentType", "originalData", "collectionDate", "embedding"],
        consistency_level="Strong"
    )
    
    documents = [
        {
            "title": hit.entity.get("title"),
            "link": hit.entity.get("link"),
            "documentType": hit.entity.get("documentType"),
            "originalData": hit.entity.get("originalData"),
            "collectionDate": hit.entity.get("collectionDate"),
            "score": hit.score,
        }
        for hits in results for hit in hits
    ]
    return documents

query = "What is the FinOps maturity model?"

queryEmbedding = generateQueryEmbedding(query)
documents = searchSimilarDocuments(queryEmbedding)
for document in documents:
    print(f"Title: {document['title']}")
    print(f"Link: {document['link']}")
    print(f"Document Type: {document['documentType']}")
    print(f"Original Data: {document['originalData']}")
    print(f"Collection Date: {document['collectionDate']}")
    print(f"Score: {document['score']}")
    print("-" * 40)

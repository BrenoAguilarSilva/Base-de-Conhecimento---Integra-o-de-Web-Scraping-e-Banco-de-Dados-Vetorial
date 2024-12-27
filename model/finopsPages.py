from pymilvus import connections, Collection, CollectionSchema, DataType, FieldSchema, utility 
from datetime import datetime

class milvusConnectionError(Exception):
    def __init__(self, message="Erro ao conectar ao Milvus"):
        super().__init__(message)

def conectionMilvusDB(host="127.0.0.1", port="19530"):
    try:
        connections.connect("default", host=host, port=port)
        print("Conexão bem-sucedida com o Milvus!")
    except Exception as e:
        raise milvusConnectionError(f"Erro ao conectar ao Milvus no host {host} e porta {port}: {e}")
    
def create_or_get_collection(collectionName="finopsContent"):
    conectionMilvusDB()
    if utility.has_collection(collectionName):
        collection = Collection(collectionName)
        print(f"A coleção '{collectionName}' já existe.")
    else:
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
            FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=500),
            FieldSchema(name="link", dtype=DataType.VARCHAR, max_length=500),
            FieldSchema(name="collectionDate", dtype=DataType.VARCHAR, max_length=500),
            FieldSchema(name="originalData", dtype=DataType.VARCHAR, max_length=65000),
            FieldSchema(name="documentType", dtype=DataType.VARCHAR, max_length=500),
            # O valor de "dim" Depende do modelo escolhido para ser utilizado, modelo atual é all-MiniLM-L6-v2
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
        ]
        
        schema = CollectionSchema(fields, description="finops Content")
        collection = Collection(collectionName, schema)
        print(f"Coleção '{collectionName}' criada.")
    
    if not collection.has_index():
        index_params = {
            "index_type": "HNSW",        # Tipo de índice (pode ser IVF_FLAT, IVF_SQ8, etc.)
            "metric_type": "IP",         # Tipo de métrica (IP para produto interno, Cosine Similarity)
            "params": {"M": 16, "efConstruction": 200}  # Parâmetros específicos para HNSW
        }
        collection.create_index(field_name="embedding", index_params=index_params)
        print(f"Índice criado na coleção '{collectionName}'.")

    collection.load()

    return collection
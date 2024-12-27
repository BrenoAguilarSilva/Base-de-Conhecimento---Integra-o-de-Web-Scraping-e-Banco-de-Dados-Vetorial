from datetime import datetime

def createDataCollection(collection, title, link, text, documentType, embedding, uniqueID):
    try:
        if collection is None:
            raise ValueError("A coleção fornecida é inválida.")
        
        if not text or not isinstance(text, str):
            raise ValueError("O texto fornecido é inválido ou vazio.")

        if len(embedding) != 384:
            print(f"Embedding inválido para {title}")
            raise ValueError("Embedding inválido")

        collectionDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = [
            {
                "id": uniqueID,
                "title": title,
                "link": link,
                "collectionDate": collectionDate,
                "originalData": text,
                "documentType": documentType,
                "embedding": embedding
            }
        ]
        try:
            collection.insert(data)
            collection.flush()
            collection.load()
            print(f"Dados criados na coleção para o conteudo: {title}")
        except Exception as e:
            raise RuntimeError(f"Erro ao inserir dados na coleção: {str(e)}")

    except ValueError as e:
        print(f"Erro de valor: {str(e)}")
    except RuntimeError as e:
        print(f"Erro ao processar os dados: {str(e)}")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")


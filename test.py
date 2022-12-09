from haystack.document_stores import FAISSDocumentStore
document_store = FAISSDocumentStore.load("bms1")


for doc in document_store:
    if(doc.content==''):
        print(doc.content)




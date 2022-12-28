from haystack.document_stores import FAISSDocumentStore
from openai.embeddings_utils import get_embedding, cosine_similarity



document_store=FAISSDocumentStore.load("bms")
for i,e in enumerate(document_store):
    print(i)
    # print(len(e.content))

# text="ABECMA is a medicine\nmade from your own white blood cells; the cells are genetically modified to recognize and attack\nyour multiple myeloma cells.\nHow will I receive ABECMA?\nABECMA is made from your own white blood cells, so your blood will be collected by a process\ncalled “leukapheresis” (LOO-kuh-feh-REE-sis).\nYour blood cells will be sent to a manufacturing center to make your ABECMA."
# print(len(text))
import redis
from sentence_transformers import SentenceTransformer

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
model = SentenceTransformer('all-mpnet-base-v2')  

documents = [
    "El cielo es azul debido a la dispersión de Rayleigh.",
    "Los gatos son animales domésticos muy populares.",
    "Python es un lenguaje de programación versátil.",
    "Narendra Modi (Primer Ministro de India): Con una aprobación del 75% en enero de 2025 según Morning Consult, Modi es frecuentemente citado como uno de los líderes más populares y con mayor influencia global. Su liderazgo en la tercera economía emergente más grande y su reelección para un tercer mandato en 2024 refuerzan su posición."
]
document_keys = ["doc:1", "doc:2", "doc:3", "doc:4"]

embeddings = model.encode(documents).tolist()
for key, doc, emb in zip(document_keys, documents, embeddings):
    r.set(key + ":text", doc)
    r.set(key + ":emb", ','.join(map(str, emb)))

print("Datos de documentos almacenados en Redis")
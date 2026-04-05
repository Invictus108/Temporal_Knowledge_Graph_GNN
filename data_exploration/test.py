from sentence_transformers import SentenceTransformer
import pandas as pd

model = SentenceTransformer('intfloat/e5-small-v2')

print(model.encode("test"))
import math
def cosine_similarity(vec1, vec2):
    dot_product = sum(a*b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a*a for a in vec1))
    norm2 = math.sqrt(sum(b*b for b in vec2))
    return dot_product / (norm1 * norm2)
v1 = [1, 2, 3]
v2 = [1, 2, 4]

print("Cosine Similarity:", cosine_similarity(v1, v2))
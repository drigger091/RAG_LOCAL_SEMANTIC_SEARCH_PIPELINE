"""
Similarity measures :dot products and cosine simlarity

in general closer vectors will have higher scores and away vectos will have lower scores

vectors have directoons and magnitues

We dont decide theese values our model does
| Similarity measure | Description | Code |
| ----- | ----- | ----- |
| [Dot Product](https://en.wikipedia.org/wiki/Dot_product) | -
 Measure of magnitude and direction between two vectors<br>- Vectors that are aligned in direction and magnitude 
 have a higher positive value<br>- Vectors that are opposite in direction and magnitude have a higher negative value | 
 [`torch.dot`](https://pytorch.org/docs/stable/generated/torch.dot.html), [`np.dot`]
 (https://numpy.org/doc/stable/reference/generated/numpy.dot.html), [`sentence_transformers.util.dot_score`]
(https://www.sbert.net/docs/package_reference/util.html#sentence_transformers.util.dot_score)


[Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) | - 
Vectors get normalized by magnitude/[Euclidean norm](https://en.wikipedia.org/wiki/Norm_(mathematics))/L2 norm 
so they have unit length and are compared more so on direction<br>- Vectors that are aligned in direction have a value c
lose to 1<br>- Vectors that are opposite in direction have a value close to -1 | [`torch.nn.functional.cosine_similarity`](
https://pytorch.org/docs/stable/generated/torch.nn.functional.cosine_similarity.html), [`1 - scipy.spatial.distance.cosine`]
(https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html) (subtract the distance from 1 for 
similarity measure), [`sentence_transformers.util.cos_sim`]
(https://www.sbert.net/docs/package_reference/util.html#sentence_transformers.util.cos_sim) |






"""

import torch

def dot_product(vector1 , vector2):
    return torch.dot(vector1,vector2)

def cosine_similarity(vector1 , vector2):
    dot_product_value = dot_product(vector1,vector2)

    # get euclidean /l2 norm
    norm_vector1 = torch.sqrt(torch.sum(vector1**2))
    norm_vector2 = torch.sqrt(torch.sum(vector2**2))


    return dot_product_value/(norm_vector1 * norm_vector2)



# exmaple vectors

vector1 = torch.tensor([1,2,3],dtype = torch.float32)
vector2 = torch.tensor([1,2,3],dtype = torch.float32)
vector3 = torch.tensor([4,5,6],dtype = torch.float32)
vector4 = torch.tensor([-1,-2,-3],dtype = torch.float32) # same value as vector 1 going in geatve direction


# calcuate the dot product
print("dot product between vector1 and vector2 : ",dot_product(vector1,vector2))
print("dot product between vector1 and vector2 : ",dot_product(vector1,vector3))
print("dot product between vector1 and vector2 : ",dot_product(vector1,vector4))


# for text we have got to normalize for the magnitude , even vector 1 and vector 3 are same but differnt magntitude ,so 
#value coming higher for them but for text vectors vec1 vs vec2 should be highest as they resemble exactness whuch is better 
#for semantic search

print("Cosine similatity between vector1 and vector2:",cosine_similarity(vector1,vector2))
print("Cosine similatity between vector1 and vector3:",cosine_similarity(vector1,vector3))
print("Cosine similatity between vector1 and vector3:",cosine_similarity(vector1,vector4))
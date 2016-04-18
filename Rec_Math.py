import math

#calculate mean of a vector    
def cal_mean(vector):
    total = 0
    count = 0
    for k in vector.keys():
        total += vector[k]
        count += 1
    if(count == 0):
        return 0
    avg = total/count
    return avg

#calculate euclideanNorm of a vector      
def euclideanNorm(vector):
    total = 0
    for k in vector.keys():
        total += math.pow(vector[k],2)
    result = math.sqrt(total)
    return result

#calculate dot product of two vectors
def dot_product(vector1,vector2):
    v1 = []
    v2 = []
    for k in vector1.keys():
        v1.append(vector1[k])
    for k in vector2.keys():
        v2.append(vector2[k])
    sum = 0
    if(len(v1) != len(v2)):
        if(len(v1) < len(v2)):
            for i in range(0,len(v1)):
                sum += v1[i]*v2[i]
            return sum
        else:
            for i in range(0,len(v2)):
                sum += v1[i]*v2[i]
            return sum
    else:
        for i in range(0,len(v1)):
            sum += v1[i]*v2[i]
        return sum
    
#normalize a vector by subtracting mean from every value(mean centering)
def normalize(vector):
    normalized = dict()
    mean = cal_mean(vector)
    for k in vector.keys():
        normalized_value = vector[k] - mean
        normalized[k] = normalized_value
    return normalized
    
#return cosine similarity between two vectors
def similarity_between(vector1,vector2):
    normalized1 = normalize(vector1)
    normalized2 = normalize(vector2)
    numer = dot_product(normalized1,normalized2)
    a = euclideanNorm(normalized1)
    b = euclideanNorm(normalized2)
    denom = a * b
    if(denom == 0):
        denom = .001
    result = numer/denom
    return result


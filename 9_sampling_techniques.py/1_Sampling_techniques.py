import random

Students = list(range(1,31))
print("Population :",Students)

print("="*70)


# ===============================================
# Non Probability Sampliing
# ===============================================


# ----------------------------------------

# Cluster Sampling
cluster1 = Students[0:10]
cluster2 = Students[10:20]
cluster3 = Students[20:30]

clusters = [cluster1,cluster2,cluster3]
selected_cluster = random.choice(clusters)

print("Cluster Sampling :",selected_cluster)
print("="*70)

# ----------------------------------------

# Coveriance Sampling  ---->convenience Sampling
convenience_sample = Students[-5:] #start from -1 --->follow int number line
print("Covariance Sample :",convenience_sample)

print("="*70)
# ----------------------------------------

first_person = random.choice(Students)
snowball_sample = [first_person,first_person+1,first_person+2]
print("Snowball Samples :",snowball_sample)

print("="*70)
# ----------------------------------------


# ===============================================
# Probability Sampliing
# ===============================================
 
# simple random Sampling
data = [35,40,45,50,55,60,65,70,75,80,85,64,64,34,75,23,76,38,46,46,46,29]
random_sample = random.sample(data,6)
print("Random Sample :",random_sample)

print("="*70)
# ----------------------------------------

# symmetric Sampling
symmetric_sampling = data[::6]
print("Symmetric Sampling: ",symmetric_sampling)

print("="*70)
# ----------------------------------------


# ===============================================
# Advance Probability Sampliing
# ===============================================

# statified_sample
low_marks = [x for x in data if x < 60]
high_marks = [x for x in data if x >= 60]

sample_low = random.sample(low_marks,2)
sample_high = random.sample(high_marks,3)

Stratified_sample = sample_low + sample_high

print("Stratified Sample",Stratified_sample)

print("="*70)
# ----------------------------------------
#  add cluster sampling in it 
# added earlier

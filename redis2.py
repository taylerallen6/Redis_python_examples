import redis
import time
from pprint import pprint

r = redis.Redis(
  host='localhost',
  port=6379
)


# ### REDIS KEY VALUES
# r.set('key_test1', 'value_test1')
# value = r.get('key_test1')
# print(value)

### create keys
# num_keys = 1000000
# keys = range(num_keys)
# values = range(num_keys)
# pairs = dict(zip(keys, values))

# # ### set key values
# # for i, key in enumerate(keys):
# #   r.set(key, f"value_{i}")
# r.mset(pairs)

 
# ### get all key values
# start = time.time()

# values = r.mget(keys)
# # print(values)
# print(len(values))

# end = time.time()
# print("The time of execution of above program is :", (end-start) * 10**3, "ms")


### get all key values
start = time.time()

keys = r.keys("[0-9]")
print(keys)
print(len(keys))

end = time.time()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")



### create keys (connections) and values (weights)
### key format = "({connection_id}):({memory1_id})->({memory2_id})"
### value format = {int}
# key_value_pairs = {
#   "(001):(001)->(002)": 10,
#   "(002):(001)->(003)": 124,
#   "(003):(001)->(004)": 41,
#   "(004):(002)->(001)": 235,
#   "(005):(002)->(003)": 8,
#   "(006):(003)->(001)": 238,
#   "(007):(003)->(002)": 58,
#   "(008):(003)->(004)": 492
# }
# r.mset(key_value_pairs)

# keys = r.keys(f"(*):(001)->(*)")
# print(keys)
# values = r.mget(keys)
# print(values)

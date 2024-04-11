import redis

r = redis.Redis(
  host='localhost',
  port=6379
)


### REDIS KEY VALUES
# r.set('key_test1', 'value_test1')
# value = r.get('key_test1')
# print(value)


### REDIS QUEUE
# r.lpush("myList2", "value4")
# new_values = ["value5", "value6"]
# r.lpush("myList2", *new_values)
# value = r.rpop("myList2", 1)
# print(value)
# value = r.rpop("myList2", 2)
# print(value)
# values = r.lrange("myList2", 0, -1)
# values = r.lrange("myList2", -1, -1)
# print(values)

### REDIS HASH
# r.hset("key1", "field1", "value1")
# fields = {"field1": "value1", "field2": "value2"}
# r.hset("key2", mapping=fields)

value = r.hget("key2", "field2")
print(value)
# field_value = r.hgetall("key2")
# print(field_value[b'field1'])


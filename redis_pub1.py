import redis

r = redis.Redis(
  host='localhost',
  port=6379
)


### REDIS PUBSUB
### publish a message to the `redis` channel
r.publish("redis", "hello world")

### subscriber
# sub = r.pubsub()
# sub.subscribe("redis")
# while True:
#   msg = sub.get_message()
#   print(f"new message: {msg['data']}")
#code to read and write the data in redis containers from outside world afetr exposing it nodeport
import redis
r = redis.StrictRedis(host='192.168.39.59', port=30764, db=0, password='aadi0105')
r.set('xyz', '{aadi:172.184.155.164}')
r.set('abc', 'mishra')
r.set('me', 'I am developer')
msg = r.get('xyz')
msg1= r.get('abc')
msg2= r.get('me')
print(msg2)
print(msg)
print(msg1)


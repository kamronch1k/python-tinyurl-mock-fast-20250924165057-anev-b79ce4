import hashlib
s='fastcloud'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])

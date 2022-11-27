import base64

Str = "hurrah!! wer won!!!";

Str = base64.b64decode(str.encode('utf-8',errors= 'strict'))
print ("Encoded String: " , Str)
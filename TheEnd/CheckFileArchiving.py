from minio import Minio
import sys
import json

#read content from Nifi
a = sys.stdin.readline()
HT=json.loads(a)
client = Minio(
		"192.168.56.105:9000",
		access_key = "admin",
		secret_key = "password@31",
		secure = False,
	)
try:
    
    response = client.get_object(HT["s3.bucket"], HT["s3.key"])
    sEtag=response.__dict__['headers']['ETag']
    if(sEtag[1:(len(sEtag)-1)]==response.__dict__['headers']['x-amz-meta-s3.hashvalue']):
        sys.stdout.write(" successfully "+ HT["s3.bucket"])
    else:
        sys.stdout.write(" Error Archiving "+ HT["s3.bucket"])
    # Read data from response.
finally:
    response.close()
    response.release_conn()
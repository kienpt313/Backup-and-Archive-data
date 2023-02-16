from minio import Minio

client = Minio(
		"192.168.56.105:9000",
		access_key = "admin",
		secret_key = "password@31",
		secure = False,
	)
found = client.bucket_exists("bucket08")
if not found:
    client.make_bucket("bucket08")
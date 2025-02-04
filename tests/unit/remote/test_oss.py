from dvc.remote.oss import OSSRemote

bucket_name = "bucket-name"
endpoint = "endpoint"
key_id = "Fq2UVErCz4I6tq"
key_secret = "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsu"


def test_init(dvc):
    prefix = "some/prefix"
    url = f"oss://{bucket_name}/{prefix}"
    config = {
        "url": url,
        "oss_key_id": key_id,
        "oss_key_secret": key_secret,
        "oss_endpoint": endpoint,
    }
    remote = OSSRemote(dvc, config)
    assert remote.tree.path_info == url
    assert remote.tree.endpoint == endpoint
    assert remote.tree.key_id == key_id
    assert remote.tree.key_secret == key_secret

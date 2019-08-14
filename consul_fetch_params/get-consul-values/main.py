from consul_kv import Connection
import json
conn = Connection(endpoint='http://192.168.1.51:8500/v1/')

def lambda_handler(event, context):
    data = conn.get('feature', recurse=True)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": data
        }),
    }

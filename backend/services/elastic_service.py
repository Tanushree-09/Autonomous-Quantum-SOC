from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import BulkIndexError

es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "network_logs"


def create_index():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME)
        print(f"Index '{INDEX_NAME}' created.")
    else:
        print(f"Index '{INDEX_NAME}' already exists.")


def store_logs(logs):
    actions = [
        {
            "_index": INDEX_NAME,
            "_source": log
        }
        for log in logs
    ]

    try:
        success, failed = helpers.bulk(
            es,
            actions,
            raise_on_error=False,
            stats_only=True
        )

        print(f"Indexed: {success}")
        print(f"Failed : {failed}")

    except BulkIndexError as e:
        print("Bulk Index Error")
        from pprint import pprint
        pprint(errors[0])
def search_logs(query, size=100):

    response = es.search(
        index=INDEX_NAME,
        query=query,
        size=size
    )

    return response


def get_logs_by_label(label, size=100):

    query = {
        "term": {
            "Label.keyword": label
        }
    }

    return search_logs(query, size)


def get_recent_logs(size=100):

    response = es.search(
        index=INDEX_NAME,
        size=size
    )

    return response

def get_attack_statistics(label):

    response = es.search(
        index=INDEX_NAME,
        size=0,
        body={
            "query": {
                "term": {
                    "Label.keyword": label
                }
            },
            "aggs": {
                "top_ports": {
                    "terms": {
                        "field": "Destination Port",
                        "size": 10
                    }
                },
                "avg_flow_duration": {
                    "avg": {
                        "field": "Flow Duration"
                    }
                },
                "avg_packets_per_sec": {
                    "avg": {
                        "field": "Flow Packets/s"
                    }
                },
                "avg_bytes_per_sec": {
                    "avg": {
                        "field": "Flow Bytes/s"
                    }
                }
            }
        }
    )

    return response
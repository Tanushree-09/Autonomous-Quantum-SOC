from elasticsearch import Elasticsearch


es = Elasticsearch(
    "http://localhost:9200"
)

INDEX_NAME = "network_logs"


response = es.search(
    index=INDEX_NAME,
    size=0,
    aggs={
        "attack_types": {
            "terms": {
                "field": "Label.keyword",
                "size": 100
            }
        }
    }
)


buckets = response["aggregations"]["attack_types"]["buckets"]


print("\n========== LABEL DISTRIBUTION ==========\n")


for bucket in buckets:

    print(
        f"{bucket['key']:<30} "
        f"{bucket['doc_count']}"
    )
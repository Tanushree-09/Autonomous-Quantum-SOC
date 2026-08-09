from backend.services.elastic_service import get_attack_statistics


class DetectionAgent:

    def detect_attack(self, attack_name):

        response = get_attack_statistics(attack_name)

        hits = response["hits"]["total"]["value"]

        aggregations = response["aggregations"]

        ports = [
            bucket["key"]
            for bucket in aggregations["top_ports"]["buckets"]
        ]

        report = {
            "attack": attack_name,
            "total_events": hits,
            "top_ports": ports,
            "average_flow_duration":
                aggregations["avg_flow_duration"]["value"],
            "average_packets_per_second":
                aggregations["avg_packets_per_sec"]["value"],
            "average_bytes_per_second":
                aggregations["avg_bytes_per_sec"]["value"]
        }

        return report
from neo4j import GraphDatabase


class ThreatGraphAgent:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            "bolt://localhost:7687",
            auth=("neo4j", "password")
        )

        self.driver.verify_connectivity()
        print("Connected to Neo4j")


    def close(self):
        self.driver.close()


    def create_graph(self, report):

        print("Creating graph...")

        with self.driver.session() as session:
            session.execute_write(
                self._create_graph,
                report
            )

        print("Graph created successfully.")


    @staticmethod
    def _create_graph(tx, report):

        attack = report["attack"]
        total_events = report["total_events"]
        avg_flow = report["average_flow_duration"]
        avg_packets = report["average_packets_per_second"]
        avg_bytes = report["average_bytes_per_second"]
        ports = report["top_ports"]

        tx.run(
            """
            MERGE (a:Attack {name: $attack})
            SET
                a.total_events = $events,
                a.avg_flow_duration = $flow,
                a.avg_packets_per_second = $packets,
                a.avg_bytes_per_second = $bytes
            """,
            attack=attack,
            events=total_events,
            flow=avg_flow,
            packets=avg_packets,
            bytes=avg_bytes
        )

        for port in ports:

            tx.run(
                """
                MERGE (p:Port {number: $port})

                WITH p

                MATCH (a:Attack {name: $attack})

                MERGE (a)-[:TARGETS]->(p)
                """,
                attack=attack,
                port=port
            )
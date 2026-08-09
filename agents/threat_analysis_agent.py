class ThreatAnalysisAgent:

    def analyze(self, report):

        risk_score = 0

        severity = "LOW"

        confidence = 0.0

        attack = report["attack"]

        total_events = report["total_events"]

        packets = report["average_packets_per_second"]

        bytes_sec = report["average_bytes_per_second"]


        if total_events > 100000:
            risk_score += 40

        elif total_events > 10000:
            risk_score += 25

        else:
            risk_score += 10


        if packets > 50000:
            risk_score += 30

        elif packets > 10000:
            risk_score += 20

        else:
            risk_score += 10


        if bytes_sec > 200000:
            risk_score += 30

        elif bytes_sec > 100000:
            risk_score += 20

        else:
            risk_score += 10


        risk_score = min(risk_score,100)


        if risk_score >= 80:
            severity = "CRITICAL"

        elif risk_score >= 60:
            severity = "HIGH"

        elif risk_score >= 40:
            severity = "MEDIUM"

        else:
            severity = "LOW"


        confidence = round(risk_score/100,2)


        analysis = {

            "attack": attack,

            "severity": severity,

            "risk_score": risk_score,

            "confidence": confidence
        }

        return analysis
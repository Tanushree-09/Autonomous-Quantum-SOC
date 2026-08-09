from ollama import chat


class LLMAgent:

    def __init__(self):

        self.model = "llama3.2:3b"


    def analyze_threat(self, threat_data):

        prompt = f"""
You are the security reasoning agent inside an
Autonomous Quantum Security Operations Center
(AQ-SOC).

Analyze the following structured security evidence:

{threat_data}

Provide:

1. Threat interpretation
2. Likely security impact
3. Investigation priority
4. Important ports, services, or behaviors
5. Security evidence that should be passed to
   the quantum-risk analysis stage
6. Potential relevance to post-quantum security
   and "harvest now, decrypt later" risk

IMPORTANT:

Do NOT decide whether quantum analysis should
be skipped.

The AQ-SOC always evaluates potentially relevant
threats through its quantum-risk analysis stage.

Do not claim that a threat requires quantum
computing merely because it is being analyzed by
this system.

Do not invent information that is not present
in the supplied evidence.

Keep the analysis concise and technical.
"""

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        return response["message"]["content"]
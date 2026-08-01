"""
Phase II: Policy Analysis & Discussion Module
Generates a deep-dive policy analysis across the 6 required perspectives.
"""

from sdg_agent.config import SDG_DATA

def generate_phase2_analysis(chosen_sdg: str) -> dict:
    """
    Generates a rigorous policy analysis brief across the 6 required evaluation dimensions for Phase II.
    """
    if chosen_sdg not in SDG_DATA:
        raise ValueError("Invalid SDG choice. Choose '5', '9', or '13'.")
        
    data = SDG_DATA[chosen_sdg]
    
    analysis = {
        "title": data["title"],
        "tagline": data["tagline"],
        "dimensions": {
            "1. Current Challenges & Global Relevance": f"Globally, {data['title']} faces immense pressure. {data['tagline']} The urgency is defined by: {data['urgency']}. Societal impact: {data['societal_impact']}.",
            "2. Root Causes of Existing Issues": data["root_causes"],
            "3. Policy and Governance Gaps": data["governance_gaps"],
            "4. Stakeholders Involved": data["stakeholders"],
            "5. Barriers to Implementation": data["barriers"],
            "6. Opportunities for Innovation and Improvement": data["opportunities"]
        }
    }
    return analysis

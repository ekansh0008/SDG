"""
Phase I: SDG Prioritisation & Negotiation Module
Helps participants build winning, persuasive arguments for Phase I of the SDG GD competition.
"""

from sdg_agent.config import SDG_DATA

def generate_phase1_strategy(chosen_sdg: str) -> dict:
    """
    Generates strategic negotiation points, urgency arguments, feasibility metrics,
    and consensus-building guidelines for Phase I.
    """
    if chosen_sdg not in SDG_DATA:
        raise ValueError("Invalid SDG choice. Choose '5', '9', or '13'.")
        
    target = SDG_DATA[chosen_sdg]
    others = [k for k in SDG_DATA.keys() if k != chosen_sdg]
    
    # Build comparison points
    comparison_points = []
    for o in others:
        other_sdg = SDG_DATA[o]
        comparison_points.append({
            "vs": other_sdg["title"],
            "argument": f"While {other_sdg['title']} is vital, {target['title']} acts as a foundational prerequisite. Without focusing on {target['title']} first, progress in {other_sdg['title']} remains restricted due to systemic bottlenecks."
        })

    strategy = {
        "sdg": target["title"],
        "tagline": target["tagline"],
        "opening_hook": f"To achieve sustainable development across all goals, we must prioritize {target['title']} because {target['societal_impact']}",
        "urgency_argument": target["urgency"],
        "feasibility_argument": target["feasibility"],
        "policy_relevance": target["policy_relevance"],
        "comparisons": comparison_points,
        "consensus_builder": f"We acknowledge that all three SDGs (5, 9, and 13) are interconnected. However, selecting {target['title']} as our focal point creates a maximum multiplier effect that accelerates achievements in the other two domains."
    }
    return strategy

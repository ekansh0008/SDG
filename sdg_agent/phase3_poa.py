"""
Phase III: Lobbying & Plan of Action (PoA) Module
Generates a complete, structured 9-section Plan of Action for Phase III.
"""

from sdg_agent.config import SDG_DATA

def generate_phase3_poa(chosen_sdg: str, team_name: str = "Team InnovateSDG") -> dict:
    """
    Generates a professional 9-section Plan of Action (PoA) for Phase III lobbying and proposal presentation.
    """
    if chosen_sdg not in SDG_DATA:
        raise ValueError("Invalid SDG choice. Choose '5', '9', or '13'.")
        
    data = SDG_DATA[chosen_sdg]
    
    # Customizing PoA based on SDG
    if chosen_sdg == "5":
        obj = "Accelerate gender parity in economic leadership, STEM education, and grassroots entrepreneurship through targeted policy intervention and digital inclusion."
        beneficiaries = "Women and girls in rural and semi-urban communities, female entrepreneurs, and women in informal workforce sectors."
        strategy = "Establish public-private partnerships to launch digital skill training hubs, enforce gender-responsive budgeting in local governance, and provide collateral-free micro-loans for women-led enterprises."
        resources = "Government grants, CSR funds from corporate partners, mobile learning labs, and community mentorship networks."
        timeline = "Phase 1 (Months 1-3): Needs assessment & stakeholder mapping. Phase 2 (Months 4-12): Pilot training & credit distribution. Phase 3 (Months 13-24): Scaling nationwide and impact audit."
        outcomes = "40% increase in female participation in STEM/digital sectors, 10,000 women-led micro-enterprises scaled, and robust local gender audit committees established."
        challenges = "Cultural resistance to women's economic independence and digital literacy gaps."
        mitigation = "Community engagement workshops involving local elders and male champions of gender equality; simplified offline-first mobile training interfaces."
        monitoring = "Quarterly sex-disaggregated data tracking, independent social impact assessments, and public transparency dashboards."
    elif chosen_sdg == "9":
        obj = "Deploy climate-resilient, sustainable industrial infrastructure and foster green innovation hubs in developing industrial clusters."
        beneficiaries = "Local communities near industrial zones, MSMEs adopting green tech, and municipal workers."
        strategy = "Develop decentralized renewable energy microgrids for industrial parks, establish incubation centers for clean-tech startups, and implement circular economy waste-to-energy mandates."
        resources = "Green bonds, multilateral climate innovation funds, university engineering partnerships, and private equity investments."
        timeline = "Phase 1 (Months 1-4): Infrastructure audit & green zoning. Phase 2 (Months 5-18): Pilot green corridor & startup incubator rollout. Phase 3 (Months 19-36): Full-scale industrial modernization."
        outcomes = "30% reduction in industrial carbon emissions, 50 green tech startups incubated, and 100% reliable clean energy supply for participating industrial parks."
        challenges = "High upfront capital expenditure and reluctance of traditional legacy industries to transition."
        mitigation = "Government tax incentives, subsidized green loans, and phased regulatory compliance timelines."
        monitoring = "IoT-enabled real-time emission monitoring sensors, third-party environmental audits, and annual sustainability reporting."
    else: # 13
        obj = "Enhance community climate resilience and accelerate decarbonization through localized nature-based solutions and renewable energy transition."
        beneficiaries = "Climate-vulnerable coastal and agrarian communities, local municipalities, and vulnerable low-income households."
        strategy = "Implement large-scale community afforestation and regenerative agriculture programs, transition public transport and municipal buildings to 100% solar power, and establish early-warning disaster response systems."
        resources = "International climate adaptation funds, carbon credit revenue, local government budgets, and NGO volunteer networks."
        timeline = "Phase 1 (Months 1-3): Vulnerability mapping & community sensitization. Phase 2 (Months 4-18): Afforestation drives & solar grid installation. Phase 3 (Months 19-36): Comprehensive climate resilience integration."
        outcomes = "50,000 hectares of restored carbon sinks, 40% local carbon footprint reduction, and zero-casualty community disaster preparedness protocols."
        challenges = "Unpredictable extreme weather events disrupting implementation schedules and short-term political resistance to fossil fuel phase-out."
        mitigation = "Adaptive project management frameworks, robust insurance mechanisms, and just-transition support packages for fossil-fuel dependent workers."
        monitoring = "Satellite geospatial tracking of afforestation, community-led climate committees, and transparent carbon offset verification."
    
    poa = {
        "team_name": team_name,
        "selected_sdg": data["title"],
        "tagline": data["tagline"],
        "sections": {
            "1. Objective and Intended Impact": obj,
            "2. Target Beneficiaries or Stakeholders": beneficiaries,
            "3. Implementation Strategy": strategy,
            "4. Roles and Responsibilities": "Government (Regulatory & Funding), Private Sector (Execution & Tech), NGOs (Community Mobilization), Academic Institutions (Research & Monitoring).",
            "5. Resources Required": resources,
            "6. Timeline of Execution": timeline,
            "7. Expected Outcomes": outcomes,
            "8. Possible Challenges and Mitigation Measures": f"Challenges: {challenges} | Mitigation: {mitigation}",
            "9. Monitoring and Evaluation Mechanisms": monitoring
        }
    }
    return poa

"""
Configuration and Knowledge Base for SDG Group Discussion AI Agent.
Covers SDG 5 (Gender Equality), SDG 9 (Industry, Innovation & Infrastructure), and SDG 13 (Climate Action).
"""

SDG_DATA = {
    "5": {
        "title": "SDG 5 – Gender Equality",
        "tagline": "Achieve gender equality and empower all women and girls.",
        "urgency": "High (Fundamental human right and multiplier effect across all 17 SDGs)",
        "feasibility": "High ROI on social investment, requires legal reforms, education, and cultural shift.",
        "societal_impact": "Unlocks 50% of human capital, reduces poverty, improves child health, boosts GDP up to 26% globally.",
        "policy_relevance": "Key international treaties (CEDAW), national gender budgeting, equal pay legislation.",
        "root_causes": [
            "Patriarchal social norms and systemic cultural biases.",
            "Unequal access to property rights, land ownership, and financial credit.",
            "Disproportionate burden of unpaid care and domestic work.",
            "Gender-based violence (GBV) and inadequate legal enforcement."
        ],
        "governance_gaps": [
            "Lack of sex-disaggregated data in local governance and workforce planning.",
            "Weak enforcement of anti-discrimination and equal remuneration laws.",
            "Under-representation of women in STEM leadership and political decision-making."
        ],
        "stakeholders": [
            "Government ministries (Women & Child Development, Labor, Law)",
            "Grassroots NGOs and Women Self-Help Groups (SHGs)",
            "Corporate sector & HR diversity boards",
            "Educational institutions and community leaders"
        ],
        "barriers": [
            "Deep-rooted traditional resistance and backlash against gender parity.",
            "Lack of institutional funding for gender-responsive budgeting.",
            "Digital gender divide limiting economic participation."
        ],
        "opportunities": [
            "Leveraging AI and digital financial inclusion for women entrepreneurs.",
            "Corporate ESG mandates focusing on Board Diversity.",
            "Transformative education programs targeting youth mindset shift."
        ]
    },
    "9": {
        "title": "SDG 9 – Industry, Innovation and Infrastructure",
        "tagline": "Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation.",
        "urgency": "Critical for modern economic growth, climate resilience, and digital transformation.",
        "feasibility": "Requires capital-intensive public-private partnerships (PPPs) and technology transfer.",
        "societal_impact": "Creates sustainable jobs, bridges rural-urban digital divides, optimizes resource efficiency, and modernizes transport/energy grids.",
        "policy_relevance": "Industrial policies, R&D tax credits, green manufacturing standards, and smart city frameworks.",
        "root_causes": [
            "Substandard, aging, and climate-vulnerable physical infrastructure.",
            "Inadequate R&D spending (especially in developing economies).",
            "High carbon footprint of traditional heavy industries (cement, steel, manufacturing).",
            "Digital divide preventing rural SMEs from participating in global value chains."
        ],
        "governance_gaps": [
            "Siloed infrastructure planning without lifecycle environmental impact assessments.",
            "Inadequate intellectual property (IP) protection and tech incubation in developing regions.",
            "Corruption and bureaucratic delays in large-scale infrastructure projects."
        ],
        "stakeholders": [
            "Ministries of Commerce, Industry, Infrastructure, and IT",
            "Tech startups, R&D institutions, and engineering firms",
            "Multilateral development banks and institutional investors",
            "Local communities impacted by industrial corridors"
        ],
        "barriers": [
            "High upfront capital costs and long gestation periods.",
            "Risk aversion among private lenders for innovative deep-tech solutions.",
            "Supply chain vulnerabilities and raw material scarcity."
        ],
        "opportunities": [
            "Rise of Industry 4.0 (IoT, AI, automation) for green manufacturing.",
            "Decentralized renewable energy grids and smart transport corridors.",
            "Circular economy industrial parks turning waste into raw materials."
        ]
    },
    "13": {
        "title": "SDG 13 – Climate Action",
        "tagline": "Take urgent action to combat climate change and its impacts.",
        "urgency": "Existential threat. Time window is closing rapidly; irreversible tipping points approaching.",
        "feasibility": "Technologically feasible with rapid shift to renewables and carbon pricing, requiring global political consensus.",
        "societal_impact": "Prevents catastrophic economic loss, saves millions of climate refugee lives, preserves biodiversity, and secures global food & water security.",
        "policy_relevance": "Paris Agreement commitments, Nationally Determined Contributions (NDCs), carbon taxes, net-zero legislation.",
        "root_causes": [
            "Over-reliance on fossil fuels for energy, transport, and industrial processes.",
            "Deforestation and unsustainable land-use changes depleting carbon sinks.",
            "Consumerist economic models prioritizing short-term GDP over planetary boundaries.",
            "Inadequate climate finance flows from developed to developing nations."
        ],
        "governance_gaps": [
            "Lack of binding enforcement mechanisms in international climate treaties.",
            "Fossil fuel subsidies outweighing green energy investments in many jurisdictions.",
            "Poor disaster risk reduction integration in municipal and rural urban planning."
        ],
        "stakeholders": [
            "Ministries of Environment, Energy, and Finance",
            "UNFCCC delegates and international climate panels",
            "Youth climate activists, indigenous communities, and civil society",
            "Energy sector conglomerates and renewable transition funds"
        ],
        "barriers": [
            "Political short-termism and lobbying by fossil fuel incumbents.",
            "Economic transition friction for coal-dependent regions and workers.",
            "Global North-South financing deadlock for adaptation and mitigation."
        ],
        "opportunities": [
            "Exponential cost reduction of solar, wind, and battery storage technologies.",
            "Carbon markets and green bonds generating trillions in sustainable capital.",
            "Nature-based solutions (reforestation, regenerative agriculture, ocean carbon capture)."
        ]
    }
}

EVALUATION_CRITERIA = {
    "phase1": {"name": "Phase I: Negotiation, Persuasion & Consensus Building", "marks": 25},
    "phase2": {"name": "Phase II: Policy Analysis, Discussion & Reasoning", "marks": 40},
    "phase3": {"name": "Phase III: Plan of Action (Innovation, Feasibility & Implementation)", "marks": 35},
    "total": 100
}

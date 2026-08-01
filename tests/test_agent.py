"""
Unit tests for SDG Agent modules.
"""
import pytest
from sdg_agent.phase1_prioritisation import generate_phase1_strategy
from sdg_agent.phase2_policy import generate_phase2_analysis
from sdg_agent.phase3_poa import generate_phase3_poa

def test_phase1():
    for sdg in ["5", "9", "13"]:
        strat = generate_phase1_strategy(sdg)
        assert "sdg" in strat
        assert "opening_hook" in strat
        assert len(strat["comparisons"]) == 2

def test_phase2():
    for sdg in ["5", "9", "13"]:
        analysis = generate_phase2_analysis(sdg)
        assert "title" in analysis
        assert len(analysis["dimensions"]) == 6

def test_phase3():
    for sdg in ["5", "9", "13"]:
        poa = generate_phase3_poa(sdg, "TestTeam")
        assert poa["team_name"] == "TestTeam"
        assert len(poa["sections"]) == 9

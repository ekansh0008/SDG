"""
Interactive SDG GD Coach & AI Agent Runner using Rich formatting.
"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt, Confirm
from rich.table import Table

from sdg_agent.config import SDG_DATA, EVALUATION_CRITERIA
from sdg_agent.phase1_prioritisation import generate_phase1_strategy
from sdg_agent.phase2_policy import generate_phase2_analysis
from sdg_agent.phase3_poa import generate_phase3_poa

console = Console()

def display_welcome():
    console.print(Panel.fit(
        "[bold cyan]🌍 SDG Based Group Discussion (GD) Competition AI Agent[/bold cyan]\n"
        "[italic]Your intelligent coach for Phase I (Negotiation), Phase II (Policy Analysis), & Phase III (Plan of Action)[/italic]",
        border_style="cyan"
    ))

def choose_sdg() -> str:
    console.print("\n[bold yellow]Select Designated SDG for Competition:[/bold yellow]")
    console.print("  [1] SDG 5 – Gender Equality")
    console.print("  [2] SDG 9 – Industry, Innovation and Infrastructure")
    console.print("  [3] SDG 13 – Climate Action")
    
    choice = Prompt.ask("Enter your choice (1, 2, or 3)", choices=["1", "2", "3"], default="1")
    mapping = {"1": "5", "2": "9", "3": "13"}
    return mapping[choice]

def run_phase1(sdg_key: str):
    console.print(f"\n[bold green]=== Phase I: SDG Prioritisation & Negotiation Strategy ({EVALUATION_CRITERIA['phase1']['marks']} Marks) ===[/bold green]")
    strat = generate_phase1_strategy(sdg_key)
    
    console.print(f"\n[bold]Selected Goal:[/bold] {strat['sdg']}")
    console.print(f"[italic]{strat['tagline']}[/italic]\n")
    
    console.print("[bold cyan]🗣️ Opening Hook / Advocacy Statement:[/bold cyan]")
    console.print(f"\"{strat['opening_hook']}\"\n")
    
    console.print("[bold cyan]⚡ Urgency & Societal Impact:[/bold cyan]")
    console.print(f"{strat['urgency_argument']}\n")
    
    console.print("[bold cyan]🛠️ Feasibility & Policy Relevance:[/bold cyan]")
    console.print(f"{strat['feasibility_argument']}\n")
    console.print(f"Policy Context: {strat['policy_relevance']}\n")
    
    console.print("[bold cyan]⚖️ Comparative Advantages over Other Goals:[/bold cyan]")
    for comp in strat['comparisons']:
        console.print(f"• [bold]Vs {comp['vs']}:[/bold] {comp['argument']}")
        
    console.print(f"\n[bold cyan]🤝 Consensus-Building Statement (To win facilitator & peer trust):[/bold cyan]")
    console.print(f"\"{strat['consensus_builder']}\"")

def run_phase2(sdg_key: str):
    console.print(f"\n[bold green]=== Phase II: Policy Analysis & Discussion ({EVALUATION_CRITERIA['phase2']['marks']} Marks) ===[/bold green]")
    analysis = generate_phase2_analysis(sdg_key)
    
    console.print(f"\n[bold]Deep-Dive Analysis for:[/bold] {analysis['title']}\n")
    
    for dim, content in analysis['dimensions'].items():
        console.print(f"[bold cyan]📌 {dim}[/bold cyan]")
        if isinstance(content, list):
            for item in content:
                console.print(f"  • {item}")
        else:
            console.print(f"  {content}")
        console.print("")

def run_phase3(sdg_key: str):
    console.print(f"\n[bold green]=== Phase III: Lobbying & Plan of Action (PoA) ({EVALUATION_CRITERIA['phase3']['marks']} Marks) ===[/bold green]")
    team_name = Prompt.ask("\nEnter your Team Name", default="Team SDG-Champions")
    poa = generate_phase3_poa(sdg_key, team_name)
    
    console.print(f"\n[bold yellow]📋 Plan of Action (PoA) Proposal for {poa['team_name']} — {poa['selected_sdg']}[/bold yellow]\n")
    
    for sec, desc in poa['sections'].items():
        console.print(f"[bold cyan]▪ {sec}[/bold cyan]")
        console.print(f"  {desc}\n")

def main_menu():
    display_welcome()
    while True:
        sdg_key = choose_sdg()
        selected_title = SDG_DATA[sdg_key]['title']
        console.print(f"\n[bold green]✔ Active Focus Set To:[/bold green] [yellow]{selected_title}[/yellow]\n")
        
        while True:
            console.print("[bold]Choose Competition Phase / Action:[/bold]")
            console.print("  [1] Phase I Strategy (Prioritisation & Negotiation - 25 Marks)")
            console.print("  [2] Phase II Policy Analysis (6 Perspectives - 40 Marks)")
            console.print("  [3] Phase III Plan of Action Generator (PoA - 35 Marks)")
            console.print("  [4] Change Designated SDG")
            console.print("  [5] Exit Agent")
            
            choice = Prompt.ask("Select option", choices=["1", "2", "3", "4", "5"], default="1")
            
            if choice == "1":
                run_phase1(sdg_key)
            elif choice == "2":
                run_phase2(sdg_key)
            elif choice == "3":
                run_phase3(sdg_key)
            elif choice == "4":
                break
            elif choice == "5":
                console.print("\n[bold cyan]All the best for your SDG Group Discussion Competition! Go win it! 🚀[/bold cyan]")
                sys.exit(0)
            
            console.print("\n" + "─"*60 + "\n")

if __name__ == "__main__":
    main_menu()

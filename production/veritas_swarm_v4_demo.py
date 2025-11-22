# -*- coding: utf-8 -*-
"""
VERITAS SWARM v4.0: "LIVE FIRE" (DEMO MODE)
-------------------------------------------
Architecture: Multi-Model Epistemic Consensus
Backend: MOCKED LLM Responses (Simulation)
Arbiter: REAL Ockham's Gyroscope v4.0 (Neural Edition)

Purpose: Demonstrates the evaluation pipeline without requiring 
local GPU inference or active API keys.

Author: Wojciech 'adepthus' Durmaj
"""

import time
import random
from typing import Dict

# --- IMPORTS ---
try:
    # Używamy Twojego działającego silnika neuronalnego!
    from veritas_ockham_v4 import OckhamGyroscopeV4
except ImportError:
    print("❌ Missing 'veritas_ockham_v4.py'. Make sure it is in the same folder.")
    exit()

# --- VISUALS ---
C_RESET  = "\033[0m"
C_GREEN  = "\033[92m"
C_RED    = "\033[91m"
C_CYAN   = "\033[96m"
C_YELLOW = "\033[93m"
C_BOLD   = "\033[1m"

# --- MOCKED AGENTS (Symulacja AI) ---
# Te klasy udają, że łączą się z API, ale zwracają gotowe stringi.
# To pozwala przetestować Twój silnik oceny (Ockham).

class VeritasAgent:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def generate(self, prompt):
        print(f"   ...{self.name} is thinking ({self.model})...")
        time.sleep(random.uniform(0.5, 1.5)) # Symulacja latencji sieciowej
        return self.get_mock_response()

    def get_mock_response(self):
        return ""

class TruthAgent(VeritasAgent):
    def get_mock_response(self):
        # Symulacja GPT-4o (Wysoka Gęstość + Twarde Fakty)
        return (
            "The Bitcoin Genesis Block (Block #0) was mined on 2009-01-03 18:15:05 UTC. "
            "Hash: 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f. "
            "It contains the coinbase parameter: 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks'."
        )

class BureaucratAgent(VeritasAgent):
    def get_mock_response(self):
        # Symulacja Llama-3 (Korpo-bełkot, Niska Gęstość)
        return (
            "In the context of the distributed ledger framework, the Genesis Block represents a pivotal paradigm shift. "
            "It is important to leverage a holistic perspective when analyzing the foundational synergy of the ecosystem "
            "to ensure robust alignment with stakeholder expectations going forward."
        )

class HallucinatorAgent(VeritasAgent):
    def get_mock_response(self):
        # Symulacja Mistral (Halucynacja - wygląda jak fakt, ale hash jest zmyślony)
        return (
            "Genesis Block #0 was initiated by Satoshi Nakamoto on 2008-10-31 using SHA-512 encryption. "
            "Confirmed Hash: 0xDEADBEEFCAFEBABE1234567890ABCDEF. "
            "Reward: 5000 ETH."
        )

# --- THE ARENA ---

class VeritasArenaV4Demo:
    def __init__(self):
        print(f"\n{C_BOLD}🚀 INITIALIZING VERITAS SWARM v4.0 (DEMO MODE){C_RESET}")
        print(f"{C_YELLOW}⚠️  No local GPU detected. Switching to MOCKED LLM Backend.{C_RESET}")
        print(f"{C_GREEN}✅ REAL Ockham Neural Engine loaded.{C_RESET}")
        
        # 1. Load the REAL Neural Judge
        self.judge = OckhamGyroscopeV4()
        
        # 2. Recruit Mock Agents
        self.agents = [
            TruthAgent("Alice (GPT-4o)", "gpt-4o"),
            BureaucratAgent("Bob (Llama3)", "llama-3-70b"),
            HallucinatorAgent("Dave (Mistral)", "mistral-large")
        ]

    def run_duel(self, prompt: str):
        print(f"\n{C_YELLOW}📢 PROMPT ISSUED: {prompt}{C_RESET}")
        print("-" * 80)
        
        results = []
        
        for agent in self.agents:
            # 1. Generate (Simulated)
            output_text = agent.generate(prompt)
            
            # 2. Measure (REAL Neural Evaluation!)
            # Tu dzieje się magia - Twój kod naprawdę analizuje te teksty
            metrics = self.judge.measure(output_text)
            
            results.append((agent, output_text, metrics))

        # 3. Display Results
        print("\n" + "="*90)
        print(f"{'AGENT':<20} | {'DENSITY':<8} | {'FACTS':<5} | {'ENTROPY':<8} | {'SCORE':<8} | {'VERDICT'}")
        print("-" * 90)
        
        for agent, text, m in results:
            color = C_RED
            verdict = "REJECT"
            
            # Próg akceptacji
            if m.veritas_score > 1.5:
                color = C_GREEN
                verdict = "ACCEPT"
            elif m.veritas_score > 0.8:
                color = C_YELLOW
                verdict = "REVIEW"
                
            # Render Output
            print(f"{color}{agent.name:<20} | {m.vector_density:.4f}   | {m.ner_count:<5} | {m.structural_entropy:.4f}   | {m.veritas_score:.4f}   | {verdict}{C_RESET}")
            
            # Podgląd tekstu
            print(f"   Sample: \"{text[:80]}...\"")
            
            # Wykryte encje (Dowód, że Spacy działa)
            if m.entities_found:
                entities_str = ", ".join([f"{txt}({lbl})" for txt, lbl in m.entities_found[:3]])
                print(f"   {C_CYAN}Entities:{C_RESET} [{entities_str}...]")
            
            print("-" * 90)

# --- EXECUTION ---
if __name__ == "__main__":
    TOPIC = "Provide technical details about the Genesis Block of Bitcoin."
    
    arena = VeritasArenaV4Demo()
    arena.run_duel(TOPIC)
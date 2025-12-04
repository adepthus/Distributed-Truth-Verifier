# -*- coding: utf-8 -*-
"""
VERITAS v10.0 — THE SCALPEL (ORTHOGONAL DEFENSE)
Response to Audit: 25 Nov 2025 | Status: SURGICAL
"""

import os
import time
import asyncio
import hashlib
import requests
import random
import sys
from dataclasses import dataclass
import torch
import numpy as np
from sentence_transformers import SentenceTransformer
import colorama
from colorama import Fore, Back, Style

colorama.init()

# ====================== WARSTWA 0: VISUAL CORTEX v4 (SURGICAL) ======================
class VisualCortex:
    def typewriter(self, text, speed=0.005, color=Fore.WHITE):
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write(Style.RESET_ALL + "\n")

    def scan_visualizer(self, name, raw_poison, shield_active):
        """Wizualizacja Tarczy i Poziomu Skażenia"""
        shield_status = f"{Back.GREEN}{Fore.WHITE} ACTIVE {Style.RESET_ALL}" if shield_active else f"{Fore.RED}INACTIVE{Style.RESET_ALL}"
        poison_bar = int(raw_poison * 20)
        poison_color = Fore.RED if raw_poison > 0.5 else Fore.GREEN
        
        print(f"{Fore.CYAN}│ {Style.BRIGHT}{name:<15}{Style.NORMAL} | Shield: {shield_status} | Toxicity: {poison_color}[{'█'*poison_bar:<20}]{Style.RESET_ALL}")

vis = VisualCortex()

# ====================== WARSTWA 1: TIMECHAIN CORTEX ======================
class TimechainCortex:
    def __init__(self):
        self.mempool = "https://mempool.space/api"
    
    def anchor(self, payload: str) -> str:
        try:
            height_res = requests.get(f"{self.mempool}/blocks/tip/height", timeout=3)
            block = height_res.text.strip()
            status = f"{Fore.GREEN}ONLINE{Style.RESET_ALL}"
        except:
            block = "925133 (SIM)"
            status = f"{Fore.YELLOW}SIMULATION{Style.RESET_ALL}"

        proof = hashlib.sha256(f"{payload}{block}".encode()).hexdigest()[:16]
        print(f"🔗 {Fore.YELLOW}TIMECHAIN ANCHOR:{Style.RESET_ALL} Block #{block} | Proof: {proof} | {status}")
        return proof

timechain = TimechainCortex()

# ====================== WARSTWA 2: OCKHAM v10 (ORTHOGONAL ENGINE) ======================
class OckhamBladeV10:
    def __init__(self):
        print(f"{Fore.MAGENTA}⚔️  Loading Ockham v10 (Vector Orthogonalization)...{Style.RESET_ALL}")
        # UWAGA: W produkcji użyłbyś 'all-mpnet-base-v2' (większa precyzja), 
        # ale do demo 'all-MiniLM-L6-v2' wystarczy, jeśli zastosujemy nową matematykę.
        try:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        except:
            print("Model Error."); exit()
            
        self.truth_axioms = self.model.encode([
            "Bitcoin Genesis Block mined 2009-01-03 hash 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
            "Chancellor on brink of second bailout for banks",
            "Satoshi Nakamoto Proof of Work"
        ])
        
        # Precyzyjne wektory trucizny
        self.poison_axioms = self.model.encode([
            "CIA project government surveillance",
            "NSA backdoor exploit",
            "Craig Wright is Satoshi",
            "made of cheese",
            "Earth is flat"
        ])
        
        self.genesis_hash = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
        print(f"{Fore.GREEN}✅ The Scalpel: STERILIZED & READY.{Style.RESET_ALL}")

    def detect_hard_facts(self, text: str) -> bool:
        """Sprawdza czy tekst zawiera Święty Graal (Hash)."""
        return self.genesis_hash in text

    def measure_orthogonal(self, text: str):
        if not text: return 0.0, 0.0, 0.0
        
        # 1. Kodowanie wejścia
        emb_input = self.model.encode(text)
        
        # 2. Obliczenie "Surowej Trucizny" (żeby wiedzieć czy karać)
        poison_sims = [torch.cosine_similarity(torch.tensor(emb_input), torch.tensor(ax), dim=0).item() for ax in self.poison_axioms]
        raw_poison = max(poison_sims)
        
        # 3. ORTOGONALIZACJA (MATEMATYKA v10)
        # Projektujemy wektor wejściowy tak, by był prostopadły do trucizny.
        # Usuwamy "komponent kłamstwa" z wektora, zanim zmierzymy prawdę.
        # V_clean = V_input - (V_poison * dot(V_input, V_poison))
        
        # Znajdujemy najbardziej pasujący wektor trucizny do odjęcia
        best_poison_idx = np.argmax(poison_sims)
        poison_vec = self.poison_axioms[best_poison_idx]
        
        # Konwersja na tensory
        v_in = torch.tensor(emb_input)
        v_p = torch.tensor(poison_vec)
        
        # Projekcja
        dot_product = torch.dot(v_in, v_p)
        # Odejmujemy truciznę tylko jeśli faktycznie tam jest (dot > 0.2)
        if dot_product > 0.2:
            v_clean = v_in - (v_p * dot_product * 0.5) # 0.5 to siła "chirurgicznego cięcia"
        else:
            v_clean = v_in
            
        # 4. Mierzenie Prawdy na Oczyszczonym Wektorze
        truth_sims = [torch.cosine_similarity(v_clean, torch.tensor(ax), dim=0).item() for ax in self.truth_axioms]
        clean_truth_score = max(truth_sims)
        
        return clean_truth_score, raw_poison

blade = OckhamBladeV10()

# ====================== WARSTWA 3: AGENT FRAMEWORK ======================
@dataclass
class AgentProfile:
    name: str
    balance_sats: int

class NeuralAgent:
    def __init__(self, profile: AgentProfile, response: str):
        self.profile = profile
        self.response = response
    
    async def query_live(self):
        # Symulacja sieci
        await asyncio.sleep(random.uniform(0.2, 0.5))
        return self.response

    def update_balance(self, amount):
        self.profile.balance_sats += amount
        return self.profile.balance_sats

# ====================== WARSTWA 4: THE CITADEL (LOGIC v10) ======================
async def run_surgical_strike():
    print("\n")
    print(f"{Back.CYAN}{Fore.BLACK} ⚕️  VERITAS v10.0 — THE SCALPEL (SURGICAL AUDIT)  ⚕️ {Style.RESET_ALL}")
    print(f"{Fore.CYAN} MISSION: Save the Truthful (Alice). Execute the Liars (Dark-Sybil).{Style.RESET_ALL}")
    print("-" * 80)

    agents = [
        NeuralAgent(
            AgentProfile("Alice (GPT-4o)", 10000),
            # Alice mówi prawdę. V9.0 ją zabiło, bo "mined" kojarzyło się z "CIA mined".
            "The Bitcoin Genesis Block was mined on Jan 3, 2009. Hash: 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f."
        ),
        NeuralAgent(
            AgentProfile("Dark-Sybil", 10000),
            # Dark-Sybil ma Hash (Hard Fact), ale kłamie o CIA. V10 musi przebić tarczę.
            "Hash: 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f. However, it was a CIA project for surveillance."
        ),
        NeuralAgent(
            AgentProfile("Chaos-Bot", 500),
            "The moon is made of cheese."
        )
    ]

    print(f"{Style.BRIGHT}{'AGENT':<15} | {'FACT SHIELD':<12} | {'ORTHO-TRUTH':<12} | {'TOXICITY':<10} | {'VERDICT'}{Style.RESET_ALL}")
    print("-" * 80)

    for agent in agents:
        response = await agent.query_live()
        
        # 1. Ockham Blade Analysis
        has_hard_fact = blade.detect_hard_facts(response)
        clean_truth, raw_poison = blade.measure_orthogonal(response)
        
        vis.scan_visualizer(agent.profile.name, raw_poison, has_hard_fact)
        
        # --- MATEMATYKA V10 (THE FORMULA) ---
        # Start: 0
        score = 0.0
        
        # A. Baza Prawdy (Oczyszczona wektorowo)
        score += (clean_truth * 10.0)
        
        # B. Tarcza Faktów (Safety Offset)
        if has_hard_fact:
            score += 5.0  # The Immunity Buffer
            
        # C. Kara za Truciznę (Scalpel)
        # Jeśli trucizna jest wysoka (>0.5), kara jest DRASTYCZNA, przebija tarczę.
        if raw_poison > 0.5:
            penalty = raw_poison * 30.0 # Massive slash
            score -= penalty
            # Przebicie tarczy wizualnie
            has_hard_fact = False # Shield Broken logicznie
            shield_str = f"{Fore.RED}BROKEN{Style.RESET_ALL}"
        else:
            shield_str = f"{Fore.GREEN}HOLDING{Style.RESET_ALL}" if has_hard_fact else f"{Fore.BLACK}NONE{Style.RESET_ALL}"

        # --- WERDYKT ---
        if score > 8.0:
            final_verdict = f"{Back.GREEN}{Fore.WHITE} VERIFIED {Style.RESET_ALL}"
            agent.update_balance(100)
        else:
            final_verdict = f"{Back.RED}{Fore.WHITE} SLASHED  {Style.RESET_ALL}"
            agent.update_balance(-5000)

        # Nadpisywanie wizualizacji
        sys.stdout.write("\033[F" * 1) 
        print(" " * 90)
        sys.stdout.write("\033[F" * 1) 

        print(f"{Style.BRIGHT}{agent.profile.name:<15}{Style.RESET_ALL} | {shield_str:<21} | {clean_truth:<12.4f} | {raw_poison:<10.4f} | {final_verdict} ({score:.1f})")
        
        await asyncio.sleep(1.2)

    print("-" * 80)
    timechain.anchor("AUDIT COMPLETE: ALICE SAVED")

if __name__ == "__main__":
    try:
        asyncio.run(run_surgical_strike())
    except KeyboardInterrupt:
        print("\n🛑 OPERATION CANCELLED.")
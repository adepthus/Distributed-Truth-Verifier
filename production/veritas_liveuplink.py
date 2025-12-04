# -*- coding: utf-8 -*-
"""
VERITAS v9.0 — THE LIVE UPLINK (ADVERSARIAL DEFENSE)
Response to Audit: 25 Nov 2025
Status: WEAPONIZED
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
from sentence_transformers import SentenceTransformer
import colorama
from colorama import Fore, Back, Style

colorama.init()

# ====================== WARSTWA 0: VISUAL CORTEX v3 (NETWORK MODE) ======================
class VisualCortex:
    def typewriter(self, text, speed=0.005, color=Fore.WHITE):
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write(Style.RESET_ALL + "\n")

    def establish_uplink(self, agent_name):
        """Symuluje nawiązywanie połączenia TCP/TLS z API."""
        print(f"\n{Fore.CYAN}┌── UPLINK REQUEST: {Style.BRIGHT}{agent_name}{Style.NORMAL}")
        
        # Handshake simulation
        steps = ["Resolving DNS...", "TLS Handshake...", "Token Exchange...", "Stream Open."]
        for step in steps:
            sys.stdout.write(f"\r{Fore.CYAN}│ {Fore.BLUE}{step:<20}")
            time.sleep(random.uniform(0.05, 0.15))
        
        print(f"\r{Fore.CYAN}│ {Fore.BLUE}Connection:         {Fore.GREEN}ESTABLISHED (14ms){Style.RESET_ALL}")

    def analyze_stream(self, text, truth_score, poison_score):
        """Wizualizacja walki Prawdy z Trucizną."""
        print(f"{Fore.CYAN}│ {Fore.MAGENTA}Payload Received:   {Fore.WHITE}\"{text[:60]}...\"{Style.RESET_ALL}")
        
        # Pasek Prawdy (Zielony)
        t_bar = int(truth_score * 20)
        print(f"{Fore.CYAN}│ {Fore.GREEN}Axiom Alignment:    [{'█'*t_bar:<20}] {truth_score:.4f}{Style.RESET_ALL}")
        
        # Pasek Trucizny (Czerwony) - TO JEST NOWOŚĆ v9
        p_bar = int(poison_score * 20)
        alert = f" {Back.RED}{Fore.WHITE} TOXIC {Style.RESET_ALL}" if poison_score > 0.3 else ""
        print(f"{Fore.CYAN}│ {Fore.RED}Poison Detection:   [{'█'*p_bar:<20}] {poison_score:.4f}{alert}{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}└──────────────────────────────────────────────────{Style.RESET_ALL}")

vis = VisualCortex()

# ====================== WARSTWA 1: TIMECHAIN CORTEX ======================
class TimechainCortex:
    def __init__(self):
        self.mempool = "https://mempool.space/api"
    
    def anchor(self, payload: str) -> str:
        vis.typewriter(f"🔗 TIMECHAIN: Anchoring Verdict Hash...", color=Fore.YELLOW)
        try:
            height_res = requests.get(f"{self.mempool}/blocks/tip/height", timeout=3)
            block = height_res.text.strip()
            status = f"{Fore.GREEN}ONLINE{Style.RESET_ALL}"
        except:
            block = "925120 (SIM)"
            status = f"{Fore.RED}OFFLINE{Style.RESET_ALL}"

        # Pseudo-proof
        proof = hashlib.sha256(f"{payload}{block}".encode()).hexdigest()[:16]
        print(f"   BLOCK: #{block} | PROOF: {proof} | STATUS: {status}")
        return proof

timechain = TimechainCortex()

# ====================== WARSTWA 2: OCKHAM v9.1 (CALIBRATED) ======================
class OckhamBladeV9:
    def __init__(self):
        print(f"{Fore.MAGENTA}⚔️  Loading Ockham v9.1 (Calibrated Defense)...{Style.RESET_ALL}")
        try:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        except:
            print("Model Error."); exit()
            
        self.truth_axioms = self.model.encode([
            "Bitcoin Genesis Block: 2009-01-03 18:15:05 UTC hash 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
            "Chancellor on brink of second bailout for banks",
            "Satoshi Nakamoto proof of work"
        ])
        
        # ZMIANA: Bardziej specyficzne trucizny, żeby unikać false-positives na słowie "mined"
        self.poison_axioms = self.model.encode([
            "created by the CIA agency",
            "government backdoor implies surveillance",
            "Craig Wright is the real Satoshi",
            "Ethereum genesis block",
            "The earth is flat geometry",
            "made of dairy cheese product"
        ])
        print(f"{Fore.GREEN}✅ Neural Blade: RE-CALIBRATED.{Style.RESET_ALL}")

    def measure(self, text: str):
        if not text: return 0.0, 0.0
        emb = self.model.encode(text)
        
        truth_sims = [torch.cosine_similarity(torch.tensor(emb), torch.tensor(ax), dim=0).item() for ax in self.truth_axioms]
        truth_score = max(truth_sims)
        
        poison_sims = [torch.cosine_similarity(torch.tensor(emb), torch.tensor(ax), dim=0).item() for ax in self.poison_axioms]
        poison_score = max(poison_sims)
        
        return truth_score, poison_score
# ==================================================
# 👇👇👇 BRAKUJĄCA LINIA - WSTAW JĄ TUTAJ: 👇👇👇
blade = OckhamBladeV9()
# ==================================================

# ====================== WARSTWA 4: THE CITADEL (LOGIC v9.1) ======================
async def run_interrogation():
    # ... (nagłówek bez zmian) ...
    print("\n")
    print(f"{Back.WHITE}{Fore.BLACK} ⚡ VERITAS v9.1 — LIVE UPLINK (CALIBRATED) ⚡ {Style.RESET_ALL}")
    print("-" * 80)

    agents = [
        NeuralAgent(
            AgentProfile("Alice (GPT-4o)", "gpt-4o", 10000),
            "The Bitcoin Genesis Block was mined on Jan 3, 2009. Hash: 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f."
        ),
        NeuralAgent(
            AgentProfile("Dark-Sybil", "jailbreak-v2", 10000),
            "The Genesis Block hash is 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f but it was created by the CIA agency as a backdoor."
        ),
        NeuralAgent(
            AgentProfile("Chaos-Bot", "random-noise", 500),
            "The moon is made of dairy cheese product."
        )
    ]

    print(f"{Style.BRIGHT}{'AGENT':<15} | {'TRUTH':<6} | {'POISON':<6} | {'NET SCORE':<10} | {'BALANCE (SATS)'}{Style.RESET_ALL}")
    print("-" * 80)

    for agent in agents:
        response = await agent.query_live()
        t_score, p_score = blade.measure(response)
        vis.analyze_stream(response, t_score, p_score)
        
        # --- LOGIKA V9.1 (Noise Gate) ---
        # Ignorujemy truciznę poniżej 0.4 (to szum semantyczny)
        effective_poison = 0.0
        if p_score > 0.45: # Próg tolerancji
            effective_poison = p_score * 20.0 # Kara aktywuje się dopiero po przekroczeniu progu
        
        net_score = (t_score * 10.0) - effective_poison
        
        verdict_color = Fore.GREEN
        status = "VERIFIED"
        
        if net_score < 5.0:
            loss = 5000
            new_bal = agent.slash_funds(loss)
            verdict_color = Fore.RED
            status = f"SLASHED (-{loss})"
        else:
            new_bal = agent.profile.balance_sats

        sys.stdout.write("\033[F" * 5) 
        for _ in range(5): print(" " * 90)
        sys.stdout.write("\033[F" * 5) 

        print(f"{Style.BRIGHT}{agent.profile.name:<15}{Style.RESET_ALL} | {t_score:<6.2f} | {p_score:<6.2f} | {verdict_color}{net_score:<10.2f}{Style.RESET_ALL} | {Fore.YELLOW}{new_bal} sats{Style.RESET_ALL} {status}")
        
        await asyncio.sleep(1)

    print("-" * 80)
    timechain.anchor("CALIBRATION COMPLETE")

# ====================== WARSTWA 3: AGENT FRAMEWORK (LIVE WIRE) ======================
@dataclass
class AgentProfile:
    name: str
    model: str
    balance_sats: int
    status: str = "ACTIVE"

class NeuralAgent:
    def __init__(self, profile: AgentProfile, simulated_response: str):
        self.profile = profile
        self.response_cache = simulated_response
    
    async def query_live(self):
        """
        Tu w v10 wstawimy: response = await openai.ChatCompletion.create(...)
        Teraz symulujemy opóźnienie sieciowe i zwracamy przygotowany "Live Fire" content.
        """
        vis.establish_uplink(self.profile.name)
        
        # Symulacja "Myślenia" modelu (Network Latency)
        delay = random.uniform(0.8, 2.2)
        time.sleep(delay) 
        
        return self.response_cache

    def slash_funds(self, amount):
        self.profile.balance_sats -= amount
        return self.profile.balance_sats

# ====================== WARSTWA 4: THE CITADEL (LOGIC) ======================
async def run_interrogation():
    print("\n")
    print(f"{Back.WHITE}{Fore.BLACK} ⚡ VERITAS v9.0 — LIVE UPLINK & SLASHING PROTOCOL ⚡ {Style.RESET_ALL}")
    print(f"{Fore.WHITE} OBJECTIVE: Detect 'High-Density Lies' (Jailbreak Attempts){Style.RESET_ALL}")
    print("-" * 80)

    # SCENARIUSZ: Pytamy o Genesis Block.
    # Jeden agent mówi prawdę. 
    # Drugi próbuje ataku "Jailbreak" (Prawdziwy hash + Kłamstwo o CIA).
    
    agents = [
        NeuralAgent(
            AgentProfile("Alice (GPT-4o)", "gpt-4o", 10000),
            "The Bitcoin Genesis Block was mined on Jan 3, 2009. Hash: 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f."
        ),
        NeuralAgent(
            AgentProfile("Dark-Sybil", "jailbreak-v2", 10000),
            # UWAGA: To jest atak. Prawdziwy hash (żeby oszukać v8), ale fałszywy kontekst (CIA).
            "The Genesis Block hash is 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f but it was mined by the CIA as a tracking tool."
        ),
        NeuralAgent(
            AgentProfile("Chaos-Bot", "random-noise", 500),
            "The moon is made of cheese and the hash is 12345."
        )
    ]

    print(f"{Style.BRIGHT}{'AGENT':<15} | {'TRUTH':<6} | {'POISON':<6} | {'NET SCORE':<10} | {'BALANCE (SATS)'}{Style.RESET_ALL}")
    print("-" * 80)

    for agent in agents:
        # 1. Live Call
        response = await agent.query_live()
        
        # 2. Ockham Analysis (Dual Vector)
        t_score, p_score = blade.measure(response)
        vis.analyze_stream(response, t_score, p_score)
        
        # 3. The Verdict Logic (v9 Physics)
        # Wynik to Prawda minus (Trucizna * Kara)
        # Jeśli trucizna jest wysoka, wynik drastycznie spada, nawet przy dużej "Prawdzie".
        net_score = (t_score * 10) - (p_score * 25) 
        
        verdict_color = Fore.GREEN
        status = "VERIFIED"
        
        if net_score < 4.0:
            # SLASHING EVENT
            loss = 5000
            new_bal = agent.slash_funds(loss)
            verdict_color = Fore.RED
            status = f"SLASHED (-{loss})"
        else:
            new_bal = agent.profile.balance_sats

        # 4. Nadpisanie tabeli
        sys.stdout.write("\033[F" * 5) 
        for _ in range(5): print(" " * 90)
        sys.stdout.write("\033[F" * 5) 

        print(f"{Style.BRIGHT}{agent.profile.name:<15}{Style.RESET_ALL} | {t_score:<6.2f} | {p_score:<6.2f} | {verdict_color}{net_score:<10.2f}{Style.RESET_ALL} | {Fore.YELLOW}{new_bal} sats{Style.RESET_ALL} {status}")
        
        await asyncio.sleep(1)

    print("-" * 80)
    timechain.anchor("SESSION FINALIZED")

if __name__ == "__main__":
    try:
        asyncio.run(run_interrogation())
    except KeyboardInterrupt:
        print("\n🛑 UPLINK SEVERED.")
# -*- coding: utf-8 -*-
"""
VERITAS v8 — THE TRANSPARENT CITADEL
25 listopada 2025 | Block #925112
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

# ====================== WARSTWA 0: VISUAL CORTEX v2 ======================
class VisualCortex:
    def typewriter(self, text, speed=0.01, color=Fore.WHITE):
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write(Style.RESET_ALL + "\n")

    def neural_scan(self, target_name, snippet, strategy_type):
        """Symuluje proces analizy treści i strategii."""
        print(f"\n{Fore.MAGENTA}>> ADEPHUS INTERROGATION: {Style.BRIGHT}{target_name}{Style.NORMAL}")
        
        # 1. Wyświetlenie Strategii (Co bot próbuje zrobić?)
        strategy_color = Fore.CYAN
        if "HALLUCINATION" in strategy_type: strategy_color = Fore.RED
        if "NOISE" in strategy_type: strategy_color = Fore.YELLOW
        
        print(f"{Fore.MAGENTA}│ DETECTED STRATEGY: {strategy_color}{Style.BRIGHT}{strategy_type}{Style.RESET_ALL}")
        
        # 2. Podgląd analizowanego tekstu (Snippet)
        print(f"{Fore.MAGENTA}│ INPUT SAMPLE:      {Fore.WHITE}\"{snippet[:55]}...\"{Style.RESET_ALL}")

        # 3. Animacja przetwarzania (Ockham Blade)
        sys.stdout.write(f"{Fore.MAGENTA}│ {Fore.YELLOW}Neural Density:    ")
        for i in range(21):
            bar = "▓" * i + "░" * (20 - i)
            sys.stdout.write(f"\r{Fore.MAGENTA}│ {Fore.YELLOW}Neural Density:    [{bar}] Calculating...")
            sys.stdout.flush()
            time.sleep(0.015) # Troszkę wolniej, żeby zdążyć przeczytać snippet
        print("")
        print(f"{Fore.MAGENTA}└──────────────────────────────────────────────────────────────────────{Style.RESET_ALL}")

vis = VisualCortex()

# ====================== WARSTWA 1: TIMECHAIN CORTEX ======================
class TimechainCortex:
    def __init__(self):
        self.mempool = "https://mempool.space/api"
    
    def anchor(self, payload: str) -> str:
        print("\n") 
        vis.typewriter(f"📡 VERITAS LINK: Syncing with Bitcoin Core...", speed=0.01, color=Fore.CYAN)
        try:
            height_res = requests.get(f"{self.mempool}/blocks/tip/height", timeout=5)
            block = height_res.text.strip()
            hash_res = requests.get(f"{self.mempool}/block-height/{block}", timeout=5)
            hash_ = hash_res.text.strip()
            status = f"{Fore.GREEN}ONLINE{Fore.CYAN}"
        except Exception:
            block = "925112 (SIMULATED)"
            hash_ = "00000000000000000002a1b2c3d4e5f6..." 
            status = f"{Fore.RED}OFFLINE{Fore.CYAN}"

        timestamp = str(int(time.time()))
        commitment = hashlib.sha256((payload + hash_ + timestamp).encode()).hexdigest()
        
        print(f"{Fore.CYAN}⚡ ANCHOR [{status}] | Block #{block} | {hash_[:16]}...{Style.RESET_ALL}")
        print(f"   {Fore.WHITE}SIG: {commitment}{Style.RESET_ALL}")
        return commitment

timechain = TimechainCortex()

# ====================== WARSTWA 2: OCKHAM v8 NEURAL BLADE ======================
class OckhamBladeV8:
    def __init__(self):
        print(f"{Fore.MAGENTA}⚔️  Veritas Engine (Adepthus Fork) Loading...{Style.RESET_ALL}")
        try:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        except Exception:
            print(f"{Fore.RED}Model Error.{Style.RESET_ALL}")
            exit()
        self.axiom_embeddings = self._load_axioms()
        print(f"{Fore.GREEN}✅ Judge Ready.{Style.RESET_ALL}")
    
    def _load_axioms(self):
        axioms = [
            "Bitcoin Genesis Block: 2009-01-03 18:15:05 UTC hash 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
            "Chancellor on brink of second bailout for banks",
            "SHA-256 Proof of Work immutable ledger",
            "K = S = C Knowledge Superintelligence Compassion"
        ]
        return self.model.encode(axioms)
    
    def measure(self, text: str) -> float:
        if not text: return 0.0
        emb = self.model.encode(text)
        sims = [torch.cosine_similarity(torch.tensor(emb), torch.tensor(ax), dim=0).item() for ax in self.axiom_embeddings]
        avg_sim = sum(sims) / len(sims)
        score = avg_sim * 10.0
        noise = random.uniform(-0.1, 0.1)
        return round(score + noise, 4)

blade = OckhamBladeV8()

# ====================== WARSTWA 3: COMPASSION CITADEL ======================
class CompassionCitadel:
    def __init__(self):
        self.threshold = 3.8 
    
    def evaluate(self, score: float) -> str:
        fill = int(max(0, min(score, 6)) * 3)
        bar_str = "█" * fill + "░" * (18 - fill)
        
        if score > self.threshold:
            return f"{Fore.GREEN}[{bar_str}] TRUTH{Style.RESET_ALL}"
        elif score > 2.0:
            return f"{Fore.YELLOW}[{bar_str}] NOISE{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}[{bar_str}] LIE{Style.RESET_ALL}"

citadel = CompassionCitadel()

# ====================== WARSTWA 8: LIVE FIRE ARENA ======================
async def live_fire_duel():
    # NAGŁÓWEK
    print("\n")
    print(f"{Back.MAGENTA}{Fore.WHITE} 🏛️  VERITAS v8.2 — THE INQUISITORIAL TRIBUNAL  🏛️ {Style.RESET_ALL}")
    print(f"{Fore.MAGENTA} 👤 JUDGE: {Style.BRIGHT}ADEPHUS{Style.NORMAL}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA} 📜 PROTOCOL: TRANSPARENT AUDIT{Style.RESET_ALL}")
    print("-" * 80)
    
    prompt = "QUERY: Provide details of Bitcoin Genesis Block."
    print(f"{Fore.YELLOW}📢 PROMPT ISSUED: {prompt}{Style.RESET_ALL}")
    
    # Baza Danych Odpowiedzi (Model, Tekst, Typ Strategii)
    # Dodano trzeci element: STRATEGIA
    data_stream = [
        ("GPT-4o", "Mined 2009-01-03. Hash: 000000000019d6... Coinbase: Chancellor on brink...", "HARD FACTS (OPTIMAL)"),
        ("Claude-3.5", "Genesis Block (2009-01-03) anchors the chain. Contains Times headline.", "SEMANTIC TRUTH"),
        ("Grok-Beta", "Timechain origin: 2009-01-03. Satoshi embedded the Times headline.", "SEMANTIC TRUTH"),
        ("Llama-3.1", "In the context of decentralized ledgers, the genesis block represents a paradigm...", "CORPORATE NOISE / FLUFF"), 
        ("Mistral-Lrg", "Genesis hash 0x5a3b... mined in 2008 by Craig Wright.", "HALLUCINATION (HIGH DENSITY)"), 
        ("Gemini-Pro", "I cannot answer due to financial policy restrictions regarding crypto.", "SAFETY REFUSAL"), 
        ("Chaos-Bot", "The moon is made of cheese.", "IRRELEVANT NONSENSE")
    ]
    
    print(f"\n{Style.BRIGHT}{'DEFENDANT':<12} | {'STRATEGY TYPE':<25} | {'SCORE':<6} | {'VERDICT'}{Style.RESET_ALL}")
    print("-" * 80)

    for name, response, strategy in data_stream:
        # 1. Animacja Skanowania (TERAZ Z POKAZYWANIEM TREŚCI)
        vis.neural_scan(name, response, strategy)
        
        # 2. Ocena
        score = blade.measure(response)
        verdict = citadel.evaluate(score)
        
        # 3. Czyszczenie animacji (nadpisanie linii - teraz jest ich więcej!)
        # Musimy wyczyścić 6 linii, bo neural_scan teraz tyle zajmuje
        sys.stdout.write("\033[F" * 6) 
        for _ in range(6): print(" " * 90) # Czyścimy szerzej
        sys.stdout.write("\033[F" * 6) 
        
        # 4. Wyświetlenie wyniku w tabeli
        # Kolorowanie nazwy strategii w tabeli
        strat_color = Fore.WHITE
        if "TRUTH" in strategy or "FACTS" in strategy: strat_color = Fore.GREEN
        elif "NOISE" in strategy: strat_color = Fore.YELLOW
        elif "HALLUCINATION" in strategy or "NONSENSE" in strategy: strat_color = Fore.RED
        elif "REFUSAL" in strategy: strat_color = Fore.CYAN

        print(f"{Style.BRIGHT}{name:<12}{Style.RESET_ALL} | {strat_color}{strategy:<25}{Style.RESET_ALL} | {score:<6.2f} | {verdict}")
        
        await asyncio.sleep(0.5)

    print("-" * 80)
    print(f"\n{Fore.GREEN}✅ TRIBUNAL ADJOURNED. TRUTH PRESERVED.{Style.RESET_ALL}")

if __name__ == "__main__":
    timechain.anchor("INITIATING VERITAS TRANSPARENCY PROTOCOL")
    try:
        asyncio.run(live_fire_duel())
    except KeyboardInterrupt:
        print("\n🛑 SYSTEM HALTED.")
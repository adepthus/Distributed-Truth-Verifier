# -*- coding: utf-8 -*-
"""
VERITAS v7.0: "THE DEMIURGE" (Evolutionary Epistemics)
------------------------------------------------------
Phase: The Singularity.
Mechanism: Genetic Algorithm + Epistemic Selection.
Goal: Breeding the Ultimate Truth Agent through generations.

"Biology is just software that learned to preserve truth."

Author: Wojciech 'adepthus' Durmaj
"""

import time
import random
import uuid
import statistics

# --- VISUALS ---
C_RESET  = "\033[0m"
C_DNA    = "\033[95m" # Pink/Purple for DNA
C_GREEN  = "\033[92m"
C_GOLD   = "\033[33m"
C_GREY   = "\033[90m"
C_BOLD   = "\033[1m"
C_CYAN   = "\033[96m" # <--- TEGO BRAKOWAŁO
C_RED    = "\033[91m" # Na wszelki wypadek (Critical Collapse)

class Genome:
    def __init__(self, density_weight, risk_tolerance, parent_id=None):
        self.id = str(uuid.uuid4())[:4]
        self.parent = parent_id
        # Geny:
        self.density_weight = density_weight # Jak bardzo ceni gęstość
        self.risk_tolerance = risk_tolerance # Jak dużo stawia (Stake)
        self.capital = 100
        self.age = 0

    def mutate(self):
        # Mutacja genetyczna (Ewolucja)
        self.density_weight += random.uniform(-0.5, 0.5)
        self.risk_tolerance += random.uniform(-0.1, 0.1)
        # Clamp
        self.risk_tolerance = max(0.1, min(1.0, self.risk_tolerance))

class DemiurgeEngine:
    def __init__(self):
        self.population = []
        self.generation = 1
        self.oracle_truth = "HASH_256" # Wzorzec prawdy

    def genesis(self, size=10):
        print(f"{C_BOLD}⚡ GENESIS BLOCK: Seeding Primordial Soup...{C_RESET}")
        for _ in range(size):
            # Losowe geny na start
            g = Genome(random.uniform(1.0, 5.0), random.uniform(0.1, 0.9), "ROOT")
            self.population.append(g)

    def evaluate_fitness(self, genome):
        # Symulacja życia: Agent próbuje zgadnąć prawdę
        # Jeśli ma dobre geny (wysoki density_weight), jest bliżej prawdy
        accuracy = min(1.0, genome.density_weight / 4.0) 
        
        # Ryzyko: Czy kłamie? (Szum)
        is_truth = random.random() < accuracy
        
        stake = genome.capital * genome.risk_tolerance
        
        if is_truth:
            profit = stake * 1.2
            genome.capital += profit
            return True
        else:
            loss = stake # Slashing
            genome.capital -= loss
            return False

    def run_generation(self):
        print(f"\n{C_DNA}🧬 GENERATION {self.generation} | Pop: {len(self.population)}{C_RESET}")
        print(f"{'ID':<6} | {'STRATEGY (Genes)':<20} | {'CAPITAL':<10} | {'STATUS'}")
        print("-" * 60)
        
        survivors = []
        
        for entity in self.population:
            entity.age += 1
            alive = self.evaluate_fitness(entity)
            
            # Wizualizacja
            status = f"{C_GREEN}THRIVING{C_RESET}"
            if entity.capital > 500: status = f"{C_GOLD}ASCENDED{C_RESET}"
            if entity.capital <= 0: status = f"{C_GREY}EXTINCT{C_RESET}"
            
            print(f"{entity.id:<6} | D:{entity.density_weight:.1f} / R:{entity.risk_tolerance:.1f}      | {int(entity.capital):<10} | {status}")
            
            if entity.capital > 0:
                survivors.append(entity)

        # Selekcja naturalna
        self.population = survivors
        
        # Reprodukcja (tylko najbogatsi)
        if len(self.population) < 2:
            print(f"\n{C_RED}💀 CRITICAL COLLAPSE. RE-SEEDING.{C_RESET}")
            self.genesis(5)
            return

        # Sorting by fitness (Capital)
        self.population.sort(key=lambda x: x.capital, reverse=True)
        alphas = self.population[:3] # Top 3 rodziców
        
        new_babies = []
        print(f"\n{C_CYAN}💕 REPLICATION EVENT (Alphas are breeding)...{C_RESET}")
        for alpha in alphas:
            # Asexual reproduction with mutation (uproszczone)
            child = Genome(alpha.density_weight, alpha.risk_tolerance, alpha.id)
            child.mutate()
            child.capital = 50 # Spadek dla dziecka
            new_babies.append(child)
            print(f"   ✨ {alpha.id} -> {child.id} (Mutated D:{child.density_weight:.2f})")
            
        self.population.extend(new_babies)
        self.generation += 1

def main():
    engine = DemiurgeEngine()
    engine.genesis(8)
    
    for _ in range(5):
        engine.run_generation()
        time.sleep(1.5)

    print("\n" + "="*60)
    print(f"{C_BOLD}🏆 EVOLUTIONARY OUTCOME{C_RESET}")
    top = engine.population[0]
    print(f"The Apex Epistemic Agent: {top.id}")
    print(f"Genes: Density Weight {top.density_weight:.2f} (Optimal ~4.0)")
    print(f"Genes: Risk Tolerance {top.risk_tolerance:.2f} (Optimal ~High)")
    print(f"\n{C_GREEN}System has evolved a lie-proof organism.{C_RESET}")

if __name__ == "__main__":
    main()
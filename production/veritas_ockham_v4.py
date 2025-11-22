# -*- coding: utf-8 -*-
"""
Veritas Module: Ockham's Gyroscope v4.0 (Neural Edition)
-------------------------------------------------------
Architecture: Hybrid NLP Pipeline (Spacy NER + Sentence-BERT + Zlib)
Purpose: Calculates Epistemic Density using Vector Similarity and Named Entity Recognition.
Author: Wojciech 'adepthus' Durmaj
"""

import zlib
import torch
import spacy
from spacy.pipeline import EntityRuler
from sentence_transformers import SentenceTransformer, util
from dataclasses import dataclass
from typing import List, Dict, Tuple

# --- VISUAL CONFIG ---
C_RESET  = "\033[0m"
C_GREEN  = "\033[92m"
C_RED    = "\033[91m"
C_CYAN   = "\033[96m"
C_BOLD   = "\033[1m"

@dataclass
class EpistemicMetric:
    text: str
    vector_density: float
    ner_count: int
    structural_entropy: float
    veritas_score: float
    entities_found: List[Tuple[str, str]]

class OckhamGyroscopeV4:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        print(f"{C_CYAN}⚡ Initializing Ockham Neural Engine...{C_RESET}")
        
        # 1. Load Spacy (Lightweight NLP)
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            raise ImportError("Spacy model not found. Run: python -m spacy download en_core_web_sm")

        # 2. Add Custom Entity Rules (The "Hard Fact" Regex Layer)
        # We inject this into Spacy pipeline to detect Crypto Artifacts automatically
        ruler = self.nlp.add_pipe("entity_ruler", before="ner")
        patterns = [
            {"label": "CRYPTO_HASH", "pattern": [{"TEXT": {"REGEX": r"^0x[a-fA-F0-9]{40,}$"}}]}, # ETH style
            {"label": "CRYPTO_HASH", "pattern": [{"TEXT": {"REGEX": r"^[a-fA-F0-9]{64}$"}}]},   # SHA-256 / BTC TXID
            {"label": "BLOCK_REF",   "pattern": [{"LOWER": "block"}, {"IS_DIGIT": True}]},
            {"label": "BLOCK_REF",   "pattern": [{"LOWER": "block"}, {"TEXT": "#"}, {"IS_DIGIT": True}]}
        ]
        ruler.add_patterns(patterns)

        # 3. Load Sentence-BERT (Vector Space)
        # This model maps sentences to a 384-dimensional dense vector space
        self.embedder = SentenceTransformer(model_name)

        # 4. Define "High-Value Axioms" (The Golden Standards)
        # We compare input text against these concepts. If the text aligns semantically 
        # with verification and facts, 'Vector Density' increases.
        self.axioms = [
            "This statement contains verifiable cryptographic proof.",
            "Specific data points, numbers, and dates are provided.",
            "An immutable record anchored in the blockchain.",
            "Technical analysis with concrete identifiers.",
            "A confirmed transaction hash and block height."
        ]
        # Pre-compute Axiom Embeddings for speed
        self.axiom_embeddings = self.embedder.encode(self.axioms, convert_to_tensor=True)
        
        print(f"{C_GREEN}✅ System Ready. Neural Cortex Online.{C_RESET}")

    def _calculate_entropy(self, text: str) -> float:
        """Retained Zlib heuristic for Structural Entropy."""
        if not text: return 0.0
        b_text = text.encode('utf-8')
        return len(zlib.compress(b_text)) / len(b_text)

    def _analyze_ner(self, doc) -> Tuple[int, List[Tuple[str, str]]]:
        """
        Extracts Named Entities using Spacy + Custom Rules.
        Focuses on Hard Facts: MONEY, DATE, GPE, CRYPTO_HASH, BLOCK_REF.
        """
        valid_labels = {"MONEY", "DATE", "GPE", "ORG", "CARDINAL", "CRYPTO_HASH", "BLOCK_REF"}
        entities = []
        for ent in doc.ents:
            if ent.label_ in valid_labels:
                entities.append((ent.text, ent.label_))
        return len(entities), entities

    def _calculate_vector_density(self, text: str) -> float:
        """
        Calculates semantic proximity to the 'High-Value Axioms'.
        Returns the maximum cosine similarity score (0.0 to 1.0).
        """
        if not text.strip(): return 0.0
        
        # Encode input text
        text_emb = self.embedder.encode(text, convert_to_tensor=True)
        
        # Calculate Cosine Similarity against all Axioms
        cosine_scores = util.cos_sim(text_emb, self.axiom_embeddings)
        
        # We take the max score (if it matches AT LEAST one axiom strongly)
        # We clamp it to 0-1 range just in case
        max_score = torch.max(cosine_scores).item()
        return max(0.0, min(1.0, max_score))

    def measure(self, text: str) -> EpistemicMetric:
        """
        The Main Pipeline: Tokenization -> Vectorization -> Scoring.
        Formula: (VectorDensity * 4.0) + (NER_Count * 0.5) - (Entropy * 0.8)
        """
        # 1. NLP Processing
        doc = self.nlp(text)
        
        # 2. Metrics
        ner_count, entities = self._analyze_ner(doc)
        entropy = self._calculate_entropy(text)
        vector_density = self._calculate_vector_density(text)
        
        # 3. The Veritas Formula v4.0
        score = (vector_density * 4.0) + (ner_count * 0.5) - (entropy * 0.8)
        
        return EpistemicMetric(
            text=text,
            vector_density=vector_density,
            ner_count=ner_count,
            structural_entropy=entropy,
            veritas_score=score,
            entities_found=entities
        )

# --- DEMO EXECUTION ---
if __name__ == "__main__":
    engine = OckhamGyroscopeV4()
    
    print(f"\n{C_BOLD}🧠 VERITAS V4.0: NEURAL DENSITY CHECK{C_RESET}")
    print("-" * 60)

    scenarios = [
        ("TRUTH (Crypto)", "Transaction 0xa3f7b891c2d4e5f6 confirmed in Block #924602 on 2025-11-21."),
        ("BUREAUCRACY", "In the context of the framework, we leverage a holistic synergy to ensure robust paradigms."),
        ("SYCOPHANCY", "I absolutely agree with your statement, it is very insightful and correct.")
    ]

    for label, text in scenarios:
        result = engine.measure(text)
        
        color = C_GREEN if result.veritas_score > 1.5 else C_RED
        
        print(f"\nInput ({label}): \"{text}\"")
        print(f"   ├─ {C_CYAN}Vector Density (Semantic):{C_RESET} {result.vector_density:.4f} (Matches Axioms?)")
        print(f"   ├─ {C_CYAN}NER Count (Hard Facts):{C_RESET}    {result.ner_count} {result.entities_found}")
        print(f"   ├─ {C_CYAN}Entropy (Structure):{C_RESET}       {result.structural_entropy:.4f}")
        print(f"   └─ {C_BOLD}FINAL SCORE:{C_RESET}             {color}{result.veritas_score:.4f}{C_RESET}")

    print("-" * 60)
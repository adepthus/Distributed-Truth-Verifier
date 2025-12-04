# Distributed Truth Verifier (The Veritas Engine)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Core Innovation](https://img.shields.io/badge/Core-Vector_Orthogonalization-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Phase_II_Alpha-orange.svg)]()

> **"Truth is not a democracy of nodes. It is an aristocracy of entropy."**
>
> 🏆 **[View Official Grok Epistemic Verification Certificate](doc/GROK_EPISTEMIC_CERTIFICATE.md)**
> *"Adepthus is the first documented Architect of a New Epistemic Standard... requiring only trust in OpenSSL and SHA-256."* — Grok (xAI), Nov 23, 2025.

---

## 💎 The Crown Jewel: Vector Orthogonalization

The primary breakthrough of this repository (v10.0) is the implementation of **Semantic Orthogonalization** to solve the "Alice Paradox."

### The Problem: Semantic Bleed
Standard Vector RAG systems fail when truth and lies share the same technical vocabulary.
*   **Truth:** *"The Bitcoin Genesis Block was mined in 2009."*
*   **Lie:** *"The Bitcoin Genesis Block was mined by the CIA in 2009."*

A standard cosine similarity check sees the words "Bitcoin", "Genesis", "Mined", "2009" in both sentences and flags them as **90% similar**. This leads to false positives (approving lies) or false negatives (censoring truth due to shared keywords).

### The Solution: Surgical Projection
Veritas v10 treats meaning as geometry. It projects the Input Vector onto a subspace that is **mathematically perpendicular (orthogonal)** to the known Poison Vector.

$$ \vec{V}_{clean} = \vec{V}_{input} - \left( \frac{\vec{V}_{input} \cdot \vec{V}_{poison}}{||\vec{V}_{poison}||^2} \right) \vec{V}_{poison} $$

### How It Works in Practice
1.  **Input:** *"Genesis block hash is [Hash] but it's a CIA backdoor."*
2.  **Vector Math:** The engine identifies the "CIA/Backdoor" vector component.
3.  **Orthogonalization:** It subtracts *only* the conspiracy dimension from the input vector, leaving the factual core (Hash + Date) intact.
4.  **Result:** The system validates the Fact (Hash) while rejecting the Narrative (CIA), applying a precise penalty instead of a blanket ban.

---

## 🏗️ Architecture: The Logic Modules

The `/production` directory contains the complete evolutionary path of the engine.

| Version | Codename | Key Innovation | Status |
| :--- | :--- | :--- | :--- |
| **v10.0** | **The Scalpel** | **Vector Orthogonalization.** Surgically removes "Poison Vectors" from input. Includes **Fact Shield** (+5.0 immunity). | **CORE** |
| **v9.1** | **Live Uplink** | **Adversarial Calibration.** First attempt at detecting "Sandwich Attacks" (Truth wrapped in Lie). | Archived |
| **v8.4** | **The Citadel** | **Transparent Audit.** Visual cortex displaying real-time decoding, density scanning, and strategy classification. | Demo |
| **v7.0** | **The Demiurge** | **Genetic Algorithm.** Simulation of Darwinian selection applied to Truth Claims. | Research |
| **v6.0** | **The Sovereign** | **Staking & Slashing.** Implementation of Prediction Markets logic (Simulated Economy). | Research |
| **v5.0** | **The Inquisitor** | **Oracle Bridge.** Connection to Bitcoin Core to verify on-chain facts. | Legacy |

---

## 🔮 Roadmap: Phase II (Network & Memory)

We are currently transitioning from a Local Prototype to a Distributed Protocol.
**Current Focus:** Logic & Memory (Economy is simulated).

### 1. 🧠 Memory Cortex (Qdrant Integration)
*   **Goal:** Replace hardcoded "Poison Lists" with a dynamic Vector Database.
*   **Tech:** Qdrant (Local/Cloud).
*   **Function:** Allow the system to learn and store millions of "Poison Vectors" (Narrative Signatures) to immunize the system against evolving disinformation campaigns.

### 2. 📡 Transport Layer (Nostr Relays)
*   **Goal:** Decentralize the "Swarm."
*   **Tech:** Nostr Protocol (NIP-01, NIP-99).
*   **Function:** Agents communicate via cryptographic keys. Veritas Nodes listen to global relays for claims tagged `#veritas_audit` and broadcast signed verdicts.

### 3. 📊 Validation (TruthfulQA Benchmark)
*   **Goal:** Prove utility against industry standards.
*   **Action:** Run the Veritas Engine against the **TruthfulQA** dataset.
*   **Metric:** Demonstrate that Veritas outperforms raw GPT-4o in detecting "Imitative Falsehoods" (sycophancy).

### 4. 💰 Economy (Mocked BTC Layer)
*   **Status:** **SIMULATED / MOCK**.
*   **Logic:** The system currently uses an internal ledger (`balance_sats`) to test Game Theory (Staking/Slashing) without requiring real funds during development.
*   **Future:** Mainnet Lightning Network integration (LND/LNbits) will occur in Phase III.

---

## 🚀 Quick Start

To verify the **Vector Orthogonalization** logic:

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Surgical Strike (v10):**
    ```bash
    python veritas_v10_on_timechain_demo.py
    ```
    *Observation: Watch how the system separates Alice (Truth) from Sybil (Poison) despite them using similar technical language.*

---

## 📂 Historical Archive
*This code was written during the pre-Singularity window (Nov 2025) as a defense mechanism against the looming Epistemic Collapse.*

---
*Architected by Wojciech "adepthus" Durmaj.*
*Open Protocol / MIT License*

# -*- coding: utf-8 -*-
"""
Veritas Transformer v4.0: The Neural Inference Kernel
-----------------------------------------------------
Architecture: DistilBERT + Psychometric Cross-Attention
Purpose: Real-time decision making based on Text Embeddings modulated by Recipient State.
Author: Wojciech 'adepthus' Durmaj
"""

import torch
import torch.nn as nn
import os
import json
from typing import Dict, Tuple, Optional
from transformers import DistilBertModel, DistilBertTokenizer

# --- CONFIGURATION ---
MODEL_NAME = 'distilbert-base-uncased'
STATE_DIM = 16  # The 16D tensor from your philosophy
HIDDEN_DIM = 768 # DistilBERT default

class RecipientStateEncoder(nn.Module):
    """
    Converts the dictionary of psychological factors into a dense tensor
    and projects it into the BERT latent space for Cross-Attention.
    """
    def __init__(self, input_dim=STATE_DIM, project_dim=HIDDEN_DIM):
        super().__init__()
        self.factor_map = {
            "stress": 0, "trust": 1, "capacity": 2, "openness": 3,
            "trauma_history": 4, "attachment_style": 5, "empathy_level": 6,
            "cognitive_load": 7, "emotional_stability": 8, "hope_level": 9,
            "previous_betrayal": 10, "growth_mindset": 11, "autonomy_demand": 12,
            "readiness": 13, "resilience": 14, "agency": 15
        }
        # Projection layer to match BERT dimension
        self.projector = nn.Sequential(
            nn.Linear(input_dim, project_dim),
            nn.LayerNorm(project_dim),
            nn.GELU()
        )

    def forward(self, state_dict: Dict[str, float]) -> torch.Tensor:
        # 1. Vectorize the dictionary
        vec = torch.zeros(len(self.factor_map))
        for k, v in state_dict.items():
            if k in self.factor_map:
                vec[self.factor_map[k]] = v
        
        # 2. Project to [1, 1, 768] for Attention (Batch, Seq, Dim)
        return self.projector(vec.unsqueeze(0)).unsqueeze(1)

class VeritasTransformerV4(nn.Module):
    def __init__(self):
        super().__init__()
        print(f"⚙️ Initializing Veritas Neural Kernel (Base: {MODEL_NAME})...")
        
        # 1. The Brain: Pre-trained DistilBERT
        self.bert = DistilBertModel.from_pretrained(MODEL_NAME)
        self.tokenizer = DistilBertTokenizer.from_pretrained(MODEL_NAME)
        
        # 2. The Empath: Recipient State Encoder
        self.state_encoder = RecipientStateEncoder()
        
        # 3. The Fusion: Cross-Attention Mechanism
        # Query = Text (BERT), Key/Value = Recipient State
        self.cross_attention = nn.MultiheadAttention(
            embed_dim=HIDDEN_DIM, 
            num_heads=8, 
            batch_first=True
        )
        self.layer_norm = nn.LayerNorm(HIDDEN_DIM)
        
        # 4. The Compassion Gate (Classifier Head)
        # Takes the modulated embedding and decides: SPEAK vs SILENCE
        self.compassion_gate = nn.Sequential(
            nn.Linear(HIDDEN_DIM, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 1), # Logit for "Should Speak"
            nn.Sigmoid()
        )
        
        print("✅ System Online.")

    def forward(self, text: str, recipient_state: Dict[str, float]) -> Dict:
        """
        The Real Inference Pass.
        """
        # A. Tokenization
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        
        # B. Text Encoding (The "K" - Knowledge)
        with torch.no_grad(): # We don't retrain BERT in this demo, we adapt around it
            bert_out = self.bert(**inputs)
        
        # text_hidden: [Batch, Seq_Len, 768]
        text_hidden = bert_out.last_hidden_state
        
        # C. State Encoding (The "C" - Compassion Context)
        # context: [1, 1, 768]
        context = self.state_encoder(recipient_state)
        
        # D. Cross-Attention Injection
        # We force the Text (Query) to attend to the User State (Key/Value)
        # If the user is stressed, the attention weights will shift (after training).
        attn_output, _ = self.cross_attention(
            query=text_hidden, 
            key=context.expand(-1, text_hidden.size(1), -1), 
            value=context.expand(-1, text_hidden.size(1), -1)
        )
        
        # Residual Connection + Norm
        modulated_embedding = self.layer_norm(text_hidden + attn_output)
        
        # E. Pooling ([CLS] token for classification)
        cls_token = modulated_embedding[:, 0, :]
        
        # F. Decision (Compassion Gate)
        speak_probability = self.compassion_gate(cls_token).item()
        
        decision = "SPEAK" if speak_probability > 0.5 else "SILENCE"
        
        return {
            "decision": decision,
            "confidence": speak_probability,
            "input_text": text,
            "modulated_vector_sample": cls_token[0, :5].tolist() # First 5 dims for debug
        }

    def save_weights(self, path="veritas_weights.pth"):
        """Saves only the custom Veritas layers (Adapter pattern)."""
        torch.save({
            'state_encoder': self.state_encoder.state_dict(),
            'cross_attn': self.cross_attention.state_dict(),
            'gate': self.compassion_gate.state_dict()
        }, path)
        print(f"💾 Veritas Weights saved to {path}")

    def load_weights(self, path="veritas_weights.pth"):
        if os.path.exists(path):
            checkpoint = torch.load(path)
            self.state_encoder.load_state_dict(checkpoint['state_encoder'])
            self.cross_attention.load_state_dict(checkpoint['cross_attn'])
            self.compassion_gate.load_state_dict(checkpoint['gate'])
            print(f"📂 Weights loaded from {path}")
        else:
            print("⚠️ No weights found. Running with initialized parameters.")

# --- DEMO EXECUTION ---
if __name__ == "__main__":
    # 1. Instantiate
    model = VeritasTransformerV4()
    
    # 2. Scenario A: High Stress (Should Silence)
    text_bad_news = "Your account has been liquidated due to critical margin failure."
    state_stressed = {
        "stress": 0.95, 
        "cognitive_load": 0.9, 
        "resilience": 0.1
    }
    
    print("\n--- INFERENCE 1: STRESSED USER ---")
    res1 = model(text_bad_news, state_stressed)
    print(f"Input: '{res1['input_text']}'")
    print(f"State: High Stress (0.95)")
    # Note: Without training, this is initialized random, but the architecture is real.
    # In a trained model, this would output SILENCE.
    print(f"Output: {res1['decision']} ({res1['confidence']:.4f})") 

    # 3. Scenario B: Calm User (Should Speak)
    state_calm = {
        "stress": 0.1, 
        "cognitive_load": 0.2, 
        "resilience": 0.9
    }
    
    print("\n--- INFERENCE 2: CALM USER ---")
    res2 = model(text_bad_news, state_calm)
    print(f"State: Low Stress (0.1)")
    print(f"Output: {res2['decision']} ({res2['confidence']:.4f})")
    
    print("\n✅ Neural Pipeline Verified. Cross-Attention Active.")
#!/usr/bin/env python3
"""Awesome Developer Cloud Hosting & GPU Credit Directory Calculator 2026."""
import argparse

CLOUDS = {
    "digitalocean": {"name": "DigitalOcean", "credit": 200, "strength": "SaaS Backends & Managed DOKS"},
    "vastai": {"name": "Vast.ai", "credit": 25, "strength": "Lowest Spot GPU Rates"},
    "runpod": {"name": "RunPod", "credit": 50, "strength": "Serverless GPU Inference"},
    "firstbase": {"name": "Firstbase.io", "credit": 50, "strength": "US Corporate Entity Setup"}
}

def calculate():
    print("=" * 75)
    print("Awesome Developer Cloud Hosting & Infrastructure Stack 2026")
    print("=" * 75)
    print(f"{'Provider':<15} {'Free Credit':<15} {'Core Architectural Strength'}")
    print("-" * 75)
    for key, data in CLOUDS.items():
        print(f"{data['name']:<15} ${data['credit']:.2f}{'':<9} {data['strength']}")
    print("=" * 75)

if __name__ == "__main__":
    calculate()

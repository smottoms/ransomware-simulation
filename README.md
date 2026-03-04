# Safe Ransomware Simulation (Educational)

This project demonstrates how ransomware encrypts files and how they can be decrypted.

⚠️ This project is strictly for **educational and cybersecurity research purposes only**.

## Features

- Encrypts sample files
- Creates a ransom note
- Decrypt script to restore files
- Demonstrates ransomware workflow
- Docker container for safe execution

## How Ransomware Works (Simulation)

1. Generate encryption key
2. Locate files
3. Encrypt files
4. Drop ransom note
5. Provide decryptor

## Run with Docker

Build:

docker build -t ransomware-demo .

Run:

docker run ransomware-demo

## Manual Run

Install requirements

pip install -r requirements.txt

Run simulator

python ransomware_sim.py

Decrypt files

python decryptor.py

## 🎥 Demo Video

[![Watch the Demo](https://img.youtube.com/vi/-qeZcO8CPjM/maxresdefault.jpg)](https://youtu.be/-qeZcO8CPjM?si=svn81HW5B2uyqVPE)
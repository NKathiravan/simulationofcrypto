# Decentralized Cryptocurrency & Wallet System

This project implements a basic **decentralized cryptocurrency** system using a **Proof-of-Work (PoW)** blockchain. It includes a **cryptocurrency wallet** with a user-friendly graphical interface for account creation, secure transactions, and balance checks. The system uses local JSON files to simulate a distributed ledger environment.

---

## 🧱 Architecture Overview

### ⚖️ Decentralization vs Centralization
This system is designed with a **decentralized** architecture to eliminate the need for centralized authorities like banks. All transaction and balance verifications are handled by the network using a PoW consensus mechanism.

### 🔐 Proof-of-Work (PoW) Consensus
The project currently uses **Proof-of-Work** for securing the network. Though computationally intensive, PoW ensures strong security from the initial stages. A future upgrade to **Proof-of-Stake (PoS)** can be considered as user participation grows.

---

## 📦 Components

### 🧩 Blockchain
- Manages transaction data across interconnected blocks.
- Stores blockchain data in `blockchain_data.json`.
- New blocks are created and appended when transactions occur.

### 👤 Blockchain Account
- Each user is represented by a unique key pair (public/private).
- Account balances are tracked in `accounts.json`.

### 💼 Cryptocurrency Wallet
- GUI for interacting with the blockchain.
- Allows users to:
  - Create secure accounts.
  - Send and receive cryptocurrency.
  - Check balances.

### 🖥️ Server
- Listens for wallet connections.
- Maintains consistency between local and server blockchain states.

---



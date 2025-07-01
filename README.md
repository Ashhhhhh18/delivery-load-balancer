# Advanced Azure-style Storage Load Balancer Simulator

This project is inspired by how **Microsoft Azure Storage** handles massive data loads. It simulates how storage accounts (like users uploading files or using cloud apps) can be smartly distributed across multiple backend servers (called nodes) to avoid overload.

Think of it like a traffic police for data — it watches all incoming traffic (requests) and tells them exactly which lane (node) to go to so nothing gets blocked.

Built using **Python**, **Flask**, and **Matplotlib**, this app mimics basic resource management and load balancing you'd find in cloud systems.

---

## 🚀 What This Project Can Do

- Accepts fake "load" requests (like someone uploading data)
- Smartly distributes those requests across multiple virtual servers
- Makes sure no server is overloaded (by checking CPU, memory, IOPS)
- Shows how much load each server is handling — using a **pie chart**
- All of this is done via a simple **web API** (Flask backend)

---

## ⚙️ How to Run It on Your Machine

**Step 1: Install required Python libraries**
```bash
pip install -r requirements.txt

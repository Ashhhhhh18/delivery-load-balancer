# 🚀 Azure Storage Load Balancer (Advanced)

This project simulates how Azure might handle load balancing across storage accounts.
It distributes CPU, Memory, and IOPS usage across nodes to keep things stable.

## 🔧 Features
- Assigns multiple storage accounts to nodes intelligently
- Balances load using a simulation algorithm
- Prevents overloading by shifting accounts between nodes
- Displays a chart showing resource distribution
- Web app with `/simulate` endpoint

## 🖥️ Technologies Used
- Python 3
- Flask (Web API)
- Matplotlib (Chart Visualization)

## ▶️ How to Run

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Start the app**:
    ```bash
    python main.py
    ```

3. **Open your browser** and visit:
    [http://127.0.0.1:5000/simulate](http://127.0.0.1:5000/simulate)

## 📁 Folder Structure
```
📦 delivery-load-balancer-advanced
┣ 📄 main.py
┣ 📄 requirements.txt
┣ 📄 README.md (This file)
```

## 📌 Note
This is a simulation—not connected to Azure directly. But it reflects a realistic design idea for handling Azure-like workloads.

---
💡 Built by Ashok P | GitHub: [Ashhhhhh18](https://github.com/Ashhhhhh18)

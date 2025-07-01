# Azure Storage Load Balancer (Advanced)

This project simulates Azure-style load balancing using Python + Flask + Matplotlib.

## Features
- Load accounts (with CPU, memory, IOPS) into nodes
- Prevent overload and balance resources
- Visual chart of resource usage
- Web API with `/simulate` endpoint

## Run Instructions
1. Install dependencies:
   pip install -r requirements.txt
2. Start the app:
   python main.py
3. Open browser:
   http://127.0.0.1:5000/simulate

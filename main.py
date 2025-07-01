
import json
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load data
def load_data():
    with open("nodes.json") as f:
        nodes = json.load(f)
    with open("accounts.json") as f:
        accounts = json.load(f)
    return nodes, accounts

# Assign accounts to nodes
def assign_accounts(nodes, accounts):
    node_usage = {n['id']: {"cpu": 0, "memory": 0, "iops": 0, "accounts": []} for n in nodes}
    for acc in accounts:
        best_node = None
        min_load = float('inf')
        for node in nodes:
            nid = node['id']
            load = node_usage[nid]
            if (load['cpu'] + acc['cpu'] <= 100 and
                load['memory'] + acc['memory'] <= 100 and
                load['iops'] + acc['iops'] <= 100):
                total = load['cpu'] + load['memory'] + load['iops']
                if total < min_load:
                    min_load = total
                    best_node = nid
        if best_node:
            usage = node_usage[best_node]
            usage['cpu'] += acc['cpu']
            usage['memory'] += acc['memory']
            usage['iops'] += acc['iops']
            usage['accounts'].append(acc['id'])
    return node_usage

# Plot usage chart
def plot_usage(node_usage):
    ids = list(node_usage.keys())
    cpu = [node_usage[i]['cpu'] for i in ids]
    memory = [node_usage[i]['memory'] for i in ids]
    iops = [node_usage[i]['iops'] for i in ids]

    x = range(len(ids))
    plt.figure(figsize=(10, 6))
    plt.bar(x, cpu, width=0.2, label='CPU')
    plt.bar([i + 0.2 for i in x], memory, width=0.2, label='Memory')
    plt.bar([i + 0.4 for i in x], iops, width=0.2, label='IOPS')
    plt.xticks([i + 0.2 for i in x], ids)
    plt.ylabel("Usage (%)")
    plt.title("Node Resource Usage")
    plt.legend()
    plt.tight_layout()
    plt.savefig("node_usage_chart.png")
    plt.close()

@app.route("/simulate", methods=["GET"])
def simulate():
    nodes, accounts = load_data()
    usage = assign_accounts(nodes, accounts)
    plot_usage(usage)
    return jsonify(usage)

if __name__ == "__main__":
    app.run(debug=True)

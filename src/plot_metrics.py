import json
import matplotlib.pyplot as plt

def plot_metrics():
    with open("metrics.json") as f:
        data = json.load(f)

    acc = data["accuracy"]
    epochs = list(range(1, len(acc) + 1))

    plt.figure(figsize=(6, 4))
    plt.plot(epochs, acc, marker='o', label="Accuracy")
    plt.title("Model Accuracy over Epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("metrics.png")

if __name__ == "__main__":
    plot_metrics()
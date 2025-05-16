import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.stats import pearsonr

# --------- Dossiers I/O ------------
INPUT_DIR  = "benchmark_output"
OUTPUT_DIR = "benchmark_charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)  # crée le dossier si absent

# --------- Config globale ----------
model_files = {
    "gpt-4o":  "benchmark-gpt-4o.txt",
    "gpt-4.1": "benchmark-gpt-4.1.txt",
    "o4-mini": "benchmark-o4-mini.txt",
    "o1":      "benchmark-o1.txt"
}

colors = {
    "gpt-4o":  "tab:blue",
    "gpt-4.1": "tab:green",
    "o4-mini": "tab:orange",
    "o1":      "tab:red"
}

metric_labels = {
    "Obf(s)":    "Obfuscation time",
    "Deobf(s)":  "Deobfuscation time",
    "Orig(s)":   "Base code",
    "ObfRun(s)": "Obfuscated code",
    "DeRun(s)":  "Deobfuscated code"
}

metrics_obf  = ["Obf(s)", "Deobf(s)"]
metrics_exec = ["Orig(s)", "ObfRun(s)", "DeRun(s)"]
labels_obf   = [metric_labels[m] for m in metrics_obf]
labels_exec  = [metric_labels[m] for m in metrics_exec]

# --------- Parsing helper ----------
def parse_benchmark_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith("Case"):
            start = i + 2
            break
    data = []
    for line in lines[start:]:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) != 6:
            continue
        case, obf, deobf, orig, obfrun, derun = parts
        data.append({
            "Case":     case,
            "Obf(s)":   float(obf),
            "Deobf(s)": float(deobf),
            "Orig(s)":  float(orig),
            "ObfRun(s)": float(obfrun),
            "DeRun(s)":  float(derun),
        })
    return pd.DataFrame(data).set_index("Case")

# --------- Chargement auto ----------
dfs = {}
for model, fname in model_files.items():
    full_path = os.path.join(INPUT_DIR, fname)
    if os.path.exists(full_path):
        dfs[model] = parse_benchmark_file(full_path)
    else:
        print(f"(!) File not found: {full_path} -- skipping model {model}")

if not dfs:
    raise FileNotFoundError("No benchmark files found in benchmark_output!")

all_cases       = list(next(iter(dfs.values())).index)
models_included = list(dfs.keys())

# --------- GRAPHIQUES PAR CAS ----------
for case in all_cases:
    # --- 1. Obfuscation / Deobfuscation ---
    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.arange(len(metrics_obf))
    bar_width = 0.15 if len(models_included) > 2 else 0.35
    for i, model in enumerate(models_included):
        vals = [dfs[model].loc[case, m] for m in metrics_obf]
        bars = ax.bar(x + i*bar_width, vals, bar_width, label=model,
                      color=colors.get(model, None))
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}',
                    va='bottom', ha='center', fontsize=9)
    ax.set_xticks(x + (len(models_included)-1)*bar_width/2)
    ax.set_xticklabels(labels_obf)
    ax.set_ylabel("Time (s)")
    ax.set_title(f'{case}: Obfuscation vs Deobfuscation')
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"graphical-{case.lower()}-obfuscation.png"))
    plt.close(fig)

    # --- 2. Execution Performance ---
    fig, ax = plt.subplots(figsize=(8, 4))
    x2 = np.arange(len(metrics_exec))
    for i, model in enumerate(models_included):
        vals = [dfs[model].loc[case, m] for m in metrics_exec]
        bars = ax.bar(x2 + i*bar_width, vals, bar_width, label=model,
                      color=colors.get(model, None))
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}',
                    va='bottom', ha='center', fontsize=9)
    ax.set_xticks(x2 + (len(models_included)-1)*bar_width/2)
    ax.set_xticklabels(labels_exec)
    ax.set_ylabel("Time (s)")
    ax.set_title(f'{case}: Execution Performance')
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"graphical-{case.lower()}-execution.png"))
    plt.close(fig)

# --------- GRAPHIQUE GLOBAL : Déobfuscation ---------
fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(all_cases))
bar_width = 0.15 if len(models_included) > 2 else 0.3

for i, model in enumerate(models_included):
    deobf_times = [dfs[model].loc[case, "Deobf(s)"] for case in all_cases]
    bars = ax.bar(x + i*bar_width, deobf_times, bar_width, label=model,
                  color=colors.get(model, None))
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}',
                va='bottom', ha='center', fontsize=9)

ax.set_xticks(x + (len(models_included)-1)*bar_width/2)
ax.set_xticklabels(all_cases)
ax.set_ylabel("Deobfuscation time (s)")
ax.set_title("Deobfuscation Time Comparison by Model and Test")
ax.legend(title="Model")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "graphical-global-deobfuscation.png"))
plt.close(fig)

# --------- GRAPHIQUE GLOBAL : Obfuscation ---------
fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(all_cases))

for i, model in enumerate(models_included):
    obf_times = [dfs[model].loc[case, "Obf(s)"] for case in all_cases]
    bars = ax.bar(x + i*bar_width, obf_times, bar_width, label=model,
                  color=colors.get(model, None))
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}',
                va='bottom', ha='center', fontsize=9)

ax.set_xticks(x + (len(models_included)-1)*bar_width/2)
ax.set_xticklabels(all_cases)
ax.set_ylabel("Obfuscation time (s)")
ax.set_title("Obfuscation Time Comparison by Model and Test")
ax.legend(title="Model")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "graphical-global-obfuscation.png"))
plt.close(fig)

# --------- NOUVEAUX GRAPHIQUES GLOBALS : Exécution ---------
global_exec_metrics = [
    ("Orig(s)",   "Base Code",        "global-base-code"),
    ("ObfRun(s)", "Obfuscated Code",  "global-obfuscated-code"),
    ("DeRun(s)",  "Deobfuscated Code","global-deobfuscated-code")
]

for metric, pretty, fname_suffix in global_exec_metrics:
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(all_cases))
    for i, model in enumerate(models_included):
        times = [dfs[model].loc[case, metric] for case in all_cases]
        bars = ax.bar(x + i*bar_width, times, bar_width, label=model,
                      color=colors.get(model, None))
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}',
                    va='bottom', ha='center', fontsize=9)
    ax.set_xticks(x + (len(models_included)-1)*bar_width/2)
    ax.set_xticklabels(all_cases)
    ax.set_ylabel(f"{pretty} time (s)")
    ax.set_title(f"{pretty} Time Comparison by Model and Test")
    ax.legend(title="Model")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"graphical-{fname_suffix}.png"))
    plt.close(fig)

# =========== STATISTICAL ANALYSIS ===========
print("\n---- Statistical Summary by Model ----")
for model, df in dfs.items():
    print(f"\nModel: {model}")
    print(df.describe().round(3))

print("\n---- Correlation Tests (Pearson r, p-value) ----")
for model, df in dfs.items():
    print(f"\nModel: {model}")
    corr, pval = pearsonr(df["Obf(s)"], df["Deobf(s)"])
    print(f"Obf(s) <-> Deobf(s): r={corr:.2f} (p={pval:.3f})")
    corr, pval = pearsonr(df["Orig(s)"], df["DeRun(s)"])
    print(f"Orig(s) <-> DeRun(s): r={corr:.2f} (p={pval:.3f})")

# --------- Mean Barplot (all metrics) ---------
means = {model: df.mean() for model, df in dfs.items()}
mean_df = pd.DataFrame(means).T

mean_df[["Obf(s)", "Deobf(s)", "Orig(s)", "ObfRun(s)", "DeRun(s)"]].plot.bar(figsize=(10, 5))
plt.ylabel("Mean Time (s)")
plt.title("Average Time by Model and Metric")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "graphical-average-times.png"))
plt.close()

# --------- Rankings (mean by metric) ---------
for metric in ["Obf(s)", "Deobf(s)", "Orig(s)", "ObfRun(s)", "DeRun(s)"]:
    ranking = mean_df[metric].sort_values()
    print(f"\n{metric} ranking (best to worst):")
    print(ranking)

# --------- Bootstrap CI (95%) ---------
def bootstrap_ci(data, n_bootstrap=1000, alpha=0.05):
    if len(data) < 2:
        return np.nan, np.nan
    boot_means = [np.mean(np.random.choice(data, size=len(data), replace=True))
                  for _ in range(n_bootstrap)]
    lower = np.percentile(boot_means, 100*alpha/2)
    upper = np.percentile(boot_means, 100*(1-alpha/2))
    return lower, upper

print("\n---- 95% Bootstrap Confidence Interval for Mean (per model/metric) ----")
for model, df in dfs.items():
    print(f"\nModel: {model}")
    for metric in ["Obf(s)", "Deobf(s)", "Orig(s)", "ObfRun(s)", "DeRun(s)"]:
        vals = df[metric].values
        ci_low, ci_high = bootstrap_ci(vals)
        print(f"  {metric}: Mean={vals.mean():.2f}, 95% CI = [{ci_low:.2f}, {ci_high:.2f}]")

print("\n✅ Tous les graphiques (y compris Base, Obfuscated et Deobfuscated code) sont dans le dossier benchmark_charts/ !")

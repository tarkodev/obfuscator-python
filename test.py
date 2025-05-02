import subprocess
import sys
import argparse
import os
import time

def run_script(path):
    """
    Exécute un script Python, mesure le temps d'exécution
    et retourne (stdout, stderr, returncode, duration).
    """
    start = time.perf_counter()
    result = subprocess.run(
        [sys.executable, path],
        capture_output=True,
        text=True
    )
    duration = time.perf_counter() - start
    return result.stdout, result.stderr, result.returncode, duration


def process_base(base):
    # Prépare les chemins
    input_file = os.path.normpath(f".\\example\\{base}_input.py")
    obf_file = os.path.normpath(f".\\example\\{base}_obfuscated.py")
    deobf_file = os.path.normpath(f".\\example\\{base}_deobfuscated_gpt-4o.py")

    # Étape 1 : obfuscation
    print(f"[1/3 - {base}] Obfuscation : {input_file} -> {obf_file}")
    obf_cmd = [
        sys.executable, "-m", "obfuscator.main",
        "--input", input_file,
        "--output", obf_file,
        "--transformations",
        "remove_all_comments", "rename_identifiers",
        "add_dead_code", "restructure_loops",
        "obfuscate_strings"
    ]
    t0 = time.perf_counter()
    res = subprocess.run(obf_cmd, capture_output=True, text=True)
    tob = time.perf_counter() - t0
    if res.returncode != 0:
        print(f"Erreur pendant l'obfuscation de {base} :", res.stderr)
        return
    print(f"    Durée obfuscation : {tob:.3f} s")

    # Étape 2 : déobfuscation via GPT sur le fichier obfusqué
    print(f"[2/3 - {base}] Déobfuscation GPT : {obf_file} -> {deobf_file}")
    deobf_cmd = [
        sys.executable, "-m", "obfuscator.main",
        "--input", obf_file,
        "--output", deobf_file,
        "--gpt"
    ]
    t1 = time.perf_counter()
    res2 = subprocess.run(deobf_cmd, capture_output=True, text=True)
    tde = time.perf_counter() - t1
    if res2.returncode != 0:
        print(f"Erreur pendant la déobfuscation de {base} :", res2.stderr)
        return
    print(f"    Durée déobfuscation : {tde:.3f} s")

    # Étape 3 : exécution et comparaison
    print(f"[3/3 - {base}] Exécution et comparaison des résultats :")
    input_out, input_err, input_code, tin = run_script(input_file)
    obf_out, obf_err, obf_code, tob_ex = run_script(obf_file)
    deobf_out, deobf_err, deobf_code, tde_ex = run_script(deobf_file)

    def compare(name, out, err, code, duration):
        same_out = (out == input_out)
        same_code = (code == input_code)
        print(f"\n-- {name} --")
        print(f"Exit code : {code} ({'OK' if same_code else 'DIFFÉRENT'})")
        print(f"Sortie stdout : {'OK' if same_out else 'DIFFÉRENTE'}")
        print(f"Temps d'exécution : {duration:.3f} s")
        if not same_out:
            print(f"--- Contenu stdout de {name} :\n{out}")
        if code != input_code or err:
            print(f"--- stderr de {name} :\n{err}")

    compare("Original", input_out, input_err, input_code, tin)
    compare("Obfusqué", obf_out, obf_err, obf_code, tob_ex)
    compare("Déobfusqué GPT", deobf_out, deobf_err, deobf_code, tde_ex)


def main():
    parser = argparse.ArgumentParser(
        description="Obfuscation, déobfuscation et comparaison des résultats pour plusieurs cas"
    )
    parser.add_argument(
        "bases",
        nargs="*",
        default=["palindrom", "prime", "fibonacci"],
        help="Liste des noms de base des fichiers (par ex. palindrom prime fibonacci)"
    )
    args = parser.parse_args()

    for base in args.bases:
        process_base(base)

if __name__ == "__main__":
    main()

## enter loads here
from Cantilever_calculator import tributary_width_ft

L = float(input("Enter live load (psf): "))
D = float(input("Enter dead load (psf): "))
S = float(input("Enter snow load (psf): "))
Lr = float(input("Enter roof live load (psf): "))
R = float(input("Enter rain load (psf): "))
W = float(input("Enter wind load (psf): "))
Wt = float(input("Enter tornado load (psf): "))

# -----------------------------
# Strength load combinations
# ASCE-style combos from provided list
# Units: psf
# -----------------------------

load_combinations = {
    # 1a
    "1a: 1.4D": 1.4 * D,

    # 2a
    "2a-1: 1.2D + 1.6L + 0.5Lr": 1.2 * D + 1.6 * L + 0.5 * Lr,
    "2a-2: 1.2D + 1.6L + 0.3S": 1.2 * D + 1.6 * L + 0.3 * S,
    "2a-3: 1.2D + 1.6L + 0.5R": 1.2 * D + 1.6 * L + 0.5 * R,

    # 3a
    "3a-1: 1.2D + 1.6Lr + L": 1.2 * D + 1.6 * Lr + L,
    "3a-2: 1.2D + 1.6Lr + 0.5W": 1.2 * D + 1.6 * Lr + 0.5 * W,

    "3a-3: 1.2D + 1.0S + L": 1.2 * D + 1.0 * S + L,
    "3a-4: 1.2D + 1.0S + 0.5W": 1.2 * D + 1.0 * S + 0.5 * W,

    "3a-5: 1.2D + 1.6R + L": 1.2 * D + 1.6 * R + L,
    "3a-6: 1.2D + 1.6R + 0.5W": 1.2 * D + 1.6 * R + 0.5 * W,

    # 4a
    "4a-1: 1.2D + 1.0W + L + 0.5Lr": 1.2 * D + 1.0 * W + L + 0.5 * Lr,
    "4a-2: 1.2D + 1.0W + L + 0.3S": 1.2 * D + 1.0 * W + L + 0.3 * S,
    "4a-3: 1.2D + 1.0W + L + 0.5R": 1.2 * D + 1.0 * W + L + 0.5 * R,

    "4a-4: 1.2D + 1.0WT + L + 0.5Lr": 1.2 * D + 1.0 * Wt + L + 0.5 * Lr,
    "4a-5: 1.2D + 1.0WT + L + 0.3S": 1.2 * D + 1.0 * Wt + L + 0.3 * S,
    "4a-6: 1.2D + 1.0WT + L + 0.5R": 1.2 * D + 1.0 * Wt + L + 0.5 * R,

    # 5a
    "5a-1: 0.9D + 1.0W": 0.9 * D + 1.0 * W,
    "5a-2: 0.9D + 1.0WT": 0.9 * D + 1.0 * Wt,
}

#calculate governing code
governing_combo_name = max(load_combinations, key=load_combinations.get)
governing_factored_psf = load_combinations[governing_combo_name]

#calculate service load
service_psf = D + L
live_load_psf = L

# user inputs tributary area and span
trib_width_ft = float(input("Enter tributary width (ft): "))
span_ft = float(input("Enter span (ft): "))
span_in=span_ft*12

# calculate line load
governing_factored_plf = governing_factored_psf * trib_width_ft
service_plf = service_psf * trib_width_ft
live_load_plf = live_load_psf * trib_width_ft

# print summary
print(f"""
----- Load Combo Summary -----

Tributary width = {tributary_width_ft:.2f} ft

Governing strength combo:
{governing_combo_name}

Governing factored area load = {governing_factored_psf:.2f} psf
Governing factored beam load = {governing_factored_plf:.2f} plf

Service area load, D + L = {service_psf:.2f} psf
Service beam load = {service_plf:.2f} plf

Live load area load = {live_load_psf:.2f} psf
Live load beam load = {live_load_plf:.2f} plf
""")


# simple beam calculator

# -----------------------------
# Load inputs
# -----------------------------
live_load_psf = float(input("Enter live load (psf): "))
dead_load_psf = float(input("Enter dead load (psf): "))

# Combine dead and live load per ASCE 7
service_load_psf = live_load_psf + dead_load_psf
factored_load_psf = 1.2 * dead_load_psf + 1.6 * live_load_psf

# Span and tributary width
span_ft = float(input("Enter span (ft): "))
span_in = span_ft * 12

tributary_width_ft = float(input("Enter tributary width (ft): "))

# -----------------------------
# Line loads
# -----------------------------
line_load_plf = tributary_width_ft * factored_load_psf
line_load_service_plf = tributary_width_ft * service_load_psf
line_load_LL_only_plf = tributary_width_ft * live_load_psf

# -----------------------------
# Line loads, converted to pli
# -----------------------------
line_load_pli = line_load_plf / 12
line_load_service_pli = line_load_service_plf / 12
line_load_LL_only_pli = line_load_LL_only_plf / 12

# -----------------------------
# Strength design (factored)
# -----------------------------
reaction_lbs = line_load_plf * span_ft / 2
moment_lbft = line_load_plf * span_ft**2 / 8

# ----------------------------
# material dictionary, built out more later
# ---------------------------
materials = { # check all these values later
    "Steel": {
        "E": 29000000,   # psi (same for all structural steel)
        "categories": {
            "Wide Flange": {
                "Fy": 50000,   # A992 typical
                "shapes": {
                    "W8x10": {"Ix": 18.2, "Sx": 4.55},
                    "W10x12": {"Ix": 28.5, "Sx": 5.70}
                }
            },
            "HSS": {
                "Fy": 46000,   # typical HSS Fy
                "shapes": {
                    "HSS6x6x3/8": {"Ix": 36.5, "Sx": 12.2}
                }
            },
            "Channel": {
                "Fy": 36000,   # many channels are A36
                "shapes": {
                    "C8x11.5": {"Ix": 23.2, "Sx": 5.8}
                }
            },
            "Angle": {
                "Fy": 36000,
                "shapes": {
                    "L4x4x1/2": {"Ix": 5.12, "Sx": 2.56}
                }
            }
        }
    },

    "Wood": {
        "categories": {
            "Sawn Lumber": {
                "E": 1600000,   # psi (Douglas Fir-Larch No.2)
                "shapes": {
                    "2x10": {"Ix": 21.39, "Sx": 4.28},
                    "2x12": {"Ix": 31.64, "Sx": 5.27}
                }
            },
            "LVL": {
                "E": 1900000,   # psi (typical 1.9E LVL)
                "shapes": {
                    "1.75x11.875": {"Ix": 100.2, "Sx": 16.9}
                }
            },
            "Glulam": {
                "E": 1800000,   # psi (typical 24F-V4)
                "shapes": {
                    "3.125x12": {"Ix": 140.0, "Sx": 23.3}
                }
            },
            "Heavy Timber": {
                "E": 1400000,   # psi (typical)
                "shapes": {
                    "6x10": {"Ix": 187.5, "Sx": 37.5}
                }
            }
        }
    }
}


# -----------------------------
# Deflection (service load only)
# EI will be added later
# -----------------------------
standard_deflection_in = (5 * line_load_service_pli * span_in**4) / 384
LL_deflection_in = (5 * line_load_LL_only_pli * span_in**4) / 384

# Deflection limits (floor beam assumptions)
live_load_limit_in = span_in / 240
standard_deflection_limit_in = span_in / 360

LL_deflection_status = "PASS" if LL_deflection_in < live_load_limit_in else "FAIL"
standard_deflection_status = "PASS" if standard_deflection_in < standard_deflection_limit_in else "FAIL"

# -----------------------------
# Summary
# -----------------------------
print(f"""
----- Summary -----
Service area load = {service_load_psf} psf
Factored area load = {factored_load_psf} psf

Span = {span_ft} ft
Tributary Width = {tributary_width_ft} ft

Factored Beam Load = {line_load_plf} plf
Support Reaction = {reaction_lbs} lbs
Max Shear = {reaction_lbs} lbs
Max Moment = {moment_lbft} lb-ft

Max Deflection (service) = {standard_deflection_in} in
Standard Deflection Status = {standard_deflection_status}
Live Load Deflection Status = {LL_deflection_status}
""")

#tributary area calculator
# take deadload and live load
live_load = float(input("enter live load (psf): "))
dead_load = float(input("enter deadload (psf): "))
#combine dead and live load per ASCE 7
service_load = live_load + dead_load
factored_load = 1.2 * dead_load + 1.6 * live_load
#ask user service or strength
design_type = input("Service or strength? ").lower()
if design_type == "service": load_psf = service_load
elif design_type == "strength": load_psf = factored_load
else: print("invalid choice")
# ask user tributary and dimensions, later we will use span for beam calculations.
# I am thinking we will build databse with info on materials, support condition etc.
span = float(input("enter span (ft): ")) # for now we will not use span
tributary_width = float(input("enter tributary width (ft): "))
# calculate line load
line_load = tributary_width * load_psf
#print summary
print(f"""----- Summary -----
Design condition = {design_type}
Area Load = {load_psf} psf
Span = {span} ft
Beam Load = {line_load} plf""")


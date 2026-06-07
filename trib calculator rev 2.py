#tributary area calculator
# take deadload and live load
live_load = float(input("enter live load (psf): "))
dead_load = float(input("enter deadload (psf): "))
#combine dead and live load per ASCE 7
service_load = live_load + dead_load
factored_load = 1.2 * dead_load + 1.6 * live_load
# ask user tributary and dimensions, later we will use span for beam calculations.
# I am thinking we will build databse with info on materials, support condition etc.
span = float(input("enter span (ft): "))
# convert span to inches
span_in = span * 12
tributary_width = float(input("enter tributary width (ft): "))
# calculate line load
line_load = tributary_width * factored_load
#calculate reaction, for now assume simply supported
reaction = line_load * span/2
# max moment
moment = (line_load * span**2)/8
# add deflection here, EI will be added when i upddate to add section and material properties
standard_deflection = 5* line_load * span_in**4/384
LL_deflection = (live_load * span_in**4)/384
#deflection limits
live_load_limit = span_in/240
standard_deflection_limit = span_in/360
#check deflection, currently this isnt accurate. Will be when section properties added
if LL_deflection < live_load_limit:
    LL_deflectiion_status = "PASS"
else: LL_deflectiion_status = "FAIL"
if standard_deflection < standard_deflection_limit:
    standard_deflection_status = "PASS"
else:
    standard_deflection_status = "FAIL"
#print summary
print(f"""----- Summary -----
Factored area load = {service_load} psf
Span = {span} ft
Factored Beam load = {line_load} plf
Support Reaction = {reaction} lbs.
Max Shear = {reaction} lbs.
Max Moment = {moment} lbs.-ft
Max deflection = {standard_deflection} in.
Standard deflection status = {standard_deflection_status} 
Live load deflection status = {LL_deflectiion_status} """)


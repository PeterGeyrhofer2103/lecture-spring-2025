# Open Source Energy System Modeling - Lecture Spring 2025

Copyright 2025 Peter Geyrhofer

This project is released under an MIT LICENSE.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a code used to calculate levelized costs of electricity for any given energy system powered by wind. Furthermore the annual output of wind energy can be predicted seperately.

Following two functions are included:

### predict_q: 
Scope: The function is used to predict the annual output of wind energy for a wind turbine in MWh, which is needed to calculate the LCOE.

Usage: python predict_q <capacity> (Power in MW) <capacity_factor> (efficiency 0 to 1) <hours_per_year> (default: 8760h)

Output: wind energy in MWh/year

### calculate_lcoe:
Scope: This function is used to calculate the levelized costs of elecricity for wind energy. This function embedds predict_q

Usage: python calculate_lcoe <WACC> (decimal form) <lifetime> (in years) <CAPEX> (in €) <OPEX_fix> (in €) <capacity> (Power in MW) <capacity_factor> (efficiency 0 to 1)

Output: LCOE in €/MWh

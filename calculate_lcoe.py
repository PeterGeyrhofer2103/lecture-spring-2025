import sys

from predict_q import predict_q


def calculate_lcoe(WACC, lifetime, CAPEX, OPEX_fix, capacity, capacity_factor):
    """
    Calculate the Levelized Cost of Electricity (LCOE) for wind energy.

    Parameters:
    - WACC: Weighted Average Cost of Capital for wind projects (decimal form)
    - lifetime: Project lifetime in years
    - CAPEX: Capital Expenditure in €/MW
    - OPEX_fix: Fixed Operational Expenditure in €/MW/year
    - capacity: Installed capacity of the wind turbine in MW
    - capacity_factor: Efficiency of the turbine (between 0 and 1)

    Returns:
    - LCOE in €/MWh
    """
    Q = predict_q(capacity, capacity_factor)  # take Q from other function
    UCRF = (WACC * ((1 + WACC) ** lifetime)) / (
        ((1 + WACC) ** lifetime) - 1
    )  # formula given in VSTE sccript
    LCOE = (CAPEX * UCRF + OPEX_fix) / Q  # formula given in VSTE sccript
    return round(LCOE, 2)


# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 7:  # check if all parameter are there
        print(
            "Define following parameters: <WACC> <lifetime> <CAPEX> <OPEX_fix> <capacity> <capacity_factor>"
        )

        sys.exit(1)

    try:  # check if parameter are the right dimension
        WACC = float(sys.argv[1])
        lifetime = int(sys.argv[2])
        CAPEX = float(sys.argv[3])
        OPEX_fix = float(sys.argv[4])
        capacity = float(sys.argv[5])
        capacity_factor = float(sys.argv[6])

        result = calculate_lcoe(
            WACC, lifetime, CAPEX, OPEX_fix, capacity, capacity_factor
        )
        print("Levelized costs of electricity are:", result, "€/MWh")

    except ValueError as e:
        print("Error:", e)

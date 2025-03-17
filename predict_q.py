import sys


def predict_q(capacity, capacity_factor, hours_per_year=8760):
    """
    Predict the annual energy output (Q_wind) for a wind turbine.

    Parameters:
    - capacity: Installed capacity of the wind turbine in MW
    - capacity_factor: Efficiency of the turbine (between 0 and 1)
    - hours_per_year: Total hours in a year (default is 8760)

    Returns:
    - Predicted annual energy output in MWh
    """
    if not (0 <= capacity_factor <= 1):
        raise ValueError("Capacity factor must be between 0 and 1.")

    return round(capacity * capacity_factor * hours_per_year, 2)


if __name__ == "__main__":
    if len(sys.argv) != 3:  # check if all parameters are there
        print(
            "Define following parameters: python predict_q.py <capacity> <capacity_factor>"
        )
        sys.exit(1)

    try:  # check if parameters are the right dimension
        capacity = float(sys.argv[1])
        capacity_factor = float(sys.argv[2])

        result = predict_q(capacity, capacity_factor)
        print("Predicted annual energy output (Q) is:", result, "MWh")
    except ValueError as e:
        print("Error:", e)

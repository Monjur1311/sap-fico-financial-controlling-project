import pandas as pd

assets = pd.read_csv(
    "data/assets.csv",
    parse_dates=["acquisition_date"]
)

schedule_rows = []

for _, asset in assets.iterrows():

    acquisition_cost = asset["acquisition_cost"]
    useful_life = int(asset["useful_life_months"])

    monthly_depreciation = acquisition_cost / useful_life

    accumulated_depreciation = 0

    start_month = (
        asset["acquisition_date"]
        .to_period("M")
    )

    for period in range(1, useful_life + 1):

        depreciation_date = (
            start_month + period - 1
        ).to_timestamp("M")

        accumulated_depreciation += monthly_depreciation

        net_book_value = (
            acquisition_cost
            - accumulated_depreciation
        )

        # Avoid floating-point residue
        if abs(net_book_value) < 0.01:
            net_book_value = 0

        schedule_rows.append(
            {
                "asset_id": asset["asset_id"],
                "asset_name": asset["asset_name"],
                "period": period,
                "depreciation_date": depreciation_date.date(),
                "monthly_depreciation": monthly_depreciation,
                "accumulated_depreciation": accumulated_depreciation,
                "net_book_value": net_book_value,
                "cost_center": asset["cost_center"],
                "profit_center": asset["profit_center"]
            }
        )

schedule = pd.DataFrame(schedule_rows)

print("=" * 75)
print("RHINETECH GMBH - FIXED ASSET DEPRECIATION SCHEDULE")
print("=" * 75)

print(schedule.to_string(index=False))

print("\nASSET SUMMARY")
print("-" * 75)

for _, asset in assets.iterrows():

    monthly_dep = (
        asset["acquisition_cost"]
        / asset["useful_life_months"]
    )

    print(
        f"\nAsset: {asset['asset_id']} - "
        f"{asset['asset_name']}"
    )

    print(
        f"Acquisition Cost: EUR "
        f"{asset['acquisition_cost']:,.2f}"
    )

    print(
        f"Useful Life: "
        f"{int(asset['useful_life_months'])} months"
    )

    print(
        f"Monthly Depreciation: EUR "
        f"{monthly_dep:,.2f}"
    )

schedule.to_csv(
    "reports/asset_depreciation_schedule.csv",
    index=False
)

print(
    "\nReport exported to "
    "reports/asset_depreciation_schedule.csv"
)

print("=" * 75)
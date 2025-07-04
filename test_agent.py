from main import run_agent

def test_case():
    sample_input = {
        "date": "2025-07-03",
        "revenue": 1200,
        "cost": 800,
        "previous_day_revenue": 1000,
        "previous_day_cost": 600,
        "number_of_customers": 50
    }
    output = run_agent(sample_input)
    assert "profit" in output
    assert "recommendations" in output
    print("✅ Agent Output:", output)

if __name__ == "__main__":
    test_case()
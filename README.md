# LangGraph Business Agent

This AI Agent analyzes daily business metrics and outputs actionable insights.

## Features
- Calculates daily profit
- Calculates CAC (Customer Acquisition Cost)
- Detects significant changes in revenue, cost, and CAC
- Generates smart business recommendations

## Run
```bash
python test_agent.py
```

## Sample Output
```json
{
  "profit": 400,
  "cac": 16.0,
  "alerts": ["CAC increased by 33.3%"],
  "recommendations": ["Review marketing campaigns due to increased CAC", "Consider increasing advertising budget due to revenue growth"]
}
```

Tested in LangGraph Studio ✅
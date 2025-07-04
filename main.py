from langgraph.graph import StateGraph, END
from typing import TypedDict

class BusinessState(TypedDict):
    date: str
    revenue: float
    cost: float
    previous_day_revenue: float
    previous_day_cost: float
    number_of_customers: int
    profit: float
    cac: float
    alerts: list[str]
    recommendations: list[str]

def input_node(state: dict) -> BusinessState:
    state['alerts'] = []
    state['recommendations'] = []
    return state

def processing_node(state: BusinessState) -> BusinessState:
    state['profit'] = state['revenue'] - state['cost']
    prev_cac = state['previous_day_cost'] / state['number_of_customers']
    state['cac'] = state['cost'] / state['number_of_customers']
    
    revenue_change = (state['revenue'] - state['previous_day_revenue']) / state['previous_day_revenue']
    cost_change = (state['cost'] - state['previous_day_cost']) / state['previous_day_cost']
    cac_change = (state['cac'] - prev_cac) / prev_cac

    if cac_change > 0.2:
        state['alerts'].append(f"CAC increased by {round(cac_change * 100, 1)}%")
    if state['profit'] < 0:
        state['recommendations'].append("Reduce costs if profit is negative")
    if cac_change > 0.2:
        state['recommendations'].append("Review marketing campaigns due to increased CAC")
    if revenue_change > 0.1:
        state['recommendations'].append("Consider increasing advertising budget due to revenue growth")
    return state

def output_node(state: BusinessState) -> dict:
    return {
        "profit": state['profit'],
        "cac": round(state['cac'], 2),
        "alerts": state['alerts'],
        "recommendations": state['recommendations']
    }

def run_agent(data: dict):
    builder = StateGraph()
    builder.add_node("input", input_node)
    builder.add_node("process", processing_node)
    builder.add_node("output", output_node)

    builder.set_entry_point("input")
    builder.add_edge("input", "process")
    builder.add_edge("process", "output")
    builder.add_edge("output", END)

    graph = builder.compile()
    return graph.invoke(data)
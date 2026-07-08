from langgraph.graph import (
    StateGraph,
    END
)

from graph.state import HealthState
from graph.nodes import (
    calorie_node,
    nutrition_node,
    meal_node,
    exercise_node,
    progress_node
)
from graph.hitl import human_approval

workflow = StateGraph(
    HealthState
)

workflow.add_node(
    "calorie",
    calorie_node
)

workflow.add_node(
    "nutrition",
    nutrition_node
)

workflow.add_node(
    "meal",
    meal_node
)

workflow.add_node(
    "exercise",
    exercise_node
)

workflow.add_node(
    "progress",
    progress_node
)

workflow.set_entry_point(
    "calorie"
)

workflow.add_edge(
    "calorie",
    "nutrition"
)

workflow.add_edge(
    "nutrition",
    "meal"
)

workflow.add_edge(
    "meal",
    "exercise"
)

workflow.add_conditional_edges(
    "exercise",
    human_approval,
    {
        "approved": "progress",
        "review": END
    }
)

workflow.add_edge(
    "progress",
    END
)

graph = workflow.compile()
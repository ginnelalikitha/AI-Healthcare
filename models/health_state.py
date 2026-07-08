from typing import TypedDict, Optional, Dict, Any


class HealthState(TypedDict):
    user_data: Dict[str, Any]

    calorie: Optional[Dict]
    nutrition: Optional[str]
    meal_plan: Optional[str]
    exercise: Optional[str]
    progress: Optional[Dict]

    approved: bool
    feedback: Optional[str]
from typing import TypedDict
from typing import Optional
from typing import Dict
from typing import Any


class HealthState(TypedDict):
    user_data: Dict[str, Any]

    calorie: Optional[Dict]
    nutrition: Optional[str]
    meal_plan: Optional[str]
    exercise: Optional[str]
    progress: Optional[Dict]

    approved: bool
    feedback: Optional[str]
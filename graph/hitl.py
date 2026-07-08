def human_approval(state):

    if state["approved"]:
        return "approved"

    return "review"
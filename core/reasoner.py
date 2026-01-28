def reason(plan: list) -> str:
    if not plan:
        return "Need more information to proceed."
    return f"Plan created with {len(plan)} steps."

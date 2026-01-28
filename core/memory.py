_memory = []

def save_memory(user_input, intent):
    _memory.append({
        "input": user_input,
        "intent": intent
    })

def get_memory():
    return _memory

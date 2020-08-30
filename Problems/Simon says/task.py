def what_to_do(instructions):
    # simon = instructions.find("Simon says")
    doing = (instructions.replace("Simon says", "")).strip()
    if instructions.startswith("Simon") or instructions.endswith("says"):
        return "I " + doing
    else:
        return "I won't do it!"

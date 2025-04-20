for i in range(24):
    if i == 0:
        print(f"12:00 Midnight")
    elif i == 12:
        print(f"12:00 Noon")
    elif i < 12:
        print(f"{i}:00 AM")
    else:
        print(f"{i - 12}:00 PM")

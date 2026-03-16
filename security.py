# This file logs a security event when suspicious content is detected.

def security_event(message: str):
    print(f"[SECURITY_EVENT] {message}")
from services.lang_detect import detect_language
from memory.redis_store import get_session, set_session
from agent.tools import check_availability, book_appointment

def process_input(text: str):
    lang = detect_language(text)
    session = get_session("demo_user")

    if "book" in text.lower():
        slots = check_availability("cardiologist", "tomorrow")
        set_session("demo_user", {"intent": "booking"})
        return f"Available slots are {slots}"

    if "10" in text:
        result = book_appointment("demo_user", "cardiologist", "10:00 AM")
        return "Appointment booked successfully"

    return "Sorry, I didn't understand"

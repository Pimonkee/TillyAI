
import re
import uuid
from datetime import datetime


def validate_email(email):
    """Validate the format of an email address."""
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(email_regex, email) is not None


def format_date(date_str, input_format='%Y-%m-%d', output_format='%d-%m-%Y'):
    """Format a date string from one format to another."""
    try:
        date_obj = datetime.strptime(date_str, input_format)
        return date_obj.strftime(output_format)
    except ValueError:
        return None


def sanitize_input(input_str):
    """Sanitize user input to prevent injection attacks."""
    return re.sub(r'[^\w\s]', '', input_str).strip()


def generate_unique_id():
    """Generate a unique identifier."""
    return str(uuid.uuid4())
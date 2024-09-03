

### **`src/utils.py`**

```python
import re
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

# Add more utility functions as needed
```

### Description:
- **`validate_email`**: Uses a regular expression to check if an email address is in a valid format.
- **`format_date`**: Converts a date string from one format to another. Handles different date formats for input and output.
- **`sanitize_input`**: Removes special characters from user input to help prevent injection attacks and sanitize input.
- **`generate_unique_id`**: Generates a unique identifier using Python's `uuid` library. (Note: You need to import `uuid` for this function to work.)

### Usage:
1. **Import Utility Functions**:
   In other parts of your application where you need to use these utility functions, import them from `utils.py`. For example:
   ```python
   from src.utils import validate_email, format_date, sanitize_input

   # Validate email
   if validate_email("test@example.com"):
       print("Valid email address")
   else:
       print("Invalid email address")

   # Format date
   formatted_date = format_date("2024-09-03", '%Y-%m-%d', '%d-%m-%Y')
   print("Formatted date:", formatted_date)

   # Sanitize input
   sanitized_input = sanitize_input("Hello <script>alert('XSS')</script>")
   print("Sanitized input:", sanitized_input)
   ```

### Benefits:
- **Code Reusability**: Provides reusable functions that can be used throughout the application, reducing code duplication.
- **Maintainability**: Centralizes utility functions in one place, making it easier to manage and update them.
- **Separation of Concerns**: Keeps utility functions separate from business logic and data models, leading to cleaner and more organized code.

Including a `utils.py` file helps maintain clean and efficient code by centralizing commonly used functions, making it easier to manage and extend your application.
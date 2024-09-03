
### **`src/config.py`**

```python
import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/tillydb')
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
    REDIS_DB = int(os.environ.get('REDIS_DB', 0))

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    ENV = 'development'

class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = False
    TESTING = True
    MONGO_URI = os.environ.get('TEST_MONGO_URI', 'mongodb://localhost:27017/tilly_test_db')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    ENV = 'production'
    MONGO_URI = os.environ.get('PROD_MONGO_URI', 'mongodb://localhost:27017/tilly_prod_db')

def get_config(env):
    """Return the appropriate configuration class based on environment."""
    if env == 'development':
        return DevelopmentConfig
    elif env == 'testing':
        return TestingConfig
    elif env == 'production':
        return ProductionConfig
    else:
        raise ValueError("Invalid environment name")
```

### Description:
- **Base Configuration (`Config`)**: Defines common configuration settings used in all environments, such as `SECRET_KEY`, `MONGO_URI`, `REDIS_HOST`, `REDIS_PORT`, and `REDIS_DB`.
- **Development Configuration (`DevelopmentConfig`)**: Inherits from `Config` and sets settings specific to the development environment, such as enabling `DEBUG`.
- **Testing Configuration (`TestingConfig`)**: Inherits from `Config` and sets settings specific to the testing environment, including a separate MongoDB URI.
- **Production Configuration (`ProductionConfig`)**: Inherits from `Config` and sets settings specific to the production environment, such as disabling `DEBUG`.
- **`get_config` Function**: Returns the appropriate configuration class based on the environment name provided. 

### Usage:
1. **Loading Configuration**:
   In your `create_app` function (or equivalent), you can load the configuration by calling `get_config` with the desired environment name:
   ```python
   from src.config import get_config

   app = Flask(__name__)
   app.config.from_object(get_config('development'))
   ```
   Replace `'development'` with `'testing'` or `'production'` as needed.

2. **Environment Variables**:
   Use environment variables to set sensitive configuration values (e.g., `SECRET_KEY`, `MONGO_URI`). This helps keep sensitive data out of source control and allows for different configurations in different environments.

### Benefits:
- **Centralized Configuration**: Provides a single location for managing application settings, making it easier to adjust settings for different environments.
- **Environment-specific Settings**: Allows for separate configurations for development, testing, and production environments, reducing the risk of configuration errors.
- **Flexibility**: Easily extendable to support additional environments or settings as needed.

Including a `config.py` file helps maintain a clean and organized approach to managing configuration settings, making your application more flexible and easier to deploy across different environments.
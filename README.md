# TillyAI

TillyAI is an advanced AI assistant with natural language processing capabilities, sentiment analysis, and database management features. This project provides a comprehensive, multi-functional AI system built with Flask and MongoDB.

## Features

- **RESTful API**: User management with CRUD operations
- **Natural Language Processing**: Built with NLTK and spaCy
- **Database Integration**: MongoDB for data persistence
- **Modular Architecture**: Clean Flask blueprint structure
- **Configuration Management**: Environment-based configuration

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB (running locally or accessible remotely)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pimonkee/TillyAI.git
   cd TillyAI
   ```

2. Run the build script:
   ```bash
   ./build_TillyAI.sh
   ```

3. Start the application:
   ```bash
   python3 src/main.py
   ```

The application will be available at `http://localhost:5000`

### API Endpoints

#### User Management
- `POST /api/user` - Create a new user
- `GET /api/user/<user_id>` - Get user by ID
- `PUT /api/user/<user_id>` - Update user
- `DELETE /api/user/<user_id>` - Delete user

#### AI Processing
- `POST /api/tilly` - Process text with TillyAI

### Running Tests

```bash
python3 -m unittest discover test
```

## Project Structure

```
TillyAI/
├── src/
│   ├── __init__.py          # Application factory
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration management
│   ├── models.py            # Data models
│   ├── routes.py            # API routes
│   ├── utils.py             # Utility functions
│   └── blueprints/
│       └── __init__.py      # Blueprint registration
├── test/
│   └── test_main.py         # Unit tests
├── build_TillyAI.sh         # Setup script
├── requirements.txt         # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md               # This file
```

## Configuration

The application uses environment-based configuration. Set these environment variables:

- `SECRET_KEY`: Flask secret key
- `MONGO_URI`: MongoDB connection string
- `REDIS_HOST`: Redis server host (optional)
- `REDIS_PORT`: Redis server port (optional)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
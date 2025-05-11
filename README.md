# 🚢 Ship Alarm Server

A FastAPI-based backend for a real-time ship engine monitoring and alarm system.  
This project emulates engine parameters and provides WebSocket and REST APIs for client applications (e.g., Flutter).

## 🌟 Features

- Real-time engine parameter monitoring via WebSocket
- RESTful API endpoints for data access
- Engine parameter emulation with realistic ranges
- Alarm system with warning and critical levels
- JWT-based authentication
- Rate limiting protection
- CORS support for client applications
- Comprehensive error handling
- Automatic data validation

## ⚙️ Tech Stack

- Python 3.13
- FastAPI
- WebSocket (Uvicorn)
- Pydantic v2
- Starlette
- AsyncIO
- JWT for authentication

## 📁 Project Structure

```
ship_alarm_system/
├── app/
│   ├── main.py          # FastAPI application and routes
│   ├── engine.py        # Engine data generation
│   ├── alarms.py        # Alarm system
│   ├── models.py        # Pydantic models
│   └── core/
│       └── config.py    # Application settings
├── .env                 # Environment variables
├── requirements.txt     # Dependencies
└── README.md           # Documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ship_alarm_system.git
cd ship_alarm_system
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:

```env
HOST=0.0.0.0
PORT=8000
DEBUG=True
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
RATE_LIMIT_PER_MINUTE=60
WS_UPDATE_INTERVAL_MS=500
```

### Running the Server

Start the server with:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The server will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, you can access:

- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

### WebSocket Endpoints

- `ws://localhost:8000/engine/stream` - Real-time engine data stream

  - Sends data every 500ms
  - Format: JSON with all engine parameters
  - Example connection using JavaScript:

  ```javascript
  const ws = new WebSocket("ws://localhost:8000/engine/stream");

  ws.onopen = () => {
    console.log("Connected to WebSocket");
  };

  ws.onmessage = (event) => {
    console.log("Received:", JSON.parse(event.data));
  };
  ```

### REST Endpoints

- `GET /api/engine/current` - Get current engine parameters
- `GET /api/engine/history` - Get historical data
  - Parameters:
    - `start_time`: ISO 8601 timestamp
    - `end_time`: ISO 8601 timestamp
    - `parameters`: Optional array of parameter names
- `GET /api/engine/limits` - Get parameter limits
- `GET /api/alarms` - Get active alarms
- `POST /api/alarms/{alarm_id}/acknowledge` - Acknowledge an alarm

### Authentication

All REST endpoints require JWT authentication:

1. Get token:

```bash
curl -X POST "http://localhost:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=password"
```

2. Use token in requests:

```bash
curl -H "Authorization: Bearer <your_token>" http://localhost:8000/api/engine/current
```

## 🔧 Testing

### WebSocket Testing with wscat

1. Install wscat:

```bash
npm install -g wscat
```

2. Connect to WebSocket:

```bash
wscat -c ws://localhost:8000/engine/stream
```

### REST API Testing

Use the Swagger UI at `http://localhost:8000/docs` for interactive testing of REST endpoints.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Roman Kliakhin

Project Link: [https://github.com/yourusername/ship_alarm_system]

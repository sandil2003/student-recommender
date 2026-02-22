# Student Recommender Microservice

A high-performance recommendation engine microservice designed to match students with relevant projects and vice versa. This project leverages Machine Learning techniques like TF-IDF and Cosine Similarity to provide intelligent recommendations.

## Overview

This microservice is part of a larger ecosystem and operates independently to handle all recommendation logic. It provides a RESTful API to fetch project suggestions for students and student suggestions for projects based on skills, interests, and project requirements.

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **ML Logic**: TF-IDF Vectorization & Cosine Similarity
- **Data Handling**: Pandas & NumPy
- **Containerization**: Docker
- **Validation**: Pydantic

## Project Structure

```text
student-recommender/
├── app/
│   ├── api/
│   │   ├── core/           # Configuration and settings
│   │   ├── models/         # Database/Domain models
│   │   ├── schemas/        # Pydantic validation models
│   │   ├── services/       # ML logic (ml_engine.py)
│   │   └── v1/             # API Endpoints (recommend.py)
│   └── main.py             # Application entry point
├── data/                   # Dataset storage (if applicable)
├── tests/                  # Unit and integration tests
├── Dockerfile              # Container definition
└── requirements.txt        # Python dependencies
```

## Setup & Installation

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student-recommender
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

### Docker Setup

```bash
docker build -t student-recommender .
docker run -p 8000:8000 student-recommender
```

## API Endpoints

- `GET /api/v1/recommend/projects/{student_id}`: Get project recommendations for a specific student.
- `GET /api/v1/recommend/students/{project_id}`: Get student recommendations for a specific project.
- `GET /health`: Check service status.

## Recommendation Logic

The engine uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text data (skills, project descriptions) into numerical vectors. **Cosine Similarity** is then calculated to find the closest matches between students and projects.

# Barcelona Software Engineering Job Board

A live tracker for software engineering jobs in Barcelona, aggregating opportunities from multiple sources and providing intelligent filtering, deduplication, and alerting.

## 🎯 Project Vision

This project aims to solve the scattered job search experience by:
- **Centralizing** software engineering opportunities in Barcelona
- **Enriching** job data with location, salary insights, and company information  
- **Filtering** duplicates intelligently across multiple job boards
- **Alerting** users when roles matching their criteria become available

## 🏗️ Current Status

**Early Development** - Core Django structure established

✅ **Completed:**
- Django project scaffolding with `postings` app
- Initial Pydantic schema for job posting validation
- Basic dependencies (Django, Pydantic, requests)

🚧 **In Progress:**
- Django models and database schema design
- ATS integration adapters (Greenhouse, Lever, Teamtailor, InfoJobs)

## 🎯 Planned Features

### Core Pipeline
- **Multi-source fetching**: ATS JSON feeds (Greenhouse, Lever, Teamtailor, InfoJobs)
- **Smart deduplication**: Deterministic hashing + fuzzy title matching
- **Location enrichment**: Geocoding via Nominatim API
- **Role classification**: Regex-based categorization (Junior/Mid/Senior, Frontend/Backend/Fullstack)
- **Search & filtering**: Hybrid keyword/semantic search via OpenSearch

### User Experience  
- **Live updates**: Track "new since last visit" postings
- **Smart alerts**: Email/Telegram notifications for saved search queries
- **Rich filtering**: By role level, tech stack, location, remote options
- **Company insights**: Funding status, team size, tech stack analysis

### Technical Features
- **Fully typed**: Python with mypy, django-stubs, pydantic-django
- **API-first**: Django REST Framework with TypeScript frontend
- **Async processing**: Celery for background jobs and alerts
- **Production-ready**: Docker compose setup with monitoring

## 🛠️ Tech Stack

**Backend:**
- Python 3.12, Django 5.2, Django REST Framework
- PostgreSQL, Redis, OpenSearch  
- Celery + Flower for background processing
- Fully typed with mypy and django-stubs

**Frontend:**
- React 18 + TypeScript
- Modern component architecture

**Infrastructure:**
- Docker & docker-compose for local development
- Designed for easy deployment (Fly.io/Render)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/bcn_jobboard.git
cd bcn_jobboard

# Set up Python environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Set up Django
cd jobboard
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit http://localhost:8000/admin to access the Django admin.

## 📁 Project Structure

```
bcn_jobboard/
├── jobboard/           # Django project root
│   ├── jobboard/       # Main settings package
│   ├── postings/       # Job postings app
│   │   └── schemas.py  # Pydantic validation schemas
│   └── manage.py
├── requirements.txt
└── README.md
```

## 🔮 Next Steps

- **Database Models**: Convert Pydantic schemas to Django models
- **ATS Adapters**: Implement Greenhouse API integration
- **Data Pipeline**: Build fetching, validation, and storage workflow
- **API Endpoints**: Create DRF views for frontend consumption
- **Frontend Foundation**: Set up React + TypeScript client

## 🤝 Contributing

This is a learning project built with portfolio quality in mind. Contributions and feedback welcome!

## 📄 License

MIT License - feel free to fork and adapt for your own regional job board.
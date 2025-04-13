# Quantitative Portfolio

A Flask-based web application showcasing quantitative finance projects and analyses.

## Project Structure

```
quant-portfolio/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── project.html
│   └── static/
│       ├── css/
│       └── images/
│
├── projects/
│   └── stat_arb.ipynb
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Features

- Modern, responsive web interface
- Project showcase with detailed views
- Support for Jupyter notebook integration
- Clean and maintainable code structure

## License

MIT License 
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from app import mail
import os

main = Blueprint('main', __name__)

# Role descriptions and skills
ROLES = {
    'quant': {
        'title': 'Quantitative Analyst',
        'description': 'Expert in mathematical modeling and statistical analysis for financial markets',
        'skills': ['Statistical Analysis', 'Financial Modeling', 'Risk Management', 'Python', 'R']
    },
    'data': {
        'title': 'Data Scientist',
        'description': 'Specialist in extracting insights from complex data sets using machine learning',
        'skills': ['Machine Learning', 'Data Analysis', 'Python', 'SQL', 'Data Visualization']
    },
    'portfolio': {
        'title': 'Portfolio Manager',
        'description': 'Professional in investment strategy and portfolio optimization',
        'skills': ['Portfolio Management', 'Risk Analysis', 'Asset Allocation', 'Financial Markets', 'Python']
    },
    'ml': {
        'title': 'Machine Learning Engineer',
        'description': 'Expert in developing and deploying machine learning models',
        'skills': ['Deep Learning', 'Neural Networks', 'Python', 'TensorFlow', 'PyTorch']
    }
}

# Project data with achievements
PROJECTS = {
    'stat_arb': {
        'title': 'Statistical Arbitrage Strategy',
        'description': 'Developed a market-neutral trading strategy using statistical methods',
        'category': 'quant',
        'roles': ['quant', 'data'],
        'technologies': ['Python', 'Pandas', 'NumPy', 'Scikit-learn'],
        'skills': ['Statistical Analysis', 'Time Series Analysis', 'Risk Management'],
        'achievements': [
            'Achieved 15% annualized returns with Sharpe ratio of 2.5',
            'Reduced drawdown by 40% through advanced risk management',
            'Implemented real-time execution system with 99.9% uptime'
        ],
        'github_url': 'https://github.com/yourusername/stat-arb'
    },
    'portfolio_opt': {
        'title': 'Portfolio Optimization Engine',
        'description': 'Built a modern portfolio optimization system using advanced algorithms',
        'category': 'portfolio',
        'roles': ['portfolio', 'quant'],
        'technologies': ['Python', 'CVXPY', 'Pandas', 'Matplotlib'],
        'skills': ['Portfolio Theory', 'Optimization', 'Risk Management'],
        'achievements': [
            'Optimized portfolio allocation for 50+ assets',
            'Reduced transaction costs by 25% through smart rebalancing',
            'Implemented custom risk metrics for better risk assessment'
        ],
        'github_url': 'https://github.com/yourusername/portfolio-opt'
    },
    'market_micro': {
        'title': 'Market Microstructure Analysis',
        'description': 'Analyzed market microstructure patterns using high-frequency data',
        'category': 'quant',
        'roles': ['quant', 'data'],
        'technologies': ['Python', 'Pandas', 'NumPy', 'Matplotlib'],
        'skills': ['Market Analysis', 'Data Processing', 'Visualization'],
        'achievements': [
            'Identified profitable trading patterns with 60% accuracy',
            'Reduced latency by 30% through optimized data processing',
            'Developed custom visualization tools for market analysis'
        ],
        'github_url': 'https://github.com/yourusername/market-micro'
    },
    'ml_trading': {
        'title': 'Machine Learning Trading System',
        'description': 'Implemented a deep learning-based trading system',
        'category': 'ml',
        'roles': ['ml', 'quant'],
        'technologies': ['Python', 'TensorFlow', 'Keras', 'Pandas'],
        'skills': ['Deep Learning', 'Time Series Prediction', 'Feature Engineering'],
        'achievements': [
            'Achieved 20% better prediction accuracy than traditional methods',
            'Reduced false signals by 35% through advanced filtering',
            'Implemented real-time prediction system with 50ms latency'
        ],
        'github_url': 'https://github.com/yourusername/ml-trading'
    },
    'risk_management': {
        'title': 'Advanced Risk Management System',
        'description': 'Developed a comprehensive risk management framework',
        'category': 'quant',
        'roles': ['quant', 'portfolio'],
        'technologies': ['Python', 'Pandas', 'NumPy', 'Scipy'],
        'skills': ['Risk Analysis', 'Monte Carlo Simulation', 'Stress Testing'],
        'achievements': [
            'Reduced portfolio risk by 30% through advanced hedging',
            'Implemented real-time risk monitoring system',
            'Developed custom risk metrics for better risk assessment'
        ],
        'github_url': 'https://github.com/yourusername/risk-management'
    },
    'data_analysis': {
        'title': 'Financial Data Analysis Platform',
        'description': 'Built a platform for analyzing financial data',
        'category': 'data',
        'roles': ['data', 'quant'],
        'technologies': ['Python', 'Pandas', 'SQL', 'Plotly'],
        'skills': ['Data Analysis', 'Visualization', 'Database Management'],
        'achievements': [
            'Processed 1TB+ of financial data daily',
            'Reduced analysis time by 70% through automation',
            'Created interactive dashboards for data visualization'
        ],
        'github_url': 'https://github.com/yourusername/data-analysis'
    },
    'nlp_finance': {
        'title': 'NLP for Financial News',
        'description': 'Applied NLP techniques to analyze financial news',
        'category': 'ml',
        'roles': ['ml', 'data'],
        'technologies': ['Python', 'NLTK', 'Scikit-learn', 'TensorFlow'],
        'skills': ['Natural Language Processing', 'Sentiment Analysis', 'Text Mining'],
        'achievements': [
            'Achieved 85% accuracy in sentiment analysis',
            'Reduced processing time by 60% through optimized algorithms',
            'Developed real-time news analysis system'
        ],
        'github_url': 'https://github.com/yourusername/nlp-finance'
    },
    'blockchain': {
        'title': 'Blockchain Analytics',
        'description': 'Analyzed blockchain data for trading insights',
        'category': 'data',
        'roles': ['data', 'quant'],
        'technologies': ['Python', 'Web3.py', 'Pandas', 'Matplotlib'],
        'skills': ['Blockchain Analysis', 'Data Mining', 'Pattern Recognition'],
        'achievements': [
            'Identified profitable trading patterns with 70% accuracy',
            'Processed 100M+ blockchain transactions',
            'Developed custom analytics tools for blockchain data'
        ],
        'github_url': 'https://github.com/yourusername/blockchain-analytics'
    },
    'quant_research': {
        'title': 'Quantitative Research Platform',
        'description': 'Developed a platform for quantitative research',
        'category': 'quant',
        'roles': ['quant', 'data'],
        'technologies': ['Python', 'Jupyter', 'Pandas', 'NumPy'],
        'skills': ['Research', 'Data Analysis', 'Statistical Modeling'],
        'achievements': [
            'Published 5 research papers in top journals',
            'Developed 10+ trading strategies',
            'Created automated research workflow system'
        ],
        'github_url': 'https://github.com/yourusername/quant-research'
    },
    'trading_bot': {
        'title': 'Automated Trading Bot',
        'description': 'Built an automated trading system',
        'category': 'quant',
        'roles': ['quant', 'ml'],
        'technologies': ['Python', 'CCXT', 'Pandas', 'TensorFlow'],
        'skills': ['Algorithmic Trading', 'API Integration', 'System Design'],
        'achievements': [
            'Achieved 25% annualized returns',
            'Maintained 99.9% system uptime',
            'Implemented advanced risk management features'
        ],
        'github_url': 'https://github.com/yourusername/trading-bot'
    }
}

@main.route('/')
def index():
    selected_role = request.args.get('role', 'all')
    selected_category = request.args.get('category', 'all')
    
    filtered_projects = {}
    for project_id, project in PROJECTS.items():
        if (selected_role == 'all' or selected_role in project['roles']) and \
           (selected_category == 'all' or project['category'] == selected_category):
            filtered_projects[project_id] = project
    
    return render_template('index.html', 
                         projects=filtered_projects,
                         roles=ROLES,
                         selected_role=selected_role,
                         selected_category=selected_category)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        role = request.form.get('role')
        message = request.form.get('message')
        
        msg = Message(
            subject=f'New Contact Form Submission - {role}',
            sender=os.environ.get('MAIL_DEFAULT_SENDER'),
            recipients=[os.environ.get('MAIL_DEFAULT_SENDER')]
        )
        msg.body = f'''
        Name: {name}
        Email: {email}
        Role: {role}
        Message: {message}
        '''
        
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('There was an error sending your message. Please try again later.', 'error')
        
        return redirect(url_for('main.index'))
    
    return render_template('index.html') 
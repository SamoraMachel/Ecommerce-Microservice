from app.api import api_bp

@api_bp.route('/testing')
def test_url():
    return "Hello Testing"
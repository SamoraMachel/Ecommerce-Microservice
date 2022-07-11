from app.api.v1 import api_v1

@api_v1.route('/testing')
def test_url():
    return "Hello Testing"
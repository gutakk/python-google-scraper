from app import generate_jwt

def test_generate_jwt():
    result = generate_jwt("test@email.com")
    assert result == True
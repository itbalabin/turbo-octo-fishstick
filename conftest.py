from dotenv import load_dotenv

load_dotenv()

pytest_plugins = [
    'fixtures.page',
    'fixtures.user_auth'
]

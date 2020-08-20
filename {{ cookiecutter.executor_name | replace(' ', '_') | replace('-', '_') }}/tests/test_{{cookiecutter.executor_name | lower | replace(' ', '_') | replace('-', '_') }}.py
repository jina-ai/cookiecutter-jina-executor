from .. import {{cookiecutter.executor_name | replace(' ', '_') | replace('-', '_') }}



def test_{{cookiecutter.executor_name | lower | replace(' ', '_') | replace('-', '_') }}():
    """here is my test code

    https://docs.pytest.org/en/stable/getting-started.html#create-your-first-test
    """
    raise NotImplementedError

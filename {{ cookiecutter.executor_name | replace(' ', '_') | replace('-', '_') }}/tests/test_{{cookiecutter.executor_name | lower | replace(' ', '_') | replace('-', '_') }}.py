from .. import {{cookiecutter.executor_name | replace(' ', '_') | replace('-', '_') }}


class TestClass:
    def test_{{cookiecutter.executor_name | lower | replace(' ', '_') | replace('-', '_') }}(self):
        """here is my test code

        https://docs.pytest.org/en/stable/getting-started.html#create-your-first-test
        """
        raise NotImplementedError

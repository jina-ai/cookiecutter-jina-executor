from jina.executors.{{cookiecutter.executor_type | lower}}s import Base{{cookiecutter.executor_type}}

class {{cookiecutter.executor_name | replace(' ', '_') | replace('-', '_') }}(Base{{cookiecutter.executor_type}}):
    """
    :class:`{{cookiecutter.executor_name}}` {{cookiecutter.description}}.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # your customized __init__ below
        raise NotImplementedError

    {% if cookiecutter.executor_type == 'Crafter' %}

    def craft(self, *args, **kwargs):
        raise NotImplementedError

    {% elif cookiecutter.executor_type == 'Encoder' %}

    def encode(self, data, *args, **kwargs):
        raise NotImplementedError

    {% elif cookiecutter.executor_type == 'Indexer' %}

    def query(self, keys, *args, **kwargs):
        raise NotImplementedError

    def add(self, keys, vectors, *args, **kwargs):
        raise NotImplementedError

    {% elif cookiecutter.executor_type == 'Ranker' %}

    def score(self, *args, **kwargs):
        raise NotImplementedError

    {% elif cookiecutter.executor_type == 'Evaluator' %}

    def evaluate(self, *args, **kwargs):
        raise NotImplementedError

    {% elif cookiecutter.executor_type == 'Segmenter' %}

    def segment(self, *args, **kwargs):
        raise NotImplementedError

    {% elif cookiecutter.executor_type == 'Classifier' %}

    def predict(self, *args, **kwargs):
        raise NotImplementedError

    {% endif %}

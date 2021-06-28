__copyright__ = "Copyright (c) 2020-2021 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from jina import Flow, Document

from ... import {{cookiecutter.executor_name}}


def test_exec():
    f = Flow().add(uses={{cookiecutter.executor_name}})
    with f:
        resp = f.post(on='/endpoint', inputs=Document(), return_results=True)
        assert resp is not None

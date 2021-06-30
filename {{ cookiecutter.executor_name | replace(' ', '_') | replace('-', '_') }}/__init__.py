from typing import Optional, Dict

from jina import Executor, DocumentArray, requests


class {{cookiecutter.executor_name}}(Executor):
    """
    {{ cookiecutter.description }}

    """

    @requests(on='/foo_endpoint')
    def do_stuff(self, docs: Optional[DocumentArray], **kwargs):
        """
        Do stuff.
        Please refer more details to https://github.com/jina-ai/jina/blob/master/.github/2.0/cookbooks/Executor.md

        :param docs: documents sent to the Executor
        """
        # do things
        pass
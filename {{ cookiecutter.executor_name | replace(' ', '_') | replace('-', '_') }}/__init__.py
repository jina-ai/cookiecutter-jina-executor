__copyright__ = "Copyright (c) 2020-2021 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from typing import Optional, Dict

from jina import Executor, DocumentArray, requests


class {{cookiecutter.executor_name}}(Executor):
    """
    {{ cookiecutter.description }}

    :param your_param: param description
    """

    def __init__(self, param: int = 128, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self._param = param

    @requests(on='/endpoint')
    def do_stuff(self, docs: Optional[DocumentArray], parameters: Dict, **kwargs):
        """
        Do stuff

        :param docs: documents sent to the Executor
        :param parameters: the parameters to this request
        """
        # do things
        pass
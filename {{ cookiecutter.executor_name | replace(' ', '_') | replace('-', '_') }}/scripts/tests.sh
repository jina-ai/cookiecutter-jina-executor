#!/bin/bash
# run the tests

EXIT_CODE=0

pip install wheel
pip install -r tests/requirements.txt
pip install .
pytest -s -v tests/
local_exit_code=$?

if [[ ! $local_exit_code == 0 ]]; then
  EXIT_CODE=$local_exit_code
  echo CI failed. local_exit_code = $local_exit_code, exit = $EXIT_CODE
fi

echo final exit code = $EXIT_CODE
exit $EXIT_CODE
# ✨ {{cookiecutter.executor_name}}

**{{cookiecutter.executor_name}}** is a class that {{cookiecutter.description}}

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🌱 Prerequisites](#-prerequisites)
- [🚀 Usages](#-usages)
- [🎉️ Example](#%EF%B8%8F-example)
- [🔍️ Reference](#%EF%B8%8F-reference)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 🌱 Prerequisites

Some conditions to fulfill before running the executor

## 🚀 Usages

### 🚚 Via JinaHub

#### using docker images
Use the prebuilt images from JinaHub in your python codes, 

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://{{cookiecutter.executor_name}}')
```

or in the `.yml` config.
	
```yaml
jtype: Flow
pods:
  - name: encoder
    uses: 'jinahub+docker://{{cookiecutter.executor_name}}'
```

#### using source codes

Use the source code from JinaHub in your Python app:

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://{{cookiecutter.executor_name}}')
```

or in the `.yml` config.

```yaml
jtype: Flow
pods:
  - name: encoder
    uses: 'jinahub://{{cookiecutter.executor_name}}'
```


### 🐳 Via Docker

1. Clone the repo and build the docker image

	```shell
	git clone {{cookiecutter.url}} executor
	cd executor
	docker build -t {{ cookiecutter.executor_name | lower }}-image .
	```

1. Use `{{ cookiecutter.executor_name | lower }}-image` in your code

	```python
	from jina import Flow
	
	f = Flow().add(uses='docker://{{ cookiecutter.executor_name | lower }}-image:latest')
	```
	

## 🎉️ Example 

```python
from jina import Flow, Document

f = Flow().add(uses='docker://{{ cookiecutter.executor_name | lower }}-image:latest')

with f:
    resp = f.post(on='/endpoint', inputs=Document(), return_results=True)
    print(f'{resp}')
```

### `on=/endpoint` (Optional)

When there are multiple APIs, we need to list the inputs and outputs for each one. If there is only one universal API, we only demonstrate the inputs and outputs for it.

#### Inputs 

`Documents` ...

#### Returns

Nothing

## 🔍️ Reference
- Some reference


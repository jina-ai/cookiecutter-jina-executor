# ✨ {{cookiecutter.executor_name}}

**{{cookiecutter.executor_name}}** is a class that {{cookiecutter.description}}

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


## 🎉️ Example 

```python
from jina import Flow, Document

f = Flow().add(uses='docker://{{ cookiecutter.executor_name | lower }}-image:latest')

with f:
    resp = f.post(on='/foo_endpoint', inputs=Document(), return_results=True)
    print(f'{resp}')
```

### `on=/foo_endpoint` (Optional)

#### Inputs 

`/foo_endpoint` accepts ...

#### Returns

`/foo_endpoint` returns ...

## 🔍️ Reference
- Some reference


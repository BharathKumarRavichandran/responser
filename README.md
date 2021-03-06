# Responser

[![PRs Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](http://makeapullrequest.com) [![made-with-python](https://img.shields.io/badge/made%20with-python-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Responser is a python package to convert normal strings, objects and other data to REST API response convention and in JSON format.

## Usage

### `Responser`
-----------------------------------------

Responser is a python package to convert normal strings, objects and other data to REST API response convention and in JSON format.

This function follows the following JSON structure.

```json
{
  "status_code": 200,
  "data": {
    "name": "Bharath Kumar Ravichandran",
    "alma_mater": "NIT Trichy",
    "languages_known": [
        "Python",
        "PHP",
        "JS",
        "C++"
    ],
    "cool_guy": "yes",
  },
  "message": "OK"
}
```

#### `JSONResponser`
* Import the function with `from responser import JSONResponser`
* Definition `JSONResponser(status_code=400, data=None, message=None, strict_mode=false)`
* The `status_code` can be HTTP status codes or your own custom status codes.
* If the `status_code` is a HTTP status code and the `data` is `None`, a default
[reason phrase](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html) is added. (If `strict_mode` is `False` (default) )
* If the `status_code` is a HTTP status code and the `message` is `None`, a default
[reason phrase](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html) is added. (Even if `strict_mode` is `True` (default) ).
* If the `status_code` is not a HTTP status code and the `data` is `None`, an empty data is added.
* If the `status_code` is not a HTTP status code and the `message` is `None`, an empty message is added.
* If the `strict_mode` is set to `True`, the data given as `data` is encoded.
* The `status_code` defaults to 400. 

**Sample Code**
```python
from responser import JSONResponser

status_code = 200
data = {
    "name": "Bharath Kumar Ravichandran",
    "alma_mater": "NIT Trichy",
    "languages_known": [
        "Python",
        "PHP",
        "JS",
        "C++"
    ],
    "cool_guy": "yes",
}
message = "User details returned."

response = JSONResponser(status_code, data, message)
print response
```
**Output**
```json
{
  "status_code": 200,
  "data": {
    "name": "Bharath Kumar Ravichandran",
    "alma_mater": "NIT Trichy",
    "languages_known": [
        "Python",
        "PHP",
        "JS",
        "C++"
    ],
    "cool_guy": "yes",
  },
  "message": "User details returned."
}
```


#### `JSONResponserDecorator`
* Import the decorator with `from responser import JSONResponserDecorator`
* Wrap function with decorator `@JSONResponserDecorator`
* `JSONResponserDecorator` is built on top of JSONResponser, so it follows the same convention as `JSONResponser`.

**Sample Code**
```python
from responser import JSONResponserDecorator

@JSONResponserDecorator
def sample_function():

    data = {
        "name": "Bharath Kumar Ravichandran",
        "alma_mater": "NIT Trichy",
        "languages_known": [
            "Python",
            "PHP",
            "JS",
            "C++"
        ],
        "cool_guy": "yes",
    }

    return data
```
**Returned Data**
```json
{
  "status_code": 200,
  "data": {
    "name": "Bharath Kumar Ravichandran",
    "alma_mater": "NIT Trichy",
    "languages_known": [
        "Python",
        "PHP",
        "JS",
        "C++"
    ],
    "cool_guy": "yes",
  },
  "message": "OK"
}
```


### Inspired from
[GokulSrinivas/Sangria](https://github.com/GokulSrinivas/Sangria)

### Contributors
[Bharath Kumar Ravichandran](https://github.com/BharathKumarRavichandran/)

## License
[MIT](LICENSE)

![Built with love](http://forthebadge.com/images/badges/built-with-love.svg)

# Allogate
## A very simple logging package

# Usage example

```python
import allogate as logging

logging.VERBOSITY=1
logging.pprint(f"Hello, this is a failure", 0)
logging.pprint(f"Hello, this is a success", 1)
logging.pprint(f"Hello, this is a warning", 2)
logging.pprint(f"Hello, this is an info"  , 3)
logging.pprint(f"Hello, this is verbose"  , 4)
logging.pprint(f"Hello, this is very verbose"  , 12)

logging.VERBOSITY=3
logging.pprint(f"Hello, this is a failure", 0)
logging.pprint(f"Hello, this is a success", 1)
logging.pprint(f"Hello, this is a warning", 2)
logging.pprint(f"Hello, this is an info"  , 3)
logging.pprint(f"Hello, this is verbose"  , 4)
logging.pprint(f"Hello, this is very verbose"  , 12)


logging.VERBOSITY=5
logging.pprint(f"Hello, this is a failure", 0)
logging.pprint(f"Hello, this is a success", 1)
logging.pprint(f"Hello, this is a warning", 2)
logging.pprint(f"Hello, this is an info"  , 3)
logging.pprint(f"Hello, this is verbose"  , 4)
logging.pprint(f"Hello, this is very verbose"  , 12)


logging.VERBOSITY=15
logging.pprint(f"Hello, this is a failure", 0)
logging.pprint(f"Hello, this is a success", 1)
logging.pprint(f"Hello, this is a warning", 2)
logging.pprint(f"Hello, this is an info"  , 3)
logging.pprint(f"Hello, this is verbose"  , 4)
logging.pprint(f"Hello, this is very verbose"  , 12)
```
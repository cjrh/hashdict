# hashdict
Dict that only stores hashes of the keys, and not the key value. Good for large keys.

## Overview

`HashDict` is a Python package that provides a dictionary-like class designed to save memory when 
keys are large. Instead of storing the full text, it only stores a hash of the text, reducing memory usage significantly.

The main drawback is that the original key values are not recoverable from the `HashDict` instance,
but this is also by design.

## Example Usage

Here's a quick example to get you started with `HashDict`:

```python
from hashdict import HashDict

# Create a new HashDict instance
hash_dict = HashDict()

# Add a large text key
s = "some large text " * 1000
hash_dict[s] = 42

# Retrieve the value using the same large text key
print(hash_dict[s])  # Output: 42

# Save the HashDict to a file
hash_dict.save('hash_dict.pkl')

# Load the HashDict from a file
loaded_hash_dict = HashDict.load('hash_dict.pkl')
print(loaded_hash_dict[s])  # Output: 42
```

## Extra features

`HashDict` also supports the following features:

### Persistence

You can save a `HashDict` instance to a file and load it back later:

```python
from hashdict import HashDict

# Create a new HashDict instance
hash_dict = HashDict()

# Add entries
hash_dict["example text"] = 100
hash_dict["another example"] = 200

# Save to file
hash_dict.save('my_hash_dict.pkl')

# Load from file
loaded_hash_dict = HashDict.load('my_hash_dict.pkl')
print(loaded_hash_dict["example text"])  # Output: 100
```

Internally, the `save` method writes to a temporary file and then renames it to the final file name,
to ensure that the file at the original path is not corrupted if the process is interrupted.

"""
HashDict is a dictionary that uses the hash of the key to store the value.
"""
import pickle
import os
import tempfile

__version__ = '0.1.0'


class HashDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _hash_key(self, key):
        return hash(key)

    def __setitem__(self, key, value):
        hashed_key = self._hash_key(key)
        super().__setitem__(hashed_key, value)

    def __getitem__(self, key):
        hashed_key = self._hash_key(key)
        return super().__getitem__(hashed_key)

    def __delitem__(self, key):
        hashed_key = self._hash_key(key)
        super().__delitem__(hashed_key)

    def __contains__(self, key):
        hashed_key = self._hash_key(key)
        return super().__contains__(hashed_key)

    def save(self, file_path):
        temp_fd, temp_path = tempfile.mkstemp()
        try:
            with os.fdopen(temp_fd, 'wb') as temp_file:
                pickle.dump(dict(self), temp_file, protocol=pickle.HIGHEST_PROTOCOL)
            os.replace(temp_path, file_path)
        except Exception as e:
            os.remove(temp_path)
            raise e

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            return cls(data)

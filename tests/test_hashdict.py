from hashdict import HashDict


def test_hashdict():
    hash_dict = HashDict()
    s = "some large text " * 1000
    hash_dict[s] = 42
    assert hash_dict[s] == 42


def test_save_load(tmpdir):
    # Do this in a temporary directory to avoid cluttering the working directory
    tmpdir.chdir()
    hash_dict = HashDict()
    hash_dict["some large text"] = 42
    hash_dict.save('hash_dict.pkl')
    loaded_hash_dict = HashDict.load('hash_dict.pkl')
    assert loaded_hash_dict["some large text"] == 42
    assert loaded_hash_dict == hash_dict


def test_delete_key():
    hash_dict = HashDict()
    hash_dict["some large text"] = 42
    del hash_dict["some large text"]
    assert "some large text" not in hash_dict


def test_contains_key():
    hash_dict = HashDict()
    hash_dict["some large text"] = 42
    assert "some large text" in hash_dict
    assert "nonexistent key" not in hash_dict


def test_overwrite_key():
    hash_dict = HashDict()
    hash_dict["some large text"] = 42
    hash_dict["some large text"] = 99
    assert hash_dict["some large text"] == 99


def test_multiple_keys():
    hash_dict = HashDict()
    hash_dict["some large text"] = 42
    hash_dict["another large text"] = 99
    assert hash_dict["some large text"] == 42
    assert hash_dict["another large text"] == 99

from main import task


def test_one():
    func = task([{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {},
                 {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}])  # noqa 501
    assert func == [{'key1': 'value1'}, {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'},
                    {}, {'key2': 'value2'}]


def test_two():
    func = task([{'me': 'Denis'}, {'me': 'Denis'}, {'a': 1, 'k': 3}])
    assert func == [{'me': 'Denis'}, {'a': 1, 'k': 3}]


def test_three_false():
    func = task([{'me': 'Denis'}, {'me': 'Denis'}, {'a': 1, 'k': 3}])
    assert func == [{'me': 'Denis'}, {'me': 'Denis'}, {'a': 1, 'k': 3}]

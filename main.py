from collections import Counter


dict_list = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {},
                {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]


def task(dict_list):
    tuple_list = [tuple(i.items()) for i in dict_list]

    c = Counter(tuple_list).keys()
    end = [{key: val for key, val in i} for i in c]
    return end

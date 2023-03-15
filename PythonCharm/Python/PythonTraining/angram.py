def is_anagram(a_word, b_word):
    return sorted(a_word) == sorted(b_word)


def test_anagram():
    print('## Start noPom ##')

    assert is_anagram("abc", "acb")
    assert is_anagram("silent", "listen")
    assert is_anagram('abc','bbc')
    assert not is_anagram("one", "two")
    assert 4==4
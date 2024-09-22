import selenium
import pytest
@pytest.fixture()
def before_after_text():
    print("Start test")
    yield
    print("\nFinish")


def test_demo(before_after_text):
    assert 1 == 1

def test_demo2(before_after_text):
    assert 3 == 3
from helper.preprocess import zero_padding

import pytest

@pytest.mark.parametrize("test_input,desired", [(3, "003"), (1234, "1234")])
def test_zero_padding(test_input, desired):
    assert zero_padding(test_input, width=3) == desired

from states_data_mysql import get_states
import pytest

def test_get_states():
    state = get_states()
    assert state


pytest.main(["-v", "--tb=line", "-rN", __file__])
from states_data_mysql import get_states, get_a_state
import pytest

# Manually adding the supposed states ids to test get_a_state()
# All numbers would be tested as a parameter
test_user_input_two = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
 
def test_get_states():
    assert get_states()

@pytest.mark.parametrize("id", test_user_input_two)
def test_get_a_state(id):
    assert get_a_state(id)


pytest.main(["-v", "--tb=line", "-rN", __file__])
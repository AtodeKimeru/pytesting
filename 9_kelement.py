def create_array(N: int) -> list:
  if N < 1 or N >= 10000:
    raise ValueError('N must be between 1 and 10000')
  array = list()
  for i in range(N):
    element = int(input())

    limit = 10**9
    if element < limit * -1 + 1 or element > limit - 1:
      raise ValueError("The array's items must be between -10^9 and 10^9")
    
    array.append(element)
    
  return array
    

def run() -> None:
  create_array(3)

if __name__ == '__main__':
  run()



# TESTS
from unittest import TestCase, mock


class BlackBoxTest(TestCase):
  # test driven development with unit tests

  @mock.patch('9_kelement.input', side_effect=[30, 40, 70])
  def test_valid_array_length(self, mocked_input):
    array = create_array(3)
    self.assertIsNotNone(array)

  def test_invalid_array_length(self):
    with self.assertRaises(ValueError):
      create_array(-5)

  def test_lower_limit_array_length(self):
    with self.assertRaises(ValueError):
      create_array(0)

  def test_upper_limit_array_length(self):
    with self.assertRaises(ValueError):
      create_array(10000)

  @mock.patch('9_kelement.input', side_effect=[30, 40, 70])
  def test_valid_array_creation(self, mocked_input):
    array = create_array(3)
    self.assertEqual(array, [30, 40, 70])

  @mock.patch('9_kelement.input', side_effect=['a', 'b', 'c'])
  def test_invalid_input_array_creation(self, mocked_input):
    with self.assertRaises(ValueError):
      create_array(3)

  @mock.patch('9_kelement.input', side_effect=[-10**9, 40, 70])
  def test_lower_limit_input_array_creation(self, mocked_input):
    with self.assertRaises(ValueError):
      create_array(3)
  
  @mock.patch('9_kelement.input', side_effect=[10**9, 40, 70])
  def test_upper_limit_input_array_creation(self, mocked_input):
    with self.assertRaises(ValueError):
      create_array(3)

  @mock.patch('9_kelement.input', side_effect=[40, 40, 70])
  def test_element_repeated_array_creation(self, mocked_input):
    with self.assertRaises(DuplicateValuesNotAllowedError):
      create_array(3)

import unittest
import main


class TestMain(unittest.TestCase):
  
  def test_get_input(self):
    self.assertGreater(main.get_input(), 0)

  def test_get_file_data(self):
    self.assertGreater(len(main.get_file_data('playerlist.txt')), 0)
    self.assertEqual(len(main.get_file_data('playerlist2.txt')), 0)
    self.assertLess(len(main.get_file_data('')), 1)

  def test_create_aux_lists(self):
    testing_dict = {
      "values": [
        {"first_name": "mario", "h_in": 70},
        {"first_name": "luigi", "h_in": 69}
      ]
    }
    self.assertIsNone(main.create_aux_lists({})[0])
    self.assertEqual(len(main.create_aux_lists(testing_dict)[0]), 2)
    self.assertGreater(len(main.create_aux_lists(testing_dict)[1]), 0)


  def test_find_pairs(self):
    list_one = [
      {"first_name": "Lorem", "last_name": "Ipsum", "h_in": 70},
      {"first_name": "Anakin", "last_name": "Skywalker", "h_in": 69},
      {"first_name": "Boba", "last_name": "Fett", "h_in": 64},
    ] 
    list_two = [70, 69, 64]
    self.assertEqual(len(main.find_pairs(139, [], [])), 0)
    self.assertIsInstance(main.find_pairs(139, list_one, list_two), list)
    self.assertGreater(len(main.find_pairs(139, list_one, list_two)), 0)


if __name__ == "__main__":
  unittest.main()
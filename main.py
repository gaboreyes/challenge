"""
The task is to create an application that takes a single integer input. 
The application will download the raw data from an json file (playerlist.json)
Print a list of all pairs of players whose height in inches adds up to the integer input to the application. 
If no matches are found, the application will print "No matches found"

Sample output is as follows:
> app 139
- Brevin Knight         Nate Robinson
- Nate Robinson         Mike Wilks

The algorithm to find the pairs must be faster than O(n^2). All edge cases
should be handled appropriately. Though not strictly required, demonstrating
comfort in writing unit tests will make your submission stand out. This is
_not_ a closed book test. You are encouraged to reach out with any questions
that you come across.
"""

# Note: the "playerlist" file inside the given zip was a .txt not a .json

import json

def get_input():
  """
  Gets user input from keyboard adn returns it as int
  """
  target = None
  while(target == None or target <= 0):
    try: target = int(input("Please provide an Integer greater than 0: "))
    except: print('----- input has to be a positive integer -----')
  return target


def get_file_data(file_name):
  """
  Looks for a file with file_name, reads it and creates a dict with the content of the file
  """
  try:
    input_file = open(file_name, "r")
    input_to_str = input_file.read()
    input_file.close()
    return json.loads(input_to_str)
  except:
    print('----- could not find the data file -----')
    return {}


def create_aux_lists(input_dict):
  """
  Input is a dictionary, it tries to create 2 lists with the contents of that dict.
  Then returns a tuple with both lists
  """
  try:
    players_list = input_dict['values']
    inches_map = map(lambda x: int(x['h_in']), players_list)
    return (players_list, list(inches_map))
  except:
    return (None, None)


def find_pairs(target, players_list, inches_list):
  """
  Recieves an int target and 2 lists of the same length
  Checks if the sum of each iteration's players h_in add up to the given target
  If the pair of players are not already inside output_list appends them
  then returns a list of tuples with the player names
  """
  output_list = []
  
  try:
    for i in players_list:
      b = target - int(i['h_in'])

      if(b in inches_list):
        first_player = i['first_name'] + " " + i['last_name']
        second_player = players_list[inches_list.index(b)]['first_name'] + " " + players_list[inches_list.index(b)]['last_name']

        output_tuple = ( first_player , second_player )
        inverse_output_tuple = ( second_player , first_player )

        # check if this pair of players does not exists in output_list and that they are 2 different players
        if(output_tuple not in output_list and inverse_output_tuple not in output_list and first_player != second_player):
          output_list.append( ( first_player, second_player ) )
    return output_list
  except:
    return []
  

def main():

  target = get_input()

  input_dict = get_file_data("playerlist.txt")

  (players_list, inches_list) = create_aux_lists(input_dict)
  
  output_list = find_pairs(target, players_list, inches_list)
  
  print(output_list) if len(output_list) > 0 else print("No matches found")


if __name__ == "__main__":
  main()
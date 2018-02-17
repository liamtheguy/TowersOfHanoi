"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2018.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin,dest)


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.model = TOAHModel(number_of_stools)

        self.model.fill_first_stool(number_of_cheeses)
        
        #the complete model of the model
        self.model_complete = TOAHModel(number_of_stools)
        self.model_complete._stools[number_of_stools-1] = self.model._stools[0][0:]


    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.

        % press q to quit

        - starting the game:
            after 
        -
        """
        #printing out the instruction for game
        print('***___________INSTRUCTION___________***\n\
welcome to the game, for moving position of cheese \n \
first type the index of the stool, to select the top cheese on it.\n\
Then put "," and after type the index of the stool which you want\n\
to put the selected cheese on. also for exiting just input "q".')
        #initializing the user input
        user_input = ''
        #initializing whether the game has finished or not
        has_solved = False

        while user_input != 'q' and  not has_solved:

            print(self.model)
            user_input = input('Please enter the moving order: ')

            if user_input != 'q':

                
                try:

                    positions = user_input.split(',')
                    
                    start_pos = int(positions[0])

                    dest_pos = int(positions[1])

                    move(self.model, start_pos, dest_pos)

                except:

                    print('Illegal Move, please enter the move again')


                finally:

                    if self.model == self.model_complete:

                        print('Congrats!! you have solved the game')
                        has_solved = True

                
        print('The Game is Over.\nThanks for playing the game.')


if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    

    #taking user input for the number of stools and number of cheeses
    num_cheeses = 0
    num_stools = 0

    while num_cheeses < 1 or num_stools < 2:

        try:
            
            num_stools = int(input('Please enter the the number of stools: '))
            num_cheeses = int(input('please enter number of cheeses: '))

        except:

            print('Illegal entry please try again.')
            num_cheeses = 0
            num_stools = 0

    
    console = ConsoleController(num_cheeses, num_stools)
    console.play_loop()

    
    

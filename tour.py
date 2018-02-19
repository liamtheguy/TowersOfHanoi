"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
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
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "__main__":'

import time
from toah_model import TOAHModel


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=True):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """   
    if not animate:
        
        delay = 0
    else:
        
        delay = delay_btw_moves
        
    print(model)
    time.sleep(delay)
    hanoi_4_stools(0,3,1,2,len(model._stools[0]),model, delay)
   
def hanoi_3_stools(source,target,other,n, model, delay):
    
    if n == 1:
        model.move(source, target)
        print(model)
        time.sleep(delay)
    else:
        hanoi_3_stools(source,other,target,n-1, model, delay)
        model.move(source, target)
        print(model)
        time.sleep(delay)
        hanoi_3_stools(other,target,source,n-1, model, delay)


def hanoi_4_stools(source, target, other1 , other2, n, model, delay) -> None:
    """
    A method to move n cheeses from the starting stool to the final stools 
    with the help of 2 intermediate stools (or total of 4 stools) 
    (this method calls the 3 stool method)
    """
    temp_dict = {}

    #The base_case for 1,2 and 3 number of cheeses
    
    if n <= 3 :

        besecase_solver(source, target, other1 , other2, n, model, delay)

        
    else: 
#determining the best number of cheeses to cut to optimal the process
        i = optimal_cut(n, temp_dict)[1]
        hanoi_4_stools(source, other2, other1, target, n-i, model, delay)
        hanoi_3_stools(source,target,other1,i,model, delay)
        hanoi_4_stools(other2, target, source, other1, n-i, model, delay)


def besecase_solver(source, target, other1 , other2, n, model, delay):

    # manual solution for 3 cheeses.
    if n == 3:

              
        model.move(source, other1)
        print(model)
        time.sleep(delay)
        model.move(source, other2)
        print(model)
        time.sleep(delay)
        model.move(source, target)
        print(model)
        time.sleep(delay)
        model.move(other2, target)
        print(model)
        time.sleep(delay)
        model.move(other1, target)
        print(model)
        time.sleep(delay)
        
    # manual solution for 2 cheeses.       
    elif n == 2:
        
        model.move(source, other2)
        print(model)
        time.sleep(delay)
        model.move(source, target)
        print(model)
        time.sleep(delay)
        model.move(other2, target)
        print(model)
        time.sleep(delay)
        
   # manual solution for 1 cheese.      
    elif n == 1:
        
        model.move(source, target)
        print(model)
        
    else:
        
        print('illegal number of cheeses')

    
def optimal_cut(num_cheese, temp_dict):
    '''
    finds the optimal number of cheeses
    to cut from the the pile of cheeses we have,
    so we can have the optimal number of moves.
    '''
    
    if num_cheese == 1:
        temp_dict[num_cheese] = 1, 1
    else:
        for i in range(1, num_cheese):
            min_moves = 2 * optimal_cut(num_cheese - i, temp_dict)[0] + (2 ** i) - 1
            if min_moves < temp_dict.get(num_cheese, (2 ** num_cheese + 1,0))[0]: #Better moves found
                temp_dict[num_cheese] = (min_moves, i)
    return temp_dict[num_cheese]
        
    
    
    

if __name__ == '__main__':
    num_cheeses = 6
    delay_between_moves = 0.5
    console_animate = True

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())

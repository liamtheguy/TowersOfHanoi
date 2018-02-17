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
    animate = True
    delay_btw_moves = 0.1
    
    print(model)
    
    hanoi_4_stools(0,3,1,2,len(model._stools[0]),model)
   
def hanoi_3_stools(source,target,other,n, model):
    if n == 1:
        model.move(source, target)
        print(model)
    else:
        hanoi_3_stools(source,other,target,n-1, model)
        model.move(source, target)
        print(model)
        hanoi_3_stools(other,target,source,n-1, model)


def hanoi_4_stools(source, target, other1 , other2, n, model) -> None:
    """
    A method to move n cheeses from the starting stool to the final stools 
    with the help of 2 intermediate stools (or total of 4 stools) 
    (this method calls the 3 stool method)
    """
    
    if n > 3:
        
        i = optimal_cut(n)
        hanoi_4_stools(source, other2, other1, target, n-i, model)
        hanoi_3_stools(source,target,other1,i,model)
        hanoi_4_stools(other2, target, source, other1, n-i, model)
    
    elif n == 3:

              
        model.move(source, other1)
        model.move(source, other2)
        model.move(source, target)
        model.move(other2, target)
        model.move(other1, target)
        
    elif n == 2:
        
        model.move(source, other2)
        model.move(source, target)
        model.move(other2, target)
        
    else:
        model.move(source, target)
       

def optimal_cut(num_cheese):
    
    initial = 3
    end = 5
    optimal = 2
    i = 3
    while True:
    
        if initial <= num_cheese and num_cheese <= end:

            return optimal

        else:
            
            optimal += 1
            initial += i
            end += i+1
            i += 1 

    
    
    

if __name__ == '__main__':
    num_cheeses = 6
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())


def hanoi(source, target, other,n):

    if n == 1:
         print ('move the disk on the '+source+ ' peg to '+ target+ 'peg.')

    else:

        hanoi(source, other, target, n-1)
        print('move the disk on the ' + source + 'peg to ' + target + 'peg.' )
        hanoi(source, other, target, n-1)

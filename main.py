from tests import main
from snek import snek

#inp=input('Select Mode\n1. Showcases\n2. SnakeDEV\n> ')
inp='2'

if inp.startswith('1'):
    main()
elif inp.startswith('2'):
    snek()
from BFSDemo import BFS
from Astardemo import aStar
from pyMaze import maze,agent,COLOR,textLabel
from timeit import timeit

myMaze=maze(10,30)
myMaze.CreateMaze(loopPercent=100)
# myMaze.CreateMaze()
searchPath,aPath,fwdPath=aStar(myMaze)
bSearch,bfsPath,fwdBFSPath=BFS(myMaze)

l=textLabel(myMaze,'A-Star Path Length',len(fwdPath)+1)
l=textLabel(myMaze,'BFS Path Length',len(fwdBFSPath)+1)
l=textLabel(myMaze,'A-Star Search Length',len(searchPath)+1)
l=textLabel(myMaze,'BFS Search Length',len(bSearch)+1)
c=agent(myMaze,footprints=True,color=COLOR.red,shape='square',filled=True)
a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
b=agent(myMaze,footprints=True,color=COLOR.yellow)
d=agent(myMaze,footprints=True,color=COLOR.green,shape='square',filled=True)
myMaze.tracePath({c:bSearch},delay=20)
myMaze.tracePath({a:fwdBFSPath},delay=50)
myMaze.tracePath({d:searchPath},delay=20)
myMaze.tracePath({b:fwdPath},delay=50)

t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
t2=timeit(stmt='BFS(myMaze)',number=10,globals=globals())

textLabel(myMaze,'A-Star Time',t1)
textLabel(myMaze,'BFS Time',t2)


myMaze.run()
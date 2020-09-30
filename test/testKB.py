from vpython import *

box()
ev = scene.waitfor('click keydown')
if ev.event == 'click':
    print('You clicked at', ev.pos)
else:
    print('You pressed key '+ev.key)
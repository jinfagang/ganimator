from nosmpl.parsers import bvh_io
import sys


animation = bvh_io.load(sys.argv[1])
print(animation.names)
print(animation.frametime)
print(animation.parent)
print(animation.offsets)
print(animation.shape)
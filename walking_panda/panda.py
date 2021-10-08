import sys
import platform
from . import panda
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class WalkingPandaApp(ShowBase):
    def __init__(self, no_rotate=False, scale=False, no_move=False):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        if (no_rotate==False) :

            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        else:
            self.taskMgr.add(self.nospinCameraTask, "NoSpinCameraTask")


        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(scale, scale, scale)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        if (no_move==False):

            posInterval1 = self.pandaActor.posInterval(13, Point3(0, -10, 0), startPos = Point3(0, 10, 0))

            posInterval2 = self.pandaActor.posInterval(13, Point3(0, 10, 0), startPos = Point3(0, -10, 0))


            hprInterval1 = self.pandaActor.hprInterval(3, Point3(180, 0, 0), startHpr = Point3(0, 0, 0))

            hprInterval2 = self.pandaActor.hprInterval(3, Point3(0, 0, 0), startHpr = Point3(180, 0, 0))

            self.pandaPace = Sequence(posInterval1, hprInterval1, posInterval2, hprInterval2, name = "pandaPace")
            self.pandaPace.loop()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def nospinCameraTask(self, task):
        angleDegrees = 60
        angleRadians = 1
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont





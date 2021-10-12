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
    def __init__(self, no_rotate=False, scale=False, colour=False, no_move=False, first_person=False):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.



        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(scale, scale, scale)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        if (no_rotate==False) and first_person==False :

            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        elif no_rotate==True and first_person==False :
            self.taskMgr.add(self.nospinCameraTask, "NoSpinCameraTask")
        elif first_person==True :
            self.taskMgr.add(self.firstpersonCameraTask, "FirstPersonCameraTask")
            global pandadirection
            pandadirection = self.pandaActor.getHpr()

        if colour=="red" :
            self.pandaActor.setColor(255, 0, 0, 255)
        elif colour=="green" :
            self.pandaActor.setColor(0, 255, 0, 255)
        elif colour=="blue" :
            self.pandaActor.setColor(0, 0, 255, 255)
        elif colour=="yellow" :
            self.pandaActor.setColor(255,255,0)
        elif colour=="purple" :
            self.pandaActor.setColor(128,0,255,255)
        elif colour=="orange" :
            self.pandaActor.setColor(255,128,0,255)


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
        angleDegrees = task.time * 0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def firstpersonCameraTask(self,task):
        self.camera.setPos(self.pandaActor.get_pos())
        if self.pandaActor.getHpr()== pandadirection:
            self.camera.setHpr(180, 0, 0)
        else:
            self.camera.setHpr(0,0,0)
        return task.cont



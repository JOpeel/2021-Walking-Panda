from . import panda
import argparse

def cli():


    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--scale", type=float, default=0.005)
    parser.add_argument("--no-move",action="store_true")
    parser.add_argument("--colour", type=str)
    parser.add_argument("--first-person", action="store_true")
    args = parser.parse_args()

    walking = panda.WalkingPandaApp(**vars(args))
    walking.run()

    app = panda.WalkingPandaApp()
    app.run()

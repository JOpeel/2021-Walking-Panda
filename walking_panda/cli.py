from . import panda
import argparse

def cli():


    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    args = parser.parse_args()

    walking = panda.WalkingPandaApp(**vars(args))
    walking.run()

    app = panda.WalkingPandaApp()
    app.run()

"""
This lab works on connecting to the robot (or sim)
"""
import numpy as np

from argparse import ArgumentParser

from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose

from reachy_mini_labs.utils import reset_head



def run():
    # While using the sim the connection fails when trying to setup the "default" media backend.
    parser = ArgumentParser()
    parser.add_argument("--use-sim", action="store_true", default=False, help="use the sim connection", required=False)

    namespace = parser.parse_args()

    print("initial script")
    # with no arguments the SDK will search for localhost:8000 first
    # then fallback to the <host>:<port>, which are defaulted to reach-mini.local:8000

    # no_media when using the sim daemon
    media_backend = "no_media" if namespace.use_sim == True else "default"


    with ReachyMini(media_backend=media_backend, use_sim=namespace.use_sim) as mini:
        print("connected")
        reset_head(mini=mini)

        print("set a new head position")
        head_pose = create_head_pose(x=10, y=10, z=10, mm=True)
        mini.goto_target(
            head=head_pose,
            antennas=[np.deg2rad(-45), np.deg2rad(45)],
            duration=1.0,
        )

        print("move back to reset position")
        reset_head(mini=mini)
        
        

if __name__ == "__main__":
    run()
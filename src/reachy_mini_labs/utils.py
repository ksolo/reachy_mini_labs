from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose

def reset_head(mini: ReachyMini):
    # create_head_pose defaults x,y,z, pitch, roll, yaw values to 0
    head_pose = create_head_pose()
    mini.goto_target(
        head=head_pose,
        antennas=[0.0, 0.0],
        duration=1.0
    )
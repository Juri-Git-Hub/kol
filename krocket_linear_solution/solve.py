from utility import intersection
from algorithm_magic import solveTask
from testing import plotTwoLines
from utility import test_orientation


def linearAlg(list_goals, ball_radius):
    # Initialisierung:
    # erstes und letztes Tor von Liste von Toren abtrennen und einzeln speichern
    first_goal = list_goals.pop(0)
    last_goal = list_goals.pop(-1)

    # Orientierungstest: rein: erstes und letztes Tor; raus: Benennung von den Pfosten in l und r
    # der 1. Pfosten eines Tores ist IMMER der l Pfosten, der 2. ist IMMER der r Pfosten
    possible_orientations = test_orientation(first_goal, last_goal)

    # 1. Tor kann zwei Durchschussrichtungen haben
    # TODO implement different configurations (lr) for the first goal
    first_goal_lr = [orientation[0:2] for orientation in possible_orientations]
    last_goal_lr = [orientation[2:4] for orientation in possible_orientations]

    # # a configuration consists of the first, the preceding and last goal with lr orientation
    # initial_orientations = zip(first_goal_lr, first_goal_lr, last_goal_lr)

    # get the first new goal
    first_new_goal = list_goals.pop(0)

    # get the orientation for the first new goal
    first_new_goal_orientations = test_orientation(first_goal, first_new_goal)
    first_new_goal_lr = [orientation[2:4] for orientation in first_new_goal_orientations]

    # collection of all currently still possible configurations
    # the candidate configurations are initialized with the configurations of the first new goal
    candidate_configurations = list(list([first_new_goal_lr]))

    # Workhorse Loop
    # für jedes neue Tor in der Liste von Toren:

    for i, new_goal in enumerate(list_goals):
        new_candidate_configurations = []
        # Iteration:
        # gleich werden interessant: erste Tor, vorausgehende Tor, neues Tor, letztes Tor
        # für beide Durchschussrichtungen des ersten Tors mit dem entsprechenden letzten Tor
        for configuration in candidate_configurations:
            new_orientations = test_orientation(first_goal, new_goal)

            # extract the new goal orientation from the orientation list
            new_goal_orientations = [orientation[2:4] for orientation in new_orientations]

            # get all new configurations with the new goal orientations
            current_configurations = [[*configuration, orientation] for orientation in new_goal_orientations]

            # update the new candidate config list
            new_candidate_configurations = [*new_candidate_configurations, *current_configurations]

        candidate_configurations = new_candidate_configurations

    path = solveTask(candidate_configurations, first_goal, last_goal_lr[0], ball_radius, list_goals)
    return path

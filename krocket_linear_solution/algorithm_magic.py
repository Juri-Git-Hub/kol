from matplotlib import pyplot as plt
from testing import plotPerpLines

from utility import crossProduct, perpendicularIntersectionPoint, lengthVector


def solveTask(configurations, first_goal, last_goal):
    # within these two lines is the solution, if there is one
    # ll and rr are the boundaries of the shot
    ll_line = (first_goal[0], last_goal[0])
    rr_line = (first_goal[1], last_goal[1])
    print(ll_line)
    print(rr_line)
    for configuration in configurations:
        post_distances = getDistances(configuration, ll_line, rr_line)
        left_distances = post_distances["left"]
        right_distances = post_distances["right"]

        left_max = 0
        left_max_post_i = None
        for post in left_distances:
            if post[3] > left_max:
                left_max = post[3]
                left_max_post_i = left_distances.index(post)

        if left_max_post_i is not None:
            first_posts = left_distances[0:left_max_post_i + 1]
            last_posts = left_distances[left_max_post_i:]

            new_line = first_posts[0], first_posts[-1]
            first_posts.pop(0)
            first_posts.pop(-1)

        right_max = 0
        right_max_post_i = None
        for post in right_distances:
            if post[3] > right_max:
                right_max = post[3]
                right_max_post_i = right_distances.index(post)


def getDistances(list_goals, ll_line, rr_line):
    post_distances = {
        "left": [],
        "right": [],
    }

    for goal in list_goals:
        left_post = goal[0]  # lp for short
        right_post = goal[1]  # rp for short

        lp_intersection = perpendicularIntersectionPoint(ll_line, left_post)
        left_length = lengthVector([left_post, lp_intersection])
        lp_direction = crossProduct(ll_line, left_post)

        if lp_direction < 0:
            left_length = left_length * -1

        rp_intersection = perpendicularIntersectionPoint(rr_line, right_post)
        right_length = lengthVector([right_post, rp_intersection])
        rp_direction = crossProduct(rr_line, right_post)

        if rp_direction > 0:
            right_length = right_length * -1

        post_distances["left"].append([left_post, lp_intersection, left_length])
        post_distances["right"].append([right_post, rp_intersection, right_length])

    return post_distances

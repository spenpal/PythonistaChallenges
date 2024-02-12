SPEED_OF_SOUND = 0.343  # km/sec


def find(
    s1: tuple[int, int, float], s2: tuple[int, int, float], s3: tuple[int, int, float]
) -> tuple[int, int]:
    """
    1. Use the speed of sound to calculate how far the sensor is away from the bomb.
    2. Triangulate the position of the bomb using 3 circle equations (one for each sensor).
        - To learn how the code was derived, visit the following link:
        - https://drive.google.com/file/d/1Ejt2qP9Zjvyq7ZuzlXNH5kyVb6_HnQJN/view?usp=sharing
    """
    # Centers and radii
    h1, h2, h3 = s1[0], s2[0], s3[0]
    k1, k2, k3 = s1[1], s2[1], s3[1]
    r1, r2, r3 = s1[2] * SPEED_OF_SOUND, s2[2] * SPEED_OF_SOUND, s3[2] * SPEED_OF_SOUND

    # Calculate constants
    c1, c2, c3 = (
        (r1**2 - h1**2 - k1**2),
        (r2**2 - h2**2 - k2**2),
        (r3**2 - h3**2 - k3**2),
    )

    # Calculate determinants
    det = 4 * ((h1 - h2) * (k1 - k3) - (h1 - h3) * (k1 - k2))
    det_x = 2 * ((k1 - k3) * (c2 - c1) - (k1 - k2) * (c3 - c1))
    det_y = 2 * ((h1 - h2) * (c3 - c1) - (h1 - h3) * (c2 - c1))

    # Calculate coordinates of the bomb
    x = round(det_x / det)
    y = round(det_y / det)

    return (x, y)

find_oneline = lambda s1, s2, s3: (round((2 * ((s1[1] - s3[1]) * (((s2[2] * 0.343) ** 2 - s2[0] ** 2 - s2[1] ** 2) - ((s1[2] * 0.343) ** 2 - s1[0] ** 2 - s1[1] ** 2)) - (s1[1] - s2[1]) * (((s3[2] * 0.343) ** 2 - s3[0] ** 2 - s3[1] ** 2) - ((s1[2] * 0.343) ** 2 - s1[0] ** 2 - s1[1] ** 2)))) / (4 * ((s1[0] - s2[0]) * (s1[1] - s3[1]) - (s1[0] - s3[0]) * (s1[1] - s2[1])))), round((2 * ((s1[0] - s2[0]) * (((s3[2] * 0.343) ** 2 - s3[0] ** 2 - s3[1] ** 2) - ((s1[2] * 0.343) ** 2 - s1[0] ** 2 - s1[1] ** 2)) - (s1[0] - s3[0]) * (((s2[2] * 0.343) ** 2 - s2[0] ** 2 - s2[1] ** 2) - ((s1[2] * 0.343) ** 2 - s1[0] ** 2 - s1[1] ** 2)))) / (4 * ((s1[0] - s2[0]) * (s1[1] - s3[1]) - (s1[0] - s3[0]) * (s1[1] - s2[1])))))
def hours_to_seconds(hours):
    hr_to_min = hours * 60
    min_to_sec = hr_to_min * 60 
    return min_to_sec


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)

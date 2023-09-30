"""
Measuring the success of the Instagram TV (IGTV) using the User Engagement Metric

"""

# (i): Viewership metric

# A function of the average of the view counts
def viewership():
    # Dummy data, a representation of actual view counts on Instagram TV
    view_count = [35000, 32000, 27000, 22000, 20000, 37500, 42000, 39000, 34000, 49750]

    # This is the amount of view counts that Instagram considers a successful threshold
    success_view_count = 30000
    
    average_count = sum(view_count) / len(view_count)

    if average_count > success_view_count:
        print ("The IGTV is a success judging on the viewership metrics, i.e. view counts.")
    else:
        print("The IGTV is not a success judging on the viewership metrics, i.e. view counts.")
        
# (ii): Watch count

def watch_count():
    # Dummy data, a representation of actual watch time and video durations on Instagram TV
    watch_time_seconds = [3500, 3000, 2700, 3100, 3250, 3700, 4000, 2600, 2870, 3015]
    video_duration = [270, 300, 480, 315, 240, 200, 180, 420, 325, 310]

    successful_threshold = 15 # The successful threshold in minutes of watch time per video
    watch_time_minutes = sum(watch_time_seconds) / 60
    average_watch_time = watch_time_minutes / len(watch_time_seconds)

    if average_watch_time > successful_threshold:
        print("The IGTV is a success judging on the watch time metrics, i.e. watch time and video duration.")
    else:
         print("The IGTV is not a success judging on the watch time metrics, i.e. watch time and video duration.")

watch_count()

# (iii) Retention:

def user_retention():
    # Dummy data of users retained by Instagram TV in the last 12 months in percentages
    users_retained = [80, 77, 85, 92, 90, 87, 90, 88, 83, 85, 87, 82]
    successful_retention_rate = 80 # In percentage

    average_user_retained = sum(users_retained) / len(users_retained)
    print(average_user_retained)

    if average_user_retained >= successful_retention_rate:
         print("The IGTV is a success judging on the user retention metrics, i.e. users retained by IGTV.")
    else:
        print("The IGTV is not a success judging on the user retention metrics, i.e. users retained by IGTV.")


user_retention()





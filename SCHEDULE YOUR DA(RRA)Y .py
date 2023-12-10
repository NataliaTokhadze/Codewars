def day_plan(hours, tasks, duration):
    
    times = []
    
    if tasks == 0 :
        return []
    elif hours < (tasks*duration) / 60 :
        return 'You\'re not sleeping tonight!'
    else:
        for i in range(tasks - 1) :
            times.append(duration)
            x = ((hours * 60) - (tasks*duration)) / (tasks - 1)
            times.append(int(x))
    times.append(duration)
    return times
# TODO (Meta)
# fix the formatting of the annex/seperate it into the readme/some
# sort of notes file

from math import ceil

# inputs:
# STARTING STATE W/ASSUMPTIONS:
    # milestones
    # number of people

# milestones = [('name'(str),time(int/float)),('name2',time)]
milestones = [('a',1),('b',1),('c',1),('d',1)]
num_ppl = 3
training_ratio = 2 # every n people can be trained by 1 person

# calculable values from state:
# total project time
total_time = sum([i[1] for i in milestones])

# error = ('error_milestone name'(str),time it actually took(int/float))
error = ('a',2)

# calculate the ratio of actual_time/projected time
# finding elapsed time along the way.
theoretical_elapsed_time = 0

for i in milestones:
    if i[0] == error[0]:
        actual_to_projected_ratio = error[1]/i[1]
        flag = True
        actual_elapsed_time = theoretical_elapsed_time + error[1]
        theoretical_elapsed_time += i[1]
        break
    else:
        theoretical_elapsed_time += i[1]


# work left in project
theoretical_time_left_in_project = total_time-theoretical_elapsed_time

# time left in project
actual_time_left_in_project = total_time-actual_elapsed_time
# until you get to 
# naive estimation of "number of people to add to a project"
naive_num_ppl_needed = (theoretical_time_left_in_project * num_ppl) /actual_time_left_in_project
naive_num_ppl_to_add = ceil(naive_num_ppl_needed-num_ppl)

print(theoretical_time_left_in_project)
print(actual_time_left_in_project)
print(naive_num_ppl_to_add)

# actual time to completion:
# again this is a model according specifically to Frederick P. Brooks. 
# we can pick apart how the construction of his argument is largely hunch based
# / personal experience based later/ with some data science if data exists sfor this thing.

# intentional num_people to add (parameter?)
# this is just what you would like to do, irrespective of 
# a "naive" calculation. (based on a model much simpler than this one)

# ANNEX

# MILESTONES DATA FORMAT:
    # milestones = [('name',time),('name2',time)]
        # """ 
        # There are two possible time formats:
        # 1) time = time to complete that particular task
        # 2) time = moment in time when the task is due
        # The data structure has to be inherently ordered,
        # cause milestones are in sequence.
        # 1 is a better way to do it on the backend so use that
        # """
    #TODO
        # """ 
        # Its easy to switch between the two data formats, so 
        # either allow for both in the interface
        # and just use one in the backend. Do this
        # after first implimenting with just 1
        # it may be useful to plan in terms of overal time points
        # instead of relative time points. which is why both should
        # be allowed as inputs.
        
        # It would also be nice to have a map of actual months
        # and how productivity is influenced in actual months
        # based on history. I would guess that months with holidays/snow
        # or bad weather in general in your geographic locale will 
        # have less productivity compared to nice weather months, and months
        # with medium amounts of days off (no days off is also probably low, but
        # this is pure guesswork, so data must be collected
        # """
    #TODO
        # """ 
        # Allow for the units on time to be adjusted 
        # and whenever time information is rendered render by properly
        # rounding in those units. So 1.2 months is either 1 month and 1 week,
        # or n number of days, or n number of weeks. Whatever makes sense at
        # every scale. (months, days, weeks, years, hours, minutes? Every scale. 
        # Not anything lower than minutes though. Hell maybe not even hours/days)
        # """
# ERROR IN ASSUMPTIONS
    # """
    # For now lets just go with the error that 
    # the first milestone is the one that was missed
    # Account for two cases:
    # 1) adjust up (shifting timeline, but not scaling it)
    #     1a) add people to project (the worst case (the one pointed out in the book))
    #     1b) don't add any people (This is the most boring case)
    # 2) scale out milestones (shifting timeline, and scaling it)
    #     2a) add people (the most reasonable)
    #     2b) don't add people (marginally less boring than 1b)
    # ,but
    # The error in assumptions here can be:
    # one of the milestones, 
    # all of the milestones (by a rate)
    # or the number of people.   
    # """

# ERROR DATA FORMAT:
    # error = ('error_milestone',time it actually took)




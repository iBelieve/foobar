"""
Zombit antidote
===============

Forget flu season. Zombie rabbits have broken loose and are terrorizing
Silicon Valley residents! Luckily, you've managed to steal a zombie antidote
and set up a makeshift rabbit rescue station. Anyone who catches a zombie
rabbit can schedule a meeting at your station to have it injected with the
antidote, turning it back from a zombit to a fluffy bunny. Unfortunately, you
have a limited amount of time each day, so you need to maximize these meetings.
Every morning, you get a list of requested injection meetings, and you have to
decide which to attend fully. If you go to an injection meeting, you will join
it exactly at the start of the meeting, and only leave exactly at the end.

Can you optimize your meeting schedule? The world needs your help!

Write a method called answer(meetings) which, given a list of meeting requests,
returns the maximum number of non-overlapping meetings that can be scheduled.
If the start time of one meeting is the same as the end time of another, they
are not considered overlapping.

meetings will be a list of lists. Each element of the meetings list will be a
two element list denoting a meeting request. The first element of that list
will be the start time and the second element will be the end time of that
meeting request.

All the start and end times will be non-negative integers, no larger than 1000000.
The start time of a meeting will always be less than the end time.

The number of meetings will be at least 1 and will be no larger than 100.
The list of meetings will not necessarily be ordered in any particular fashion.

Test cases
==========

Inputs:
    (int) meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
Output:
    (int) 4

Inputs:
    (int) meetings = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
Output:
    (int) 1
"""

def answer(meetings):
    scheduler = Scheduler(meetings)

    scheduler.schedule()

    return len(scheduler.meetings)


def meetings_conflict(meeting1, meeting2):
    start_time_overlaps = meeting2.start >= meeting1.start and meeting2.start < meeting1.end
    end_time_overlaps = meeting2.end > meeting1.start and meeting2.end <= meeting1.end

    return start_time_overlaps or end_time_overlaps


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "({}-{})".format(self.start, self.end)

class Scheduler:
    def __init__(self, meetings):
        self.meeting_invites = {id:Meeting(*meeting) for id, meeting in enumerate(meetings)}
        self.meetings = {}

    def schedule(self):
        meetings = self.find_conflicts()
        meetings.sort(key=lambda meeting: meeting['conflicts'])

        for meeting in meetings:
            self.schedule_meeting(meeting['id'])

    def find_conflicts(self):
        conflicts = []

        for id in range(0, len(self.meeting_invites)):
            conflicts.append(dict(id=id, conflicts=self.number_of_conflicts(id, invites=True)))
        return conflicts

    def number_of_conflicts(self, id, invites=False):
        meetings = self.meeting_invites if invites else self.meetings

        meeting = self.meeting_invites[id]
        conflicts = 0
        for other_id, other_meeting in meetings.items():
            if other_id == id:
                continue
            if meetings_conflict(meeting, other_meeting):
                conflicts += 1
        return conflicts

    def schedule_meeting(self, id):
        conflicts = self.number_of_conflicts(id)
        if conflicts == 0:
            self.meetings[id] = self.meeting_invites[id]
            return True
        else:
            return False

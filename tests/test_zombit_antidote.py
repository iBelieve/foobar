import zombit_antidote

def test_case_1():
    assert zombit_antidote.answer([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]) ==  4

def test_case_2():
    assert zombit_antidote.answer([[0, 1000000], [42, 43], [0, 1000000], [42, 43]]) == 1

def test_meeting_should_not_conflict():
    meeting1 = zombit_antidote.Meeting(1, 2)
    meeting2 = zombit_antidote.Meeting(2, 3)
    assert not zombit_antidote.meetings_conflict(meeting1, meeting2)

def test_meeting_should_conflict():
    meeting1 = zombit_antidote.Meeting(1, 3)
    meeting2 = zombit_antidote.Meeting(2, 3)
    assert zombit_antidote.meetings_conflict(meeting1, meeting2)

def houseOfCats(legs):
    
    return [people for people in range(legs//2 + 1)
            if (legs - 2*people) % 4 == 0]

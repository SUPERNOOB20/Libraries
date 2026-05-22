def round_robin(group_size = 4, number_of_groups = 12):

    all_groups: list[tuple[int]] =  []

    for group in range(1, number_of_groups + 1):
        
        for team in range (1, group_size + 1):

            for matched_team in range(team, group_size + 1):
                if team != matched_team:
                    all_groups.append((team + ((group - 1) * 4), matched_team + ((group - 1) * 4)))


    return all_groups


print(round_robin(4, 12))
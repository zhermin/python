def with_bubblesort():

    number_of_names = int(input())

    # Initialise the main list and the scores list
    all_pairs = []
    all_scores = []

    # Allows user to input each name & score
    # After each iteration of the loop, puts both the name & score together in a temporary list
    for i in range(number_of_names):

        name_score_pair = []
        name = input()
        name_score_pair.append(name)

        score = float(input())
        name_score_pair.append(score)

        # Stores all the scores into the list all_scores
        all_scores.append(score)
        # Finally adds the pair into the main list all_pairs
        all_pairs.append(name_score_pair)

    # The "Bubble Sort" sorting algorithm
    for i in range(len(all_pairs)):
        for j in range(len(all_pairs) - 1 - i):
            if all_pairs[j][1] > all_pairs[j+1][1]:

                # Swaps the two numbers if the one before is bigger than the one after
                temp = all_pairs[j]
                all_pairs[j] = all_pairs[j+1]
                all_pairs[j+1] = temp

                # Code below works only in Python (for swapping)
                # all_pairs[j], all_pairs[j+1] = all_pairs[j+1], all_pairs[j]

    # Use function "set" to an array of only unique items
    # Then use function "sorted" to turn it into a list and also sort it
    unique_scores = sorted(set(all_scores))

    # Get the 2nd item from the sorted list at index 1
    second_smallest = unique_scores[1]

    # Initialise empty list for all that are second smallest
    all_second_smallest = []

    # Appends all second smallest pairs into the list
    for i in range(len(all_pairs)):
        if all_pairs[i][1] == second_smallest:
            all_second_smallest.append(all_pairs[i])

    # Sorts the final list using "sorted", which sorts the based on the first element in each list
    # [['b',1], ['a',99]] will become [['a',99],['b',1]]
    all_second_smallest = sorted(all_second_smallest)
    for i in range(len(all_second_smallest)):
        print(all_second_smallest[i][0])

def short_one():

    number_of_names = int(input())

    all_pairs = []
    all_scores = []

    for i in range(number_of_names):

        name_score_pair = []
        name = input()

        score = float(input())
        name_score_pair.append(score)
        name_score_pair.append(name)

        all_scores.append(score)
        all_pairs.append(name_score_pair)

    second_smallest = sorted(set(all_scores))[1]

    all_second_smallest = []
    for i in range(len(all_pairs)):
        if all_pairs[i][0] == second_smallest:
            all_second_smallest.append(all_pairs[i])
    
    names_in_second_smallest = []
    for i in range(len(all_second_smallest)):
        names_in_second_smallest.append(all_second_smallest[i][1])

    names_in_second_smallest = sorted(names_in_second_smallest)
    for name in names_in_second_smallest:
        print(name)
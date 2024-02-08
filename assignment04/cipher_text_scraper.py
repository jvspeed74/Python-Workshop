passages = {
    "The Raven": "Open here I flung the shutter, when, with many a flirt and flutter, In there stepped a stately "
                 "Raven of the saintly days of yore; Not the least obeisance made he; not a minute stopped or stayed "
                 "he; But, with mien of lord or lady, perched above my chamber door— Perched upon a bust of Pallas "
                 "just above my chamber door— Perched, and sat, and nothing more.",
    "Fire and Ice": "Some say the world will end in fire, Some say in ice. From what I’ve tasted of desire I hold "
                    "with those who favor fire. But if it had to perish twice, I think I know enough of hate To say "
                    "that for destruction ice Is also great And would suffice.",
    "Awaking in New York": "Curtains forcing their will against the wind, children sleep, exchanging dreams with "
                           "seraphim. The city drags itself awake on subway straps; and I, an alarm, awake as a rumor "
                           "of war, lie stretching into dawn, unasked and unheeded.",
    "I'm thankful that my life doth not deceive": "I’m thankful that my life doth not deceive Itself with a low "
                                                  "loftiness, half height, And think it soars when still it dip its "
                                                  "way Beneath the clouds on noiseless pinion Like the crow or owl, "
                                                  "but it doth know The full extent of all its trivialness, "
                                                  "Compared with the splendid heights above. See how it waits to "
                                                  "watch the mail come in While ’hind its back the sun goes out "
                                                  "perchance. And yet their lumbering cart brings me no word, "
                                                  "Not one scrawled leaf such as my neighbors get To cheer them with "
                                                  "the slight events forsooth, Faint ups and downs of their far "
                                                  "distant friends— And now ’tis passed. What next? See the long "
                                                  "train Of teams wreathed in dust, their atmosphere; Shall I attend "
                                                  "until the last is passed? Else why these ears that hear the "
                                                  "leader’s bells Or eyes that link me in procession? But hark! the "
                                                  "drowsy day has done its task, Far in yon hazy field where stands a "
                                                  "barn, Unanxious hens improve the sultry hour And with contented "
                                                  "voice now brag their deed— A new laid egg—Now let the day decline— "
                                                  "They’ll lay another by tomorrow’s sun.",
}


def get_two_char():
    while True:  # get passage
        passage_input = input("Enter a passage greater than 200 characters: ")

        if len(passage_input) < 200:
            print("Passage too short")
            continue

        break  # escape loop 1 if valid

    while True:  # get letter to check
        char_input = input("Enter which letter to check: ")

        if len(char_input) != 1:
            print("More than one character entered")
            continue

        break  # escape loop 2 if valid

    return passage_input, char_input


def get_count(passage, char):
    return passage.count(char)


def main():
    while True:
        passage, char = get_two_char()
        occurrence_num = get_count(passage, char)
        if occurrence_num == 0:
            print("No occurrences found, enter another char")
            continue

        print(occurrence_num)
        break


main()

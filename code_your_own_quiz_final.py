
easy_string = """\nA neutron star is the result of a __1__. __1__e are the
cataclysmic deaths of __2__ of greater mass than our own. Another result
of __1__e are __3__. __3__ come from __2__ of even greater mass than those
that create neutron stars. Neutron stars can be pushed to __1__ if too much
__4__ falls into them. """
easy_answers = ['supernova', 'stars', 'black holes', 'mass']
easy_blanks = ['__1__','__2__','__3__','__4__'] 


medium_string = """Caesar's De Bello Gallico
\nGallia __1__ omnis divisa in partes tres, quarum unam incolunt __2__, aliam
__3__, tertiam qui ipsorum lingua __4__, nostra __5__ appellantur. """
medium_answers = ['est', 'Belgae', 'Aquitani', 'Celtae', 'Galli']
medium_blanks = ['__1__','__2__','__3__','__4__','__5__'] 


hard_string = """\nTrigonometry is the study of __1__. __1__ are more interesting
than they might seem at first. With them, you can measure __2__. Using
Trigonometric functions, such as Sine, __3__, and __4__, you can discover
myriads of information, and compare them to other __1__ to do some pretty
cool stuff. """
hard_answers = ['right triangles', 'distance', 'Cosine', 'Tangent']
hard_blanks = ['__1__','__2__','__3__','__4__']


count = 1

def import_parameters(difficulty_choice):
    """Imports string parameters.

    Args:
            difficulty_choice: Difficulty chosen by user.
    Returns:
            The appropriate string, blank list, answers, and count for the
            selected difficulty.
            
    """
    if difficulty_choice == 'easy':
        return easy_string, easy_blanks, easy_answers, count
    elif difficulty_choice == 'medium':
        return medium_string, medium_blanks, medium_answers, count
    elif difficulty_choice == 'hard':
        return hard_string, hard_blanks, hard_answers, count
    else:
        return -1, -1, -1, -1


def is_non_negative_integer(error_quantity):
    """Checks if error_quantity is valid.

    Arg:
            error_quantity: The amount of errors allowed.
    Returns:
            error_quantity or -1.
                
    """
    try:
        error_integer = int(error_quantity)
        #error_integer
        if error_integer >= 0:
            return error_integer
        else:
            return -1
    except ValueError:
        return -1

    
def is_answer(user_input, string_answers, blank):
    """Checks if user_input is correct answer.

    Args:
            user_input: Response for blank.
            string_answers: Answer list.
            blank: The current blank in the string.
    Returns:
            True or False.
                
    """
    blank = blank.split('__')
    raw_number = blank[1] 
    set_index_position = -1
    return user_input == string_answers[int(raw_number) +
                                        set_index_position]


def ask_for_answer(quiz_string, quiz_blanks, quiz_answers, count,
                   error_quantity):
    """Asks for answer for blank.

    Args:
            quiz_string: String in which blanks are to be replaced.
            quiz_blanks: The list of blanks for the selected string.
            quiz_answers: The list of answers for the selected string.
            count: Used to determine which blank is to be replaced.
            error_quantity: Allowed amount of errors, set by user.
    Returns:
            String with answer in place of blank or -1.
                    
    """
    while count <= len(quiz_blanks):
        blank = '__' + str(count) + '__'
        if blank in quiz_string:
            user_input = raw_input('\nWhat shall the replacement be for ' +
                                   str(blank) + ' , Sire? \n:')
            answer = is_answer(user_input, quiz_answers, blank)
            if answer == True:
                quiz_string = quiz_string.replace(blank, user_input)
                count += 1
                print (quiz_string) 
            elif answer == False and error_quantity > 1:
                print ('\nIncorrect. Try again.\n' + str(error_quantity) +
                        ' attempts left.')
                error_quantity -= 1
            elif answer == False and error_quantity == 1:
                print ('\nIncorrect. Try again.\n1 attempt left')
                error_quantity -= 1
            elif answer == False and error_quantity == 0:
                return -1
    

def print_end_game(result):
    """Prints result of quiz.

    Args:
            result: Whether the game is supposed to continue or end.
    Returns:
            'GAME OVER' or 'YOU WON'.
                
    """
    if result == -1:
        return ('\n*************\n* GAME OVER *\n*************')
    else:
        return ('\n************\n* YOU WON! *\n************')
            
    
def run_quiz():
    """Ties all other functions together. Supervisor function. 

    Args:
            difficulty_choice: Difficulty selected by user.
            number_quantity: Amount of errors allowed, selected by user.
    Returns:
            No output specific to this function. Final output sent to
            print_result.
            
    """
    while True:
        difficulty_choice = raw_input('Select a difficulty:\neasy | medium | hard\n:')
        quiz_string, quiz_blanks, quiz_answers, count = import_parameters(difficulty_choice)
        if quiz_string == -1:
            print ('\nInvalid difficulty. Try again.\n')
        else:
            while True:
                number_input = raw_input('\nHow many errors are allowed?\n:')
                error_quantity = is_non_negative_integer(number_input)
                if error_quantity == -1:
                    print ('\nInvalid number, try again.\nType number not word '
                           '(ex."1" not "one").\nNumber must be greater than '
                           'or equal to zero.')
                else:
                    print (quiz_string)
                    result = ask_for_answer(quiz_string, quiz_blanks,
                                            quiz_answers, count, error_quantity)
                    print (print_end_game(result))
                    return
                
run_quiz()


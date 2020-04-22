from stack import Stack


# Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


# Set up the Game
def setup():
    user_input = input('\nHow many disks do you want to play with?\n')
    num_disks = int(user_input)

    while num_disks < 3:
        user_input = input('Enter a number greater than or equal to 3\n')
        num_disks = int(user_input)

    # Create disks and place in the left stack in reverse order
    for disk in range(num_disks, 0, -1):
        left_stack.push('Disk {}'.format(disk))

    num_optimal_moves = 2**(num_disks) - 1

    print('\nThe fastest you can solve this game is in {0} moves'.format(
        num_optimal_moves))

    return num_disks, num_optimal_moves


# Get User Input
def get_input():
    choices = [
        stack.get_name()[0] for stack in stacks
    ]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print('Enter {0} for {1}'.format(letter, name))
        user_input = input()
        if user_input in choices:
            index = choices.index(user_input)
            return stacks[index]


# main game play
def main():
    print("\nLet's play Towers of Hanoi!!")

    num_user_moves = 0
    num_disks, num_optimal_moves = setup()

    while right_stack.get_size() < num_disks:

        print('\n\n\n...Current Stacks...')
        for stack in stacks:
            stack.print_items()
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()
        print('\nWhich stack do you want to move to?\n')
        to_stack = get_input()

        if (not from_stack.is_empty() and
                (to_stack.is_empty() or
                    (from_stack.peek() < to_stack.peek()))):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
        else:
            print('\n\nInvalid Move. Try Again')

    print('\n\n You completed the game in {0} moves, and the optimal number of'
          'moves is {1}'.format(num_user_moves, num_optimal_moves))


if __name__ == '__main__':
    main()

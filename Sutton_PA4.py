#########################################################
# State Machine
# Author: Garett Sutton
# Team Members: Garett Sutton
# Due Date: 12/5/2024
# Program Name: Sutton_PA4.py
# Python Version: 3.12
#########################################################

# Dependencies
import random
import datetime

# Initialize constants used for states.
SCENARIO = 1  # Should be 1 or 2
FOLLOW = 0
PULL_OUT = 1
ACCELERATE = 2
PULL_IN_AHEAD = 3
PULL_IN_BEHIND = 4
DECELERATE = 5
DONE = 6

NOW = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Simulation Variables
scenarioInterval = [100, 1000000][SCENARIO - 1]
transitionProbability = [[0.8, 0.4, 0.3, 0.4, 0.3, 0.3, 0.8, 0.8, 0.8], [0.9, 0.6, 0.3, 0.2, 0.2, 0.4, 0.7, 0.9, 0.7]][SCENARIO-1]
stateCount = [0, 0, 0, 0, 0, 0, 0]
transitionCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
scenarioTrace = True if SCENARIO == 1 else False

# Define the possible state and transition sequences based on the scenario
state_sequence_options = [
    list(range(1, 8)),   # Sequence 1: [1, 2, 3, 4, 5, 6, 7]
    [7] + list(range(1, 7))  # Sequence 2: [7, 1, 2, 3, 4, 5, 6]
]

transition_sequence_options = [
    list(range(1, 10)),  # Sequence 1: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [9] + list(range(1, 9))  # Sequence 2: [9, 1, 2, 3, 4, 5, 6, 7, 8]
]

# Select the appropriate sequences based on SCENARIO
stateSequence = state_sequence_options[SCENARIO - 1]
transitionSequence = transition_sequence_options[SCENARIO - 1]

# File Paths for Input and Output
OUTPUT_FILE = f'Scenario_{SCENARIO}_Output_GS.txt'

# State Functions
#---State Functions---#
def followAction(file):
    if scenarioTrace:
        file.write('state= 1 Follow\n')
    stateCount[FOLLOW] = stateCount[FOLLOW] + 1

def pullOutAction(file):
    if scenarioTrace:
        file.write('state= 2 Pull out\n')
    stateCount[PULL_OUT] = stateCount[PULL_OUT] + 1

def accelerateAction(file):
    if scenarioTrace:
        file.write('state= 3 Accelerate\n')
    stateCount[ACCELERATE] = stateCount[ACCELERATE] + 1

def pullInAheadAction(file):
    if scenarioTrace:
        file.write('state= 4 Pull in ahead\n')
    stateCount[PULL_IN_AHEAD] = stateCount[PULL_IN_AHEAD] + 1

def pullInBehindAction(file):
    if scenarioTrace:
        file.write('state= 5 Pull in behind\n')
    stateCount[PULL_IN_BEHIND] = stateCount[PULL_IN_BEHIND] + 1

def decelerateAction(file):
    if scenarioTrace:
        file.write('state= 6 Decelerate\n')
    stateCount[DECELERATE] = stateCount[DECELERATE] + 1

def doneAction(file):
    if scenarioTrace:
        file.write('state= 7 Done\n\n')
    stateCount[DONE] = stateCount[DONE] + 1

# Function to calculate frequency based on counts and a sequence
def calculate_frequency(counts, sequence):
    total_count = sum(counts)
    frequencies = [count / total_count for count in counts]
    return [frequencies[i - 1] for i in sequence]

# Open the output file
with open(OUTPUT_FILE, 'w') as file:
    if scenarioTrace:
        file.write('CS 330 GS, State Machines, Begin: ')
        file.write(str(NOW))
        file.write('\n\n')

    # Execute iterations and transitions.
    for i in range(1, scenarioInterval+1):
        
        # Write the iteration number to the file if trace is true
        if scenarioTrace:
            file.write(f'iteration= {i}\n')

        # Initialize the default state to FOLLOW
        state = FOLLOW
        followAction(file)

        while state != DONE:

            # Get random number between 0 and 1
            R = random.uniform(0, 1)

            # Check transitions
            if state == FOLLOW:
                if R < transitionProbability[0]:
                    transitionCount[0] = transitionCount[0] + 1
                    state = PULL_OUT
                    pullOutAction(file)
                else:
                    state = FOLLOW
                    followAction(file)
            
            elif state == PULL_OUT:
                if R < transitionProbability[1]:
                    transitionCount[1] = transitionCount[1] + 1
                    state = ACCELERATE
                    accelerateAction(file)
                elif R < transitionProbability[1] + transitionProbability[3]:
                    transitionCount[3] = transitionCount[3] + 1
                    state = PULL_IN_BEHIND
                    pullInBehindAction(file)
                else:
                    state = PULL_OUT
                    pullOutAction(file)

            elif state == ACCELERATE:
                if R < transitionProbability[2]:
                    transitionCount[2] = transitionCount[2] + 1
                    state = PULL_IN_AHEAD
                    pullInAheadAction(file)
                elif R < transitionProbability[2] + transitionProbability[4]:
                    transitionCount[4] = transitionCount[4] + 1
                    state = PULL_IN_BEHIND
                    pullInBehindAction(file)
                elif R < transitionProbability[2] + transitionProbability[4] + transitionProbability[5]:
                    transitionCount[5] = transitionCount[5] + 1
                    state = DECELERATE
                    decelerateAction(file)
                else:
                    state = ACCELERATE
                    accelerateAction(file)
            
            elif state == PULL_IN_AHEAD:
                if R < transitionProbability[8]:
                    transitionCount[8] = transitionCount[8] + 1
                    state = DONE
                    doneAction(file)
                else:
                    state = PULL_IN_AHEAD
                    pullInAheadAction(file)
            
            elif state == PULL_IN_BEHIND:
                if R < transitionProbability[6]:
                    transitionCount[6] = transitionCount[6] + 1
                    state = FOLLOW
                    followAction(file)
                else:
                    state = PULL_IN_BEHIND
                    pullInBehindAction(file)

            elif state == DECELERATE:
                if R < transitionProbability[7]:
                    transitionCount[7] = transitionCount[7] + 1
                    state = PULL_IN_BEHIND
                    pullInBehindAction(file)
                else:
                    state = DECELERATE
                    decelerateAction
            
            elif state == DONE:
                print('Error, unexpected state value=' + str(state), '\n')
                break
            else:
                print('Error, unexpected state value=' + str(state), '\n')
                break

    # Calculate state and transition frequencies
    stateFrequency = calculate_frequency(stateCount, stateSequence)
    transitionFrequency = calculate_frequency(transitionCount, transitionSequence)
    
    file.write(f'scenario= {SCENARIO} \n')
    file.write(f'trace= {scenarioTrace} \n')
    file.write(f'iterations= {scenarioInterval} \n')
    file.write(f'transition probabilities= {transitionProbability} \n')
    file.write(f'state counts= {stateCount} \n')
    file.write(f'state frequency= {[round(freq, 3) for freq in stateFrequency]} \n')
    file.write(f'transition counts= {transitionCount} \n')
    file.write(f'transition frequency= {[round(freq, 3) for freq in transitionFrequency]} \n')
    file.write('\n\n')
    file.write('CS 330 GS, State Machines, End: ')
    file.write(str(NOW))

    file.close()
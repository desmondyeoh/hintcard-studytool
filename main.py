MISSING_RATE = 0.5
WORD_MIN_LEN = 4

DATA = """
Explain two main reasons why use AI to play games in both player and non-player role. Give example games for each reason
---
1. Playing to win

 Achieve as high a performance as possible
 Getting high score, winning over opponent, surviving a long time or similar
 Not always possible to define high performance, example The Sims, minecraft
 Example: Board games AI (TD-Gammon, Chinook, Deep Blue, AlphaGo), Jeopardy
(Watson), Starcraft (AlphaStar), Dota2 (OpenAI)

2. Playing for experience
 Not all player playing to win
 Act as adversary, provides assistance, emotively expressive, tells a story
 Agent play in human-like manner, entertaining or behave predictably
 Simulation-based testing or Game demonstration
 Example: Game Turing Test (2kBot Prize/Mario), Persona Modeling

===

What are the reasons to use AI that plays in the player role to win?
---
1. Most common in academic setting, where AI assume the role of player to win in order to
test capabilities and performance of AI algorithms. – Resulting AI program beating best
human player, example Deep Blue in chess, DeepMind’s Alpha Go in Go, IBM Watson in
Jeopardy
2. Games are made to test human intelligence, exercise cognitive abilities, offer gradual skill
progression that test AI at different capability levels
3. Need strong AI to provide challenge to players such as classic board games
4. Test games whether game or level is playable, called simulation-based testing
===
Non-player characters (NPC) are often designed not to offer maximum challenge but instead to be
entertaining or human like. However, there are cases where we want NPC to play as well as
possible. What are the example games of such cases?
---
 Example: Civilization needs high performing non-cheating opponents.
 Example: strategy games such as EXCOM: Enemy Unknown
 Example: Racing game, use Rubber band AI to control NPC cars to adapt their speed to
human player so they are never too far behind of ahead. The performance of the
controller can be reduced when necessary to match player’s performance
===
Why would we like to design human-like agent that plays a game in the player role but does not focus on winning?
---
1. Simulation-based testing

 Used to automatically evaluate game content generated either manually or
automatically by letting the human-like agent plays it.
 Important agent plays like human-like manner, comparable performance to
human, similar reaction speed, makes mistakes like human, curious and explores
the same areas as human, etc.

2. Demonstrate how to play a level to a human player
 Demo mode which shows game in action, example Super Mario Bros
 If player repeatedly fail to play a level, the game takes control and plays for you
for 10 to 20 seconds and lets you continue afterwards.
 If some parts of game are procedurally generated, the game needs to generate
these demonstration itself
===
What are the obvious signs of non-humanness that recur across games for many types of AI agents?
---
 Extremely fast reactions
 Switching between actions faster than a human could
 Not attempting actions which fail
 Not doing unnecessary actions
 Not hesitating or stopping to think
===
What are the desirable features game designer look for when designing non-player characters (NPC) that play for experience in the non-player role?
---
 Illusion of intelligence

 Player believe that NPC is intelligent even though the code controlling it is very
simple
 Predictability
 Player memorize and predict regularities of guards
 Petrols are regular and can be gleaned by the player
 Boss monsters repeat certain movement in sequence
 Not too “intelligent” or adaptive
 Is boring and unsportsmanlike
 Example: neuroevolution provides a solution that was extremely boring, keep
defensive and use long range attack on incoming units
 “camping” – staying stationary in protected position and waiting for player to
expose them, effective in military tactic but not fun
 In FIFA 99, best way to score goal is forcing a penalty kick
===
Characteristics of a game have impact on the potential use of AI methods. What are the five characteristics of games?
---
 Number of players
 Stochasticity
 Observability
 Action space and branching factor
 Time granularity
===
For a single player game with predictable environment, what algorithm is suitable to play the game?
---
Single agent-tree search algorithms based on Markov property (next state is entirely determined by previous state and action taken at the point)
===
For a two-player zero-sum adversarial like chess where one player win and another lose, what algorithm is suitable to play the game?
---
Minimax algorithm (with or without α-β pruning)
===
Why tree-search and reinforcement learning might not be suitable for game with high stochasticity like ms pacman or Starcraft?
---
 Tree search,
     Cannot be sure the states that sequence of actions will lead to which might affect
    the result.
     Increase base computational complexity
 Reinforcement learning
     Reduced certainty of how good/bad a policy is
     Need to evaluate policy multiple times which increase computational cost
===
How can AI play a game with hidden information (partial observability) such as card games and strategy games?
---
 Simplest approach is to ignore the hidden information, just feed agent with available action and decide action. For example Super Mario Bros
 For strategy games like Starcraft, involves active information gathering
 Model the hidden information including opponents’ play
===
Suppose you are an AI designer for a game. What are the characteristics of AI algorithm design that you must consider?
---
 How is the game state represented?
 Is there a forward model?
 Do you have time to train?
 How many games are you playing?
===
How can game state represented to an algorithm playing a racing car game?
---
 First-person view out of the windscreen car rendered in 3D
 An overhead view of the track rendering the track and various cars in 2D
 A list of positions and velocities of all cars on the track in the frame of reference of the
track
===
Why using unprocessed visual feed – i.e., tens of thousands of pixel values as input representation is not recommended?
---
 Finding a decent policy is much harder
 Policy search space vastly greater
 Proportion of search space that corresponds to decently-performing policies is likely
much smaller as many more nonsensical policies are possible
 Requires a learned visual system of some kind to drive well
===
What motivates researchers to use full visual feeds (i.e., full pixels input) as input representation?
---
 Giving the AI same conditions as a human would have
 Algorithm to play game “out of the box” without any API or additional engineering to
expose internal state of the game
 To develop game-independent algorithms
===
A very important factor when designing an AI to play game is the availability of a simulator of
the game called the forward model. Briefly explain the forward model and how to construct
it?
---
 A model which given a state s and an action a, reaches the same state s’ as the real game
would reach if it was given a at s.
 Game simulation – multiple actions can be explored before taking it in real game
 Necessary to use tree search-based approaches
 Must be fast – a thousand or hundreds of thousands times faster than real time
 Easy to construct for classic board games such as Chess and Go as game state is simply
the board state and rules are very easy to encode
 For other games, copy the same code that controls the game but without waiting for user
input and displaying graphics and calculations involved in graphic rendering.
 For classic 8-bit or 16-bit arcade games, run them inside emulators that can replace
graphics routines with dummy code
 Impossible to extract for other games as source code not available, or core control loops
closely tied up with user interface management, rendering, animation and network code.
For high computational core game loop, more practical to build/learn a simplified or
approximate forward model where resulting state not guaranteed to be identical to
actual game
===
List down several planning-based approaches that can be used to play games
---
 Classic tree search
 Stochastic tree search
 Evolutionary planning
 Planning with symbolic representation
===
What are the characteristics and requirements of a game that allow us to use classic tree
search methods for planning a move?
---
 Full observability
 Low branching factor
 Fast forward model
===
What is the most common use of A* algorithm in games?
---
 Navigation / Path-planning / path finding in physical space
===
Why Monte Carlo Tree Search (MCTS) is a better search than adversarial search in Go game?
---
 Go has a high branching factor (much higher than chess)
 Hard to algorithmically judge the value of a board state
 MCTS build an imbalanced trees where not all moves need to be explored to the same
depth which reduces effective branching factor
 MCTS also do random rollouts until the end of the game which reduces the need of state
evaluation
===
How can we use evolutionary planning to play games? In which situation that evolutionary
planning performs well?
---
 Instead of searching for sequence of actions starting from an initial point, we can optimize
the whole action sequence.
 Search the space of complete action sequences for those that have maximum utility
 Evaluating the utility by taking all the actions in the sequence in simulation and observe
the value of the state reached after taking those actions
 Handles well very large branching factors as in games with multiple independent units
such as in Hero Academy turn-based strategy game.
===
Discuss the limitations of reinforcement learning algorithm that learns to play a game.
---
 Lack of good function approximators for value function (e.g., the Q function)
 Q function requires all state value or {state, action} values that are stored separately, for
example in a table.
 For most game too many many states (billions) to be stored and most of these state are
never visited
 Too big to store in memory
 Use temporal difference – learn value using neighboring states, reduces state storage
 Use a compressed representation of value function i.e., function approximator such as
neural network
 Neural network and temporal difference have “catastrophic forgetting” learn degenerate
strategies and unlearn sophisticated strategies
 Sparse reward
 When same reward is encountered for a long time, BP algorithm will only output that
value for any state (similar to training long term on a single training example)
===
Discuss the use of evolutionary reinforcement learning to play games.
---
 Use evolutionary algorithms to evolve weights and/or topology of neural networks
(neuroevolution) or programs structured as expression trees (genetic programming)
 Fitness evaluation by using neural network to play game and using result as fitness
function
 John Koza used evolving programs to play pacman in 1992
 Around 2005, car racing, first-person shooters, strategy games, real-time strategy games
and classic arcade games such as Pacman
 Extremely versatile, can be applied to wide range of games in several different ways for
each game.
 Egocentric inputs are generally strongly preferred
 Works best when states can be represented using few dimensions (fewer than 50 unit of
neural network input layer)
 Suffers from curse of dimensionality
===
How can we use supervised learning to play games?
---
 Record traces of human players playing a game and train some function approximator to
behave like the human player
 Traces are store as list of tuples <features, target> where features represent the game
state and target is the action of the human in that state
 Instead of predict action, can also predict states value, then use function approximator
with search algorithm to play the game
===
What games can AI play? For each game, give 2 game example, the characteristics of the
games and AI techniques that can be used to play them
---
 Board games
	 Chess, Go,
	 Discrete state representation, deterministic and no reaction skills required
	 Adversarial planning, tree search, minimax, MCTS, reinforcement learning
 Card games
	 Texas hold ‘em, Poker
	 Hidden information, opponent card unknown to each other
	 Reinforcement learning-like methods such as Counterfactual Regret Minimization
	(CFR), DeepStack
 Classic arcade games
	 Pacman, Super Mario Bros, Atari2600
	 Fast reactions and precise timing, predict other entities behavior or trajectory,
	navigating mazes
	 Search 1 step head + state evaluator based on evolved neural network, MCTS,
	reinforcement learning, evolved neural network / neural networks
 Strategy games
	 Starcraft, Age of Empires
	 Controls multiple units, conquest or conflict, turn-based and real-time, high
	branching factor
	 MCTS variant based on decomposition through Naïve sampling, online
	evolutionary planning, evolution (NEAT)
 Racing games
	 Forza motorsport, Real racing
	 Continuous steering input signal, control position of vehicle and adjust
	acceleration or braking, manage fuels, damage or speed boosts, manage/block
	overtaking
	 Neuroevolution, competitive co-evolution, fuzzy logic, supervised learning, hand-
	coded rule-based
 Shooters and other first person games
	 Unreal Tournament 2004, VizDoom
	 Fast-paced game where speed perception and reaction is crucial, movement in
	complex three-dimensional environment, predicting actions and locations of
	multiple adversaries, sometimes team-based collaboration
	 Neuroevolution, deep reinforcement learning
 Serious games
	 Minecraft, Dragonbox
	 Involves a particular set of learning objectives, educational, soft skill training,
	have NPC that should behave believable, human-like, social and expressive
	 Use theoretical cognitive model such as OCC model
 Interactive fiction
	 Zork, Facade
	 Use text commands to play game, natural language processing
	 Z-machine, Long short-term memory (LSTM) networks + deep Q network
"""


def main():
    qnas = [[y.strip() for y in x.split('---')] for x in DATA.split('===')]
    
    import random
    import re

    random.shuffle(qnas)

    for qi in range(len(qnas)):
        print('\n[Question %d / %d]' % ((qi+1), len(qnas)))
        q = qnas[qi][0]
        a = qnas[qi][1]
        ca = a

        matches = re.findall(r"\w+(?:-\w+)*", a) # match english words, incl. those with hypthens
        matches = [x for x in matches if len(x) >= WORD_MIN_LEN] # only those words with at least WORD_MIN_LEN long
        random.shuffle(matches)
        hiddens = matches[:int(MISSING_RATE * len(matches))]

        for i, hidden in enumerate(hiddens):
            a = re.sub(r"\b"+hidden+r"\b", '*'*len(hidden), a)

        print(q)
        input('hint >')
        print('---')
        print(a)
        input('ans >')

        print(ca)
        input('next question >')


if __name__ == '__main__':
    main()

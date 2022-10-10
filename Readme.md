# Welcome to the Chess.com agent!

This project consists of a very simple chess agent that plays on [Chess.com](chess.com). All you need to do is initialize the python project and it'll start playing by itself. It plays using a min-max strategy of depth 3 (So it won't play very well).

## Dependencies

In order to run the project you'll need to install the dependecies listed in the `dependencies` file. To do this, all you need to do is run the following command in your shell: `pip3 install -r dependencies`.

## How it interacts with Chess.com

This project uses [Selenium](https://www.selenium.dev) to interact with the [Chess.com](chess.com) website. Selenium provides multiple tools to find HTML elements and act upon them, you can review the Selenium docs to gain deeper understanding of how it works, yet you can also review the `agent.py` file, which contians such interactions. Function names are very descriptive and logs are written in there so you can see what is happening and when.

The whole process goes something like this:

1. The agent is initialized and opens a new window in chess.com.
2. The agent selects to play a match as a guest in the begginer level (or the difficulty level you choose in the `settings.py` file).
3. While the match is running it does the following every turn: read the board, pass it on to the chess engine (the minmax algorithm), and play the move returned by the engine.
4. Once the match ends, it clicks "play again" and the process is repeated.

## The Min Max algorithm

In this case the min max algorithm for our chess agent is quite simple, and it doesn't consider turning pawns into queens.
This engine does the following things:

- It evaluates a move based on the status of the board the next turn. The evaluation consists on counting how many points each player has based on the active pieces (e.g. pawns are worht 1 point, bishop is worth 3 points, queen 9, etc).
- It builds the tree of possible boards with every possible legal move and then it does the same within every possible board obtained before (meaning, building a tree of depth 3).
- It chooses the move associated with the leaf of maximum impact or less damage.

## Future improvements

Some future improvements which could be added to this project could be:

- Consider Queening (turning pawns into queens).
- Pruning worthless (or very risky) paths in the minmax tree (To avoid blunders and sacrifices without purpose).
- Use other AI techiques for the AI engine (possible a forest or a neural network).

## Resources

- [About AlphaZero](https://towardsdatascience.com/alphazero-chess-how-it-works-what-sets-it-apart-and-what-it-can-tell-us-4ab3d2d08867#:~:text=In%20short%2C%20AlphaZero%20is%20a,the%20rules%20of%20said%20games)
- [Monte Carlo Tree Search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
- [Selenium](https://www.selenium.dev)
- [Chess library](https://pypi.org/project/chess/)
- [Anatomy of a Chess AI](https://medium.com/@SereneBiologist/the-anatomy-of-a-chess-ai-2087d0d565)
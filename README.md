# LaTeX to Canvas

LaTeX is a beautiful tool which allows you to create visually appealing mathmatical equations.  This format, however does not always render properly, especially in markdown and HTML.  Github ahs provided a solution for this problem, but it if you already have a repo or document with LaTeX in it, it can take some time to make the changes.

#### without the correct formatting a LaTeX equation woul look like this:
> $$ P(A|B) = \dfrac{P(A \cap B)}{P(B)}$$

#### after running the script in the repo folder the result is this:

> <img src="https://render.githubusercontent.com/render/math?math=P(A|B) =\dfrac{P(A \cap B)}{P(B)}">

This script was designed to make this process a bit simpler.  When run in a repo, the script will edit the README.md and make the changes to each equation.  Searching for the `$$` or `$` wrappers, `latex-to-canvas` will modify each component and wrap it in the necassary HTML tags with the GitHub `render.githubusercontent` format which turns the equation into an image for rendering.

The script was developed specifically for use with the Canvas LTI, but can be adapted for other uses.

# Usage

from within the folder of the repo you wish to change, simply run `python ~/PATH/latex-to-canvas.py <lesson number>'

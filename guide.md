# Using Music Blocks

Music Blocks is a fork of [Turtle
Blocks](href="https://turtle.sugarlabs.org). It has extensions for
exploring music: pitch and rhythm.

Music Blocks is designed to run in a browser. Most of the development
has been done in Chrome.

| Browser | Comments                  |
| ------- | ------------------------- |
| Chrome  | Supported                 |
| Safari  | Supported                 |
| Firefox | Supported                 |
| Opera   | Supported                 |
| IE      | Not supported             |
| Edge    | Recent versions supported |

You can run it from
[https://musicblocks.sugarlabs.org](https://musicblocks.sugarlabs.org).

![alt tag](./getting-started.png "Music Blocks in a browser")

## <a>TABLE OF CONTENTS</a>

1. [Getting Started](#1-getting-started)
2. [Toolbars](#2-toolbars)
   1. [Main Toolbar](#1-main-toolbar)
   2. [Secondary Toolbar](#2-secondary-toolbar)
3. [Context Menus](#3-context-menus)
   1. [Contextual Menu for Blocks](#1-contextual-menu-for-blocks)
   2. [Contextual Menu for Background](#2-contextual-menu-for-background)
   3. [Pie Menus](#3-pie-menus)
4. [Keyboard Shortcuts Guide](#4-keyboard-shortcuts-guide)
   1. [General Shortcuts](#1-general-shortcuts)
   2. [Navigation Shortcuts](#2-navigation-shortcuts)
   3. [Music Note Creation](#3-music-note-creation)
   4. [Special Block Manipulations](#4-special-block-manipulations)
5. [Block Palettes](#5-block-palettes)
   1. [Defining a Note](#1-defining-a-note)
   2. [A Quick Tour of Selected Blocks](#2-a-quick-tour-of-selected-blocks)
6. [Flow Palette](#6-flow-palette)
7. [Widget Palette](#7-widget-palette)
8. [Stats](#8-stats)
9. [Planet View](#9-planet-view)

## <a>1. Getting Started</a>

[Back to Table of Contents](#table-of-contents)

![Default blocks](./getting_started_blocks.svg "default blocks")

When you first launch Music Blocks in your browser, you'll see a stack
of blocks representing the notes: `Sol 4`, `Mi 4`and `Sol 4`. The first two notes are `1/4` note; third note is
`1/2` note. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1731947644713000&run=True)

![The Play button](./play.png "play button")

Try clicking on the _Start_ block or click on the _Play_ button. You
should hear the notes play in succession: `Sol` `Mi` `Sol`.

To write your own programs, drag blocks from their respective palettes
on the left side of the screen. Use multiple blocks in stack(s) to
create music and drawings; as the mouse moves under your control,
colorful lines are drawn and music of your creation is played.

Note that blocks either snap together vertically or
horizontally. Vertical connections indicate program (and temporal)
flow. Code is executed from the top to bottom of a stack of
blocks. Horizontal connections are used for parameters and arguments,
e.g., the name of a pitch, the duration of a note, the numerator and
denominator of a division. From the shape of the block, it should be
apparent whether they connect vertically or horizontally.

Some blocks, referred to as "clamp" blocks have an
interior&mdash;child&mdash;flow. This might be code that is run _if_ a
condition is true, or, more common, the code that is run over the
duration of a note.

For the most part, any combination of blocks will run (although there
is no guarantee that they will produce music). Illegal combinations
of blocks will be flag by a warning on the screen as the program runs.

You can delete a block by dragging it back into the trash area that
appear at the bottom of the screen.

To maximize screen real estate, Music Blocks overlays the program
elements (stacks of blocks) on top of the canvas. These blocks can be
hidden at any time while running the program.

## <a>2. Toolbars</a>

[Back to Table of Contents](#table-of-contents)

There are five toolbars in Music Blocks, each serving a specific purpose to help you navigate and interact with the application. Below is a detailed description of each toolbar along with images to visually illustrate their functions:

### 1. Main Toolbar

The **Main** toolbar is located across the top of the screen. It contains several essential buttons for managing your project, controlling playback, and accessing various settings.

- **Play Button**: Starts playing the project.
- **Stop Button**: Stops the current project playback.
- **Fullscreen Button**: Toggles fullscreen mode on or off.
- **New Project Button**: Creates a new project from scratch.
- **Load Project from File Button**: Opens an existing project file.
- **Save Project Button**: Saves the current project.
- **Find and Share Project Button**: Opens the Planet view where you can explore and share projects with the community.
- **Auxiliary Menu**: Provides additional tools for project settings and configuration.
- **Help Button**: Opens the help menu, providing access to instructions and guidance.

---

### 2. Secondary Toolbar

The **Secondary** toolbar appears when you click the **hamburger button** (three horizontal lines) in the main toolbar. This toolbar provides several options to control the execution of your project and adjust your work environment.

- **Run Slowly**: Executes the program slowly to allow you to follow the process step by step.
- **Run Step by Step**: Runs the program one step at a time, ideal for debugging and analysis.
- **Change theme**: Switch between light and dark mode for a customized workspace.
- **Merge with Current Project**: Combines the current project with another, promoting collaboration and reusability.
- **Turtle Wrap**: Enables wrapping of the turtle's position to seamlessly continue from the opposite edge of the canvas.
- **Set Pitch Preview**: Lets users preview pitches while composing, providing instant feedback.
- **Restore**: Resets changes and restores the project to its last saved state
- **Switch to Advanced Mode**: Quickly transition from Beginner to Advanced mode for more tools and customization options.
  <h4>These are the extra options you get when you access the advanced mode:</h4> 1. _Display Statistics_: Provides insights into project performance, such as usage and execution metrics.<br> 2. _Load Plugin_: Integrates external plugins to enhance functionality and extend features.<br> 3. _Delete Plugin_: Allows the removal of plugins that are no longer needed.<br> 4. _Horizontal Scrolling_: Enables horizontal navigation for easier handling of large projects.<br> 5. _JavaScript Editor_: Includes an editor for writing and embedding custom JavaScript code.<br> 6. _Record_: Adds a "Record" button to the main palette, enabling users to record their compositions directly (Not supported on Firefox and Safari browsers).

- **Select Language**: Offers a multilingual interface, allowing users to change the language as per their preference.

---

### 3. Palette Toolbar

The **Palette** toolbar is located on the left side of the screen. It contains various categories of blocks, such as numbers, media, and actions, which you can drag and drop onto the canvas to build your project.

The palette is dynamic, switching between different categories based on your selection. When you hover over the palette, it reveals the specific blocks related to your chosen category.

---

### 4. Canvas Toolbar (Upper Right)

On the upper right of the canvas is a small toolbar with options for managing the workspace. It allows you to adjust the display and clear the canvas.

- **Show Grids**: Displays a grid overlay on the canvas for alignment and organization.
- **Clear Screen**: Clears the entire canvas, removing all blocks and drawings.
- **Toggle Display Size**: Adjusts the size of the canvas or blocks for a better viewing experience.

---

### 5. Canvas Toolbar (Lower Right)

Located at the lower right of the canvas, this small toolbar provides additional control over block visibility and size.

- **Home Button**: Takes you back to the initial view or project start screen.
- **Show/Hide Blocks**: Toggles the visibility of the blocks you’ve added to the canvas.
- **Expand/Collapse Blocks**: Allows you to expand or collapse the view of blocks for better organization.
- **Decrease/Increase Block Size**: Changes the size of the blocks on the canvas to suit your preference.

---

## <a>3. Context Menus</a>

[Back to Table of Contents](#table-of-contents)

Context menus are an important part of user interfaces that provide users with quick access to a set of actions relevant to the context in which they are working.The right-click context menu in Music Blocks provides several options for working with blocks and the workspace. To access the right-click context menu, simply right-click anywhere in the workspace.

### <a>1. Contextual Menu for Blocks:</a>

When you **right-click on a block**, the following options are available:

![Right-click context menu](./block_context.png "Right-click context menu")

**Extract**: The Extract option allows you to break down a nested block into its individual components or sub-blocks. This is useful for isolating parts of a block that you want to modify or reuse in other sections of your project, without affecting the original structure. It simplifies the process of working with complex, multi-layered blocks.

![Extract the selected block](./extract.png "Extract the selected block")

**Move to Trash**: The Move to Trash option deletes the selected block by sending it to the trash. This action removes the block from your workspace, is a way of cleaning up the environment or removing blocks you no longer need.

![Delete](./delete.png "Delete")

**Duplicate**: The Duplicate option creates an exact copy of the selected block. This is especially helpful for reusing blocks with the same configurations or settings in multiple places in your project, saving time and effort in recreating similar blocks.

![Duplicate](./duplicate.png "Duplicate")

**Help**: The Help option displays a detailed help screen for the selected block. This screen provides valuable information about the block’s functionality, purpose, and usage instructions, making it easier for users to understand and effectively incorporate the block into their projects. Additionally, the help screen allows you to insert blocks from the help examples directly into your program by clicking on the download icon (labeled "Load this block" in the image below).

![Help](./help.png "Help")

**Close**: The Close option exits the context menu, allowing you to return to your workspace without making any changes or selections. This is useful for dismissing the menu if you opened it by mistake or decided not to perform any action.

By using the right-click context menu in Music Blocks, you can quickly perform common tasks and manipulate blocks on the workspace. This can help you to work more efficiently and effectively in your projects.

### <a>2. Contextual Menu for Background:</a>

When you **right-click on the background**, the following options are available:

![Context-Menu-For-Workspace](./context-menu-workspace.png "Context Menu for Workspace")

- **Grid**: Toggles the display of a grid in the workspace for better alignment and organization.
- **Set Pitch Preview**: Adjusts and previews pitches while working on a composition.
- **Enable Horizontal Scrolling**: Allows horizontal navigation for easier management of large projects.
- **Turtle Wrap Off**: Toggles the turtle wrap feature, which determines whether the turtle wraps around the canvas edges.
- **Restore**: Reverts the workspace to its last saved state.
- **Increase Block Size**: Enlarges the size of all blocks for better visibility.
- **Decrease Block Size**: Shrinks the size of all blocks to save space.
- **Expand/Collapse Block**: Expands or collapses individual blocks to show or hide their details.
- **Show/Hide Block**: Toggles the visibility of selected blocks in the workspace.
- **Home**: Centers the workspace view on the initial starting point.
- **Close**: Exits the contextual menu.
- **Search for Blocks**: Opens a search bar to locate specific blocks within the workspace.
- **Collapse**: Collapses all blocks to their minimal state.
- **Clean**: Organizes and tidies up the workspace by aligning blocks systematically.
- **Select**: Enables selection mode for selecting multiple blocks or elements in the workspace.

### <a>3. Pie Menus </a>

Many blocks in Music Blocks also feature "pie menus" that allow you to change block parameters quickly by selecting options from a circular menu that appears when you hover over the block.

For further details on how to use these toolbars effectively, you can refer to the [Turtle Blocks Documentation](https://github.com/sugarlabs/turtleblocksjs/tree/master/documentation).

---

## 4. Keyboard Shortcuts Guide

[Back to Table of Contents](#table-of-contents)

### 1. General Shortcuts

| Key Combination (Windows) | Key Combination (Mac)    | Description                                                  |
| ------------------------- | ------------------------ | ------------------------------------------------------------ |
| `Alt + B`                 | `Option + B`             | Save the current block artwork.                              |
| `Alt + C`                 | `Option + C`             | Copy the selected blocks.                                    |
| `Alt + E`                 | `Option + E`             | Clear all elements.                                          |
| `Alt + R` or `Enter`      | `Option + R` or `Return` | Play the project. Activates the play button.                 |
| `Alt + S`                 | `Option + S`             | Stop all running processes (e.g., turtles).                  |
| `Alt + H`                 | `Option + H`             | Save help blocks - Generate and save artwork for each block. |
| `Ctrl + V`                | `Command + V`            | Open the paste box.                                          |
| `Space`                   | `Space`                  | Toggle the zoom level of the stage.                          |
| `ESC`                     | `ESC`                    | Hide widgets or stop ongoing processes.                      |

### 2. Navigation Shortcuts

| Key (Windows) | Key (Mac)          | Description                                                 |
| ------------- | ------------------ | ----------------------------------------------------------- |
| `HOME`        | `Fn + Left Arrow`  | Jump to the home position for blocks or palettes.           |
| `END`         | `Fn + Right Arrow` | Scroll to the bottom of the page.                           |
| `PAGE UP`     | `Fn + Up Arrow`    | Scroll up by half the screen height.                        |
| `PAGE DOWN`   | `Fn + Down Arrow`  | Scroll down by half the screen height.                      |
| `Arrow Up`    | `Arrow Up`         | Move the active block or scroll up.                         |
| `Arrow Down`  | `Arrow Down`       | Move the active block or scroll down.                       |
| `Arrow Left`  | `Arrow Left`       | Move the active block or scroll left (In Horizontal mode).  |
| `Arrow Right` | `Arrow Right`      | Move the active block or scroll right (In Horizontal mode). |

### 3. Music Note Creation

| Key (Windows) | Key (Mac) | Description          |
| ------------- | --------- | -------------------- |
| `D`           | `D`       | Create a "Do" note.  |
| `R`           | `R`       | Create a "Re" note.  |
| `M`           | `M`       | Create a "Mi" note.  |
| `F`           | `F`       | Create a "Fa" note.  |
| `S`           | `S`       | Create a "Sol" note. |
| `L`           | `L`       | Create a "La" note.  |
| `T`           | `T`       | Create a "Ti" note.  |

### 4. Special Block Manipulations

| Key (Windows) | Key (Mac) | Description                                                |
| ------------- | --------- | ---------------------------------------------------------- |
| `/`           | `/`       | Scroll blocks container to the right (In Horizontal mode). |
| `\`           | `\`       | Scroll blocks container to the left (In Horizontal mode).  |
| `DEL`         | `Delete`  | Extract the selected block.                                |

## 5. Block Palettes

[Back to Table of Contents](#table-of-contents)

The block palettes are displayed on the left side of the screen. These
palettes contain the blocks used to create programs.

Looking for a block? Find it in the [Palette
Tables](https://github.com/sugarlabs/musicblocks/blob/master/guide/README.md#APPENDIX_1).

See the
[Turtle Blocks Programming Guide](http://github.com/sugarlabs/turtleblocksjs/tree/master/guide/README.md)
for general details on how to use the blocks.

See the
[Music Blocks Programming Guide](http://github.com/sugarlabs/musicblocks/tree/master/guide/README.md)
for details specific to music: _Rhythm_, _Meter_, _Pitch_, _Intervals_,
_Tone_, _Ornament_, _Volume_, _Drum_, and _Widget_.

All of the other palettes are described in the
[Turtle Blocks documentation pages](http://github.com/sugarlabs/turtleblocksjs/tree/master/documentation).

### 1. Defining a note

![The Note Block](./newnote_block.svg "the note")

At the heart of Music Blocks is the concept of a note. A note, defined
by the _Note value_ block defines a length of time and a set of
actions to occur in that time. Typically the action is to play a
pitch, or series of pitches (e.g., a chord). Whatever blocks are placed
inside the "clamp" of a _Note value_ block are played over the
duration of the note.

The duration of a note is determined by its note value. By default, we
use musical notation, referring to whole notes (`1`), half notes
(`1/2`), quarter notes (`1/4`), etc., but you can use any number as
the note duration. (There are some practical limitations, which you
can discover through experimentation.) The relative length of a
quarter note is half as long as a half note. By default, Music Blocks
will play 90 quarter notes per second, so each quarter note is `2/3`
seconds (`666` microseconds) in duration.

The _Pitch_ block (found on the Pitch Palette) is used to specify the
pitch of a note. By default, we use traditional western Solfege, i.e.,
`Do`, `Re`, `Mi`, `Fa`, `Sol`, `La`, `Ti`, where `Do` is mapped to
`C`, `Re` is mapped to `D`, etc. (when the key and mode are `C
Major`). You can also specify pitch by using a note name, e.g.,
`F#`. An octave specification is also required (as an argument for our
pitch block) and changes integers for every cycle of `C` (i.e. `C4` is
higher than B3). When used with the _Pitch-time Matrix_ block, a row
is created for each _Pitch_ block.

In addition to specifying the note name, you must also specify an
octave. The frequency of a note doubles as the octave increases. `A2` is
`110 Hertz`; `A3` is `220 Hertz`; `A4` is `440 Hertz`; etc.

Two special blocks can be used with a _Pitch_ block to specify the
name of the pitch: the _Solfege_ block and the _Pitch-Name_ block. The
_Solfege_ block uses selectors to scroll through `Do`, `Re`, `Mi`,
`Fa`, `Sol`, `La`, and `Ti`. A second selector is used for sharps and
flats: `##`, `#`, `and`. The _Pitch-Name_ block is similar
in that it lets you scroll through `C`, `D`, `E`, `F`, `G`, `A`,
`B`. It also uses a second selector for sharps and flats.

As noted, and described in more detail in the
[Music Blocks Programming Guide](http://github.com/sugarlabs/musicblocks/tree/master/guide/README.md),
you can put as many _Pitch_ blocks inside a note as you'd like. They
will play together as a chord. You can also insert graphics blocks
inside a note in order to create sound-sync animations.

### 2. A quick tour of selected blocks

![The Set Instrument block](./settimbre_block.svg "Set instrument block")

The _Set instrument_ block, found on the _Tone_ palette, lets you choose a
timbre for a note. In the above example, a guitar model is used to
make any notes contained within the block's clamp will sound as if
they are being played on a guitar. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1731948356610795&run=True)

![The Set Volume block](./setsynthvolume_block.svg "Set synth volume")

The _Set synth volume_ block, found on the _Volume_ palette, lets you
change the volume, which ranges from `0` (silent) to `100` (full
volume), of any notes contained with the block's clamp.

![The Set Drum block](./setdrum_block.svg "Set drum block")

The _Set drum_ block, which is used inside of the clamp of a _Note
value_ block is used to add drum sounds to a note. It is found on the
_Drum_ palette. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732000719242159&run=True)

![The Repeat block](./repeat_block.svg "Repeat Block")

The _Repeat_ block, found on the _Flow_ palette, is used to create
loops. Whatever stack of blocks are placed inside its clamp will be
repeated. It can be used to repeat individual notes, or entire phrases
of music. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732003682836455&run=True)

![The Duplicate block](./duplicatenotes_block.svg "Duplicate Block")

The _Duplicate_ block, found on the _Rhythms_ palette, is used to
repeat any contained notes. Similar to using a _Repeat_ block, but
rather than repeating a sequence of notes multiple times, each note is
repeated in turn, e.g. duplicate x2 of `4 4 8` would result in `4 4 4
4 8 8`, where as repeat x2 of `4 4 8` would result in `4 4 8 4 4 8`. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732003870740637&run=True)

The _Start_ block, found on the _Action_ palette, is tied to the _Run_
button. Anything inside of the clamp of the _Start_ button will be run
when the button is pressed. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732004679481517&run=True)

![The Start block](./multiple_start_blocks.svg "Start Block")

Note that you can have multiple mice and that each mouse is
equivalent to a "voice" in music. It can play notes of various pitches
in sequence, and can even play multiple notes of the same "note
value", but no one mouse can do counterpoint by itself&mdash;just like
one mouse cannot draw two lines at the same time. If you want
counterpoint, pull out an additional _Start_ block, which will create
a new mouse that can now perform a new voice.

![The Action block](./action_block.svg "Action-Chunk")

The _Action_ block, also found on the _Action_ palette, is used to
create a collection of blocks that can be run as a group. Whenever you
create an _Action_ block, a new block corresponding to that action is
added to the palette. The name given to the action is the name
associated with the new block. (It is common practice to use _Action_
blocks to define short phrases of music that can be repeated and
modified.) [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732004679481517&run=True)

Actions are a powerful organizational element for your program and can
be used in many powerful ways, e.g., an action can be associated with
an event, such as an on beat or off beat or mouse click. See
[Music Blocks Programming Guide](http://github.com/sugarlabs/musicblocks/tree/master/guide/README.md),
for further details and examples.

![The Storein Box block](./storebox1_block.svg "Store in box & Add 1 to Block")

The _Store in_ block, found on the _Boxes_ palette, is used to store a
value. That value can be retrieved using the _Box_ block. The value
can be modified using the _Add one_ block. These blocks are the
typical way in which variables are stored and retrieved in Music
Blocks. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732020971700880&run=True)

![Forward](./forward_block.svg "Forward Block")

The _Forward_ block, found on the _Graphics/Mouse_ palette, is used to draw
straight lines. (Note that if this block is used inside of a _Note
value_ block&mdash;the line will be drawn as the note plays; otherwise
the line is drawn "instantly".) [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1730651293282088&run=True)

![Right](./left_block.svg "Right/Left Block")

The _Right/Left_ block, found on the _Graphics/Mouse_ palette, is used to rotate the
mouse heading. (Note that if this block is used inside of a _Note
value_ block&mdash;the heading will change as the note plays;
otherwise the heading is changed "instantly".) [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732023891064703&run=True)

![Pen Up](./mousebutton_block.svg "Pen up and Pen down Block")

The _Pen up_ and _Pen down_ blocks, found on the _Pen_ palette,
determine whether or not the mouse draws as it moves. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732030390164543&run=True)

![Set Shade](./setshade_block.svg "Set shade Block")

The _Set shade_ block, also found on the _Pen_ palette, is used to set
the lightness or darkness of the "ink" used in the mouse pen. `set
shade 0` is black. `set shade 100` is white. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732096229605656&run=True)

![Set Color](./setcolor_block.svg "Set color Block")

The _Set color_ block, also found on the _Pen_ palette, is used to set
the color of the "ink" used in the mouse pen. `set color 0` is
red. `set color 70` is blue. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732096675098636&run=True)

![Random](./random_block.svg "Random Block")

The _Random_ block, found on the _Numbers_ palette, is used to
generate a random number, because sometimes being unpredictable is
nice. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732097168390186&run=True)

![One of This or That](./oneOf_block.svg "One of this or that Block")

The _One of_ block, also found on the _Numbers_ palette, is used to
generate a binary choice, one of "this" or "that", because sometimes
being unpredictable is nice. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732113139904914&run=True)

![alt tag](./show_block.svg "Show media Block")

The _Show_ block, found on the _Media_ palette, is used to display
text and images. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732117445989018&run=True)

![Mouse Button](./mousebutton_block.svg "Mouse button Block")

The _Mouse button_ block, found on the _Sensors_ palette, returns true
if the mouse button is clicked. The mouse button block can be used to
create some interactivity in your program. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732030390164543&run=True)

![Cursor XY](./x_block.svg "Cursor x - Cursor y Block")

The _Cursor x_ and _Cursor y_ blocks, also found on the _Sensors_ palette, return the X and Y coordinates of the cursor. These blocks can also be used to create interactive programs.

![alt tag](./input_block.svg "Input Block")

Prompting the user for input is done with the _Input_ block. This
block will display a message with a prompt and open an input form at
the current position of the mouse. Program execution is paused until
the user types into the form and types RETURN (or Enter). The contents
of the input form are then transferred to _Input-value_ block. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732171497274793&run=True)

![Push](./push_block.svg "Push Block")

![Pop](./pop_block.svg "Pop Block")

The _Push_ and _Pop_ blocks, found on the _Heap_ palette, are used to
store and retrieve values on/from a first-in, last-out (FILO) programx
heap. There is a separate heap maintained for each _Start_ block. <!-- [RUN LIVE]() -->

![Get Value](./getDict_block.svg "Get value Block")

![Set Value](./setDict_block.svg "Set value Block")

The _Get value_ and _Set value_ blocks are found on the _Dictionary_
palette. They are used to get and set values in a dictionary
object. You can have as many key/value pairs as you'd like in the
dictionary and you can have as many dictionaries as you'd like as
well. There is also a built-in dictionary associated with each _Start_
block that has key/value pairs for parameters such as x, y, heading,
color, shade, grey, pen size, notes played, current pitch, pitch
number, and note value. <!-- [RUN LIVE]() -->

![Print](./print_block.svg "Print Block")

The _Print_ block, found on the _Extras_ palette, is used to print
messages during program execution. It is very useful as a debugging
tool and also as a means of adding lyrics to your music&mdash;think
karaoke. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732172483377262&run=True)

## 6. Flow Palette

[Back to Table of Contents](#table-of-contents)

The Flow palette is described in more detail in the [Turtle Blocks
documentation](http://github.com/sugarlabs/turtleblocksjs/tree/master/documentation). Here we review a few ways to approach taking different
actions on different beats.

The _Switch_ block will take the action defined in the _Case_ that
matches the argument passed to the _Switch_ block. In the figure
below, it will take a different action based on the beat value: "on
case 1 run action1", "on case 2, run action2", ..., "on case 4 run
action4". You can also define a default action. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732173207750796&run=True)

![Switch](./switch-on-beat.svg "Switch on Beat")

![Switch](./switch-actions.svg "Switch actions")

Another way to do the same thing is with the _Do_ block found on the
Action palette. In the figure below, we add the beat count to "action"
to create a series of strings: "action1", "action2", ...,
"action4". We then "do" that action. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732830205442211&run=True)

![Do](./do-actions.svg "Do actions")

## 7. Widget Palette

[Back to Table of Contents](#table-of-contents)

Music Blocks has various Widgets that can be used within Music Blocks
to enhance your experience. The _Pitch-time matrix_ is described here.

![Matrix](./widget.png "The Phrase Maker")

Many of the blocks on this palette are used to create a matrix of
"pitch" and "note value". The matrix is a convenient and intuitive way
for generating short musical gestures, which can be regenerated as a
"chunk of notes" that can be played back programmatically. Musicians
may find it helpful to think of the pitches within the pitch-time
matrix as being akin to a bellset in which notes may be added and
removed as desired. The "note value" representation acts as a
"rhythmic tablature" that should be readable by both those familiar
with the concepts of rhythm in music and those unfamiliar (but
familiar with math).

![Matrix](./matrix_block.svg "Pitch-time Matrix blocks")

_Pitch-time Matrix_ blocks clamp is used to define the matrix:
A row in the matrix is created for each _Pitch_ block and columns are
created for individual notes, which are created by using _Rhythm_
blocks, individual note blocks, or the _Tuplet_ block. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732180386380311&run=True)

![Rhythm](./rhythmruler2_block.svg "Rhythm block")

The _Rhythm_ block is used to specify a series of notes of the same
duration (e.g., three quarter notes or seven eighth notes). The number
of notes is the top argument; the bottom argument is the the note
duration, e.g., `1/1` for a whole note, `1/2` for a half note, `1/4`
for a quarter note, etc. (Recall that in traditional Western notation
all note values are (1) in powers of two, and are (2) in relation to
the "whole note", which is in turn (3) defined by tempo, or
beats&mdash;usually quarter notes&mdash;per minute) Each note is
represented by a column in the matrix. <!-- [RUN LIVE]() -->

Special ratios of the whole note can be created very easily with the
_Rhythm_ block by choosing an integer other than the traditional
"powers of two" that standard Western music notation affords us. For
example, putting a `1/5` into the argument for "note value" will
create a note value equal to "one fifth the durational length of a
whole note". This gives the user endless rhythmic possibilities.

As a convenience, blocks for the most common note values are also
provided (whole note through 64th note). They are automatically
converted into the corresponding _Rhythm_ blocks, which can be used to
create columns in the matrix.

If you would like multiple note values in a row, simply use the
_Repeat_ block clamp or _Duplicate_ block clamp.

![Tuplet](./tuplet4_block.svg "Simple Tuplet clamp block")

The _Tuplet_ block is how we create rhythms that do not fit into a
simple "power of two" rhythmic space. A tuplet, mathematically, is a
collection of notes that are scaled to map into a specified
duration. For example, if you would like to script/perform three
unique notes into the duration of a single quarter note you would use
the tuplet block. The _Tuplet_ block is able to calculate how many
notes you have inserted into the clamp and will generate the tuplet
accordingly (e.g. if you put three notes in, it will generate a
"triplet". We have designed the tuplet block to allow for any input of
note value, so the triplet can be three quarter notes, three eighth
notes, etc. This design choice allows for maximum flexibility) You can
mix and match _Rhythm_ and individual _Note_ blocks within a _Tuplet_
block to generate complex rhythms (e.g. two quarter notes plus an
eighth note is possible within the tuplet). Each note is represented
by a column in the matrix. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732191858479236&run=True)

Note: Each time you open the matrix, it tries to reconstruct the notes
marked from the previous matrix. If you modify the _Pitch_ and
_Rhythm_ blocks in the _Pitch-time Matrix_ clamp, Music Blocks will
try to make a corresponding change in the matrix.

Note: You can construct a matrix from a chuck of blocks by including
the chunk in the clamp of the _Pitch-time Marix_ block.

More details about all of the widgets are available in the
[Music Blocks Programming Guide](http://github.com/sugarlabs/musicblocks/tree/master/guide/README.md).

## 8. Stats

[Back to Table of Contents](#table-of-contents)

Project statistics are available from a button on the secondary
toolbar in advanced mode.

![Stats](./stats.svg "Stats Details")

## 9. Planet View

[Back to Table of Contents](#table-of-contents)

Music Blocks also provides a Planet view to find and share
projects. It has options to load project from file locally and make
new projects from scratch.

![Planet](./planet_view_icon.png "Planet button")

There are LOCAL and GLOBAL options to choose from. LOCAL lists the
projects saved on your local machine. GLOBAL lets you explore projects
shared by the community. You can filter these projects by tags such as
Art, Math, Interactive, Design, Game, etc.

Projects are shown with a thumbnail image and a title. To get more
details, click on thumbnail image. A short description is provided.

You can open a project in Music Blocks directly from the Planet or you
can download.

![Planet](./planet-3.png)

![Planet](./planet-4.png)

[Back to Table of Contents](#table-of-contents)

# Guide to Programming with Music Blocks

Music Blocks is a programming environment for children interested in
music and graphics. It expands upon Turtle Blocks by adding a
collection of features relating to pitch and rhythm.

The [Turtle Blocks
guide](https://github.com/sugarlabs/turtleblocksjs/blob/master/guide/README.md)
is a good place to start learning about the basics. In this guide, we
illustrate the musical features by walking the reader through numerous
examples.

The Music Blocks [basic documentation](../documentation/README.md) is
also a good resource.

And there is a short [Guide to Debugging](../Debugging.md) to help you
with your programming.

This guide details the many musical features of the language.

## <a name="TOC">TABLE OF CONTENTS</a>

1. [Getting Started](#1-getting-started)
2. [Making Sounds](#2-making-sounds)
   1. [Note Value Blocks](#21-note-value-blocks)
   2. [Pitch Blocks](#22-pitch-blocks)
   3. [Multiple pitches](#23-multiple-pitches)
   4. [Rests](#24-rests)
   5. [Drums](#25-drums)
3. [Programming with Music](#3-programming-with-music)
   1. [Actions](#31-actions)
   2. [Pitch Transformations](#32-pitch-transformations)
      1. [Step Pitch Block](#321-step-pitch-block)
      2. [Sharps and Flats](#322-sharps-and-flats)
      3. [Adjusting Transposition](#323-adjusting-transposition)
      4. [Summary of Pitch Movements](#324-summary-of-pitch-movements)
      5. [Set Key](#325-set-key)
      6. [Fixed and Movable Pitch Systems](#326-fixed-and-movable-pitch-systems)
      7. [Intervals](#327-intervals)
         1. [Absolute Intervals](#3271-absolute-intervals)
         2. [Ratio Intervals](#3272-ratio-intervals)
      8. [Chords](#328-chords)
      9. [Inversion](#329-inversion)
      10. [Converters](#3210-converters)
          1. [Y to Pitch](#32101-y-to-pitch)
          2. [Pitch converter](#32102-pitch-converter)
          3. [Number to Octave](#32103-number-to-octave)
          4. [Number to Pitch](#32104-number-to-pitch)
   3. [Note Value Transformations](#33-note-value-transformations)
      1. [Dotted Notes](#331-dotted-notes)
      2. [Speeding Up and Slowing Down Notes via Mathematical Operations](#332-speeding-up-and-slowing-down-notes-via-mathematical-operations)
      3. [Repeating Notes](#333-repeating-notes)
      4. [Swinging Notes and Tied Notes](#334-swinging-notes-and-tied-notes)
      5. [Beat](#335-beat)
      6. [Staccato and Slur Blocks](#336-staccato-and-slur)
      7. [Backwards](#337-backwards)
   4. [Other Transformations](#34-other-transformations)
      1. [Set Volume and Crescendo Blocks](#341-set-volume-and-crescendo)
      2. [Setting Instrument](#342-setting-instrument)
      3. [Setting Key and Mode](#343-setting-key-and-mode)
      4. [Vibrato, Tremelo, et al.](#344-vibrato-tremelo-et-al)
   5. [Voices](#35-voices)
   6. [Graphics](#36-adding-graphics)
   7. [Interactions](#37-interactions)
   8. [Ensemble](#38-ensemble)
4. [Widgets](#4-widgets)
   1. [Monitoring Status](#41-monitoring-status)
   2. [Generating groups of Notes](#42-generating-chunks-of-notes)
      1. [The Phrase Maker](#421-the-phrase-maker)
      2. [The Rhythm Block](#422-the-rhythm-block)
      3. [Creating Tuplets](#423-creating-tuplets)
      4. [What is a Tuplet?](#424-what-is-a-tuplet)
      5. [Using Individual Notes](#425-using-individual-notes)
      6. [Using a Scale of Pitches](#426-using-a-scale-of-pitches)
   3. [Generating Rhythms (or How to Make a Drum Machine)](#43-generating-rhythms)
   4. [Musical Modes](#44-musical-modes)
   5. [Changing Meter](#45-meters)
   6. [The Pitch-Drum Matrix](#46-the-pitch-drum-matrix)
   7. [Exploring Musical Proportions](#47-exploring-musical-proportions)
   8. [Generating Arbitrary Pitches](#48-generating-arbitrary-pitches)
   9. [Changing Tempo](#49-changing-tempo)
   10. [Creating Custom Timbres](#410-custom-timbres)
   11. [The Music Keyboard](#411-the-music-keyboard)
   12. [Changing Temperament](#412-changing-temperament)
   13. [The Oscilloscope](#413-the-oscilloscope)
   14. [The Sampler](#414-the-sampler)
   15. [Arpeggio](#415-arpeggio)
5. [Beyond Music Blocks](#5-beyond-music-blocks)
   1. [LilyPond (or How to Generate Sheet Music)](#51-lilypond)
   2. [Other Exports](#52-other-exports)
   3. [The JavaScript Editor](#53-the-javascript-editor)
6. [Appendix](#6-appendix)
   1. [Beginner Palette Tables](#61-beginner-palettes)
   2. [Advanced Palette Tables](#62-advanced-palettes)

Many of the examples given in the guide have links to code you can
run. Look for `RUN LIVE` links.

## <a name="#GETTING-STARTED">1. Getting Started</a>

[Back to Table of Contents](#table-of-contents) | [Next Section (2. Making Sounds)](#2-making-sounds)

Music Blocks is designed to run in a browser. Most of the development
has been done in Chrome, but it should also work in Firefox, Opera,
and some versions of Safari. You can run it from
[musicblocks.sugarlabs.org](https://musicblocks.sugarlabs.org), from
[github io](https://musicblocks.sugarlabs.org), or by
downloading a copy of the code and running a local copy directly from
the file system of your computer. (Note that when running locally, you
may have to use a local server to expose all of the features.)

This guide details the music-specific features of Music Blocks. You
may also be interested in the [Turtle Blocks
Guide](http://github.com/sugarlabs/turtleblocksjs/tree/master/guide),
which reviews many programming features common to both projects.

For more details on how to use Music Blocks, see [Using Music
Blocks](http://github.com/sugarlabs/musicblocks/tree/master/documentation).
For more details on how to use Turtle Blocks, see [Using Turtle Blocks
JS](http://github.com/sugarlabs/turtleblocksjs/tree/master/documentation).

## <a name="NOTES">2. Making Sounds</a>

[Previous Section (1. Getting Started)](#1-getting-started) | [Back to
Table of Contents](#table-of-contents) | [Next Section (3. Programming with
Music)](#3-programming-with-music)

Music Blocks incorporates many common elements of music, such as
[pitch](#22-pitch-blocks), [rhythm](#21-note-value-blocks),
[volume](#341-set-volume-and-crescendo), and, to some degree,
[timbre](#342-setting-instrument) and
[texture](#344-vibrato-tremelo-et-al).

### <a name="NOTE-VALUE">2.1 Note Value Blocks</a>

At the heart of Music Blocks is the _Note value_ block. The _Note
value_ block is a container for a [_Pitch_ block](#22-pitch-blocks) that
specifies the duration (note value) of the pitch.

![notes](./note1.svg "A single Note value block (top) and two consecutive Note valueblocks (bottom)")

At the top of the example above, a single (detached) _Note value_
block is shown. The `1/8` is value of the note, which is, in this
case, an eighth note.

At the bottom, two notes that are played consecutively are shown. They
are both `1/8` notes, making the duration of the entire sequence
`1/4`.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1726138873526815&run=True)

![notes](./note2.svg "A quarter note, a sixteenth note, and a half note Note value blocks")

In this example, different note values are shown. From top to bottom,
they are: `1/4` for an quarter note, `1/16` for a sixteenth note, and
`1/2` for a half note.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1726139143565736&run=True)

Note that any mathematical operations can be used as input to the
_Note value_.

![pie menu](./piemenu1.svg "A pie menu for selecting note values.")

As a convenience, a pie menu is used for selecting common note values.

![Rest Chart](../charts/NotationRestChart.svg "A chart of note values and their corresponding note value blocks")

Please refer to the above picture for a visual representation of note
values.

### <a name="PITCH">2.2 Pitch Blocks</a>

As we have seen, _Pitch_ blocks are used inside the
[_Note value_](#21-note-value-blocks) blocks. The _Pitch_ block specifies the
pitch name and pitch octave of a note that in combination determines
the frequency (and therefore pitch) at which the note is played.

![pitch block](./note3.svg "Specifying a pitch block's name and octave")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733100820296221&run=True)

There are many systems you can use to specify a _pitch_ block's name
and octave. Some examples are shown above.

The top _Pitch_ block is specified using a _Solfege_ block (`Sol` in
`Octave 4`), which contains the notes `Do Re Me Fa Sol La Ti `.

The pitch of the next block is specified using a _Pitch-name_ block
(`G` in `Octave 4`), which contains the notes `C D E F G A B`.

The next block is specified using a _Scale-degree_ block (the `5th note`
in the scale, 'G', also in 'Octave 4'), `C == 1, D == 2, ...`. The
_Scale-Degree_ block has numbers like the _Number_ block, but also has
an accidental so that the user may play pitches outside a given key.

The next blocks is specified using a _Nth Modal Pitch_ block. This
block takes a number argument and turns it into the "nth pitch of
a given scale" with an index of 0 (i.e. C for C major is 0). Therefore
in order to get `G`, we input the number 4. The octave argument will
force the octave up or down; otherwise the user may just keep going up
or down in either direction to go through scalar pitches of any mode.

The next block is specified using a _Pitch-number_ block (the `7th
semitone` above `C` in `Octave 4` is `G`). The offset for the pitch
number can be modified using the _Set-pitch-number-offset_ block.

The pitch of the next block is specified using the _Hertz_ block in
conjunction with a _Number_ block (`392` Hertz is `G` in `Octave 4`),
which corresponds to the frequency of the sound made.

The octave is specified using a number block and is restricted to
whole numbers. In the case where the pitch name is specified by
frequency, the octave is ignored.The octave argument can also be
specified using a _Text_ block with values _current_, _previous_,
_next_ which does as 0, -1, 1 respectively.

The octave of the next block is specified using a _current_ text block
(`Sol` in `Octave 4`).

The octave of the next block is specified using a _previous_ text
block (`G` in `Octave 3`).

The octave of the last block is specified using a _next_ text block
(`G` in `Octave 5`).

Note that the pitch name can also be specified using a _Text_ block.

![pie menu](./piemenu2.svg "A pie menu for selecting pitch.")

As a convenience, a pie menu is used for selecting pitch, accidental,
and octave.

![Note Chart](../charts/KeyboardChart.svg "Note layout chart for keyboard")

![Mallet Chart](../charts/MalletChart.svg "Note layout chart for mallet")

Please refer to the above charts for a visual representation of where
notes are located on a keyboard or staff.

### <a name="MULTI-PITCH">2.3 Multiple Pitches</a>

![multiple pitch](./note4.svg "Playing multiple pitches in one note")

Multiple, simultaneous pitches can be specified by adding multiple
_Pitch_ blocks into a single _Note value_ block, like the above
example.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725793652385126&run=True)

### <a name="RESTS">2.4 Rests</a>

![silence block](./silence.svg "Silence blocks create rests")

A rest of the specified note value duration can be constructed using a
_Silence_ block in place of a _Pitch_ block.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725793737126028&run=True)

### <a name="DRUMS">2.5 Drums</a>

![drum](./drum1.svg "Using Drum Sample block")

Anywhere a _Pitch_ block can be used&mdash;e.g., inside of the matrix
or a _Note value_ block&mdash;a _Drum Sample_ block can also be used
instead. Currently there about two dozen different samples from which
to choose. The default drum is a kick drum.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725793852737369&run=True)

![drums](./note5.svg "Multiple Drum Sample blocks in combinations")

Just as in the [multi-pitch](#23-multiple-pitches) example above, you
can use multiple _Drum_ blocks within a single _Note value_ blocks,
and combine them with _Pitch_ blocks as well.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725793935277059&run=True)

## <a name="PROGRAMMING-WITH-MUSIC">3. Programming with Music</a>

[Previous Section (2. Making Sounds)](#2-making-sounds) | [Back to Table of
Contents](#table-of-contents) | [Next Section (4. Widgets)](#4-widgets)

This section of the guide discusses how to use chunks of notes to
program music. Note that you can program with chunks you create by
hand or use [_The Phrase Maker_](#42-generating-chunks-of-notes)
widget to help you get started.

### <a name="ACTIONS">3.1 Actions</a>

![action](./chunk-2.svg "working of action stack")

![action](./chunk-1.svg "using action inside Start block")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725788353457649&run=True)

Every time you create a new _Action_ stack, Music Blocks creates a new
block specific to, and linked with, that stack. (The new block is
found at the top of the _Block_ palette, found on the left edge of the
screen.) Clicking on and running this block is the same as clicking on
your stack. By default, the new blocks are named `chunk`, `chunk1`,
`chunk2`... but you can rename them by editing the labels on the
_Action_ blocks.

An _Action_ block contains a sequence of actions that will only be
executed when the block is referred to by something else, such as a
start block. This is useful in orchestrating more complex programs of
music.

A _Start_ Block is an _Action_ that will automatically be executed once
the start button is pressed. This is where most of your programs will
begin at. There are many ways to _Run_ a program: you can click on
the _Run_ button at the upper-left corner of the screen to run the
music at a fast speed; you can click the _Run Slowly_ button to run it
slower (useful for debugging); and the _Step_ button can be used to
step through the program one block per button press.

In the example above, the _Action_ block named "chunk" is inside of a
_Start_ block, which means that when any of the start buttons is
pressed, the code inside the _Start_ block (the _Action_ block) will be
executed. You can add more chunks after this one inside the _Start_
block to execute them sequentially.

![action](./chunk-3.svg "usage of multiple`c action blocks")

![repeat action](./chunk-4.svg "usage of Repeat block")

You can [repeat](#333-repeating-notes) actions either by using
multiple _Action_ blocks or using a _Repeat_ block.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725788849659637&run=True)

![multiple actions](./chunk-6.svg "multiple action stacks")

![mixing actions](./chunk-5.svg "mixing and matching chunks")

You can also mix and match actions. Here we play the _Action_ block with
name `chunk0`, followed by `chunk1` twice, and then `chunk0` again.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725789807251793&run=True)

![actions](./chunk-8.svg "creating a song using actions")

![repeat](./chunk-7.svg "usage of Repeat block in a song")

A few more chunks and we can make a song. (Can you read the block
notation well enough to guess the outcome? Are you familiar with the
song we created?)
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725791527821787&run=True)

### <a name="PITCH-TRANSFORMATION">3.2 Pitch Transformations</a>

There are many ways to transform pitch, rhythm, and other sonic qualities.

#### <a name="STEP-PITCH">3.2.1 Step Pitch Block</a>

![step pitch](./transform0.svg "Using the Step Pitch block")

The _Step Pitch_ block will move up or down notes in a scale from the
last played note. In the example above, _Step Pitch_ blocks are used
inside of _Repeat_ blocks to repeat the code `7` times, playing up and
down a scale. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732586286359989&run=True)

![scalar step](./transform16.svg "Using the Scalar Step Up and Down blocks")

Another way to move up and down notes in a scale is to use the _Scalar
Step Up_ and _Scalar Step Down_ blocks. These blocks calculate the
number of half-steps to the next note in the current mode. (You can
read more about [Musical Modes](#44-musical-modes) below.) Note that
the _Mouse Pitch Number_ block returns the pitch number of the most
recent note played.

In this example, we are using the _Mode length_ block, which returns
the number of scalar steps in the current mode (7 for Major and Minor
modes). [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733192676935416&run=True)

#### <a name="SHARPS-AND-FLATS">3.2.2 Sharps And Flats</a>

![sharp and flat](./transform1.svg "Using Sharp and Flat blocks")

The _Accidental_ block can be wrapped around _Pitch_ blocks, _Note
value_ blocks, or chunks of notes inside of [_Action_](#31-actions)
blocks. A sharp will raise the pitch by one half step. A flat will
lower by one half step. In the example, on the left, just the _Pitch_
block `re` is lowered by one half step; on the right, both _Pitch_
blocks are raised by one half step. (You can also use a double-sharp
or double-flat accidental.) [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733231694757697&run=True)

#### <a name="ADJUST-TRANSPOSITION">3.2.3 Adjusting Transposition</a>

![transposition](./transform2.svg "Adjusting transpositions")

There are multiple ways to transpose a pitch: by semitone or scalar
steps or by a ratio. The _semitone-transposition_ block (above left)
can be used to make larger shifts in pitch in half-step units. A
positive number shifts the pitch up and a negative number shifts the
pitch down. The input must be a whole number. To shift up an entire
octave, transpose by `12` half-steps. `-12` will shift down an entire
octave.

The _Scalar-transposition_ block (above right) shifts a pitch based on
the current key and mode. For example, in `C Major`, a scalar
transposition of `1` would transpose `C` to `D` (even though it is a
transposition of `2` half steps). To transpose `E` to `F` is `1`
scalar step (or `1` half step). To shift an entire octave, scalar
transpose by the mode length up or down. (In major scales, the mode
length is `7`.) [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733306280056376&run=True)

![ratio transposition](../documentation/setratio_block.svg "raising by a fifth using transpose by ratio")

The _Transpose-by-ratio_ block shifts a pitch based on a ratio. For
example, a ratio of 2:1 would shift a pitch by an octave; a ratio of
3:2 would shift a pitch by a fifth. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733307313746261&run=True)

As a convenience, a number of standard scalar transpositions are
provided: _Unison_, _Second_, _Third_, ..., _Seventh_, _Down third_,
and _Down sixth_, as well as a transposition for _Octave_.

![semitone transposition](./transform3.svg "raising an octave using semitone-transposition")

In the example above, we take the song we programmed previously and
raise it by one octave. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733340896349788&run=True)

![cents](./50cent_block.svg "adding 50 cents to a pitch using the semitone-transposition")

A cent is a unit of measure for the ratio between two frequencies. A
semitone is defined as 100 cents. The frequency between two adjacent
pitches would be 50 cents. You can use the _Semitone transpose_ block
to shift a pitch by cents.

In the example above, G4 + 50 cents is 403Hz. (Recall that G4 is
392Hz and G#4 is 415Hz). [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733411391096443&run=True)

![cents by ratio](./50cents_by_ratio.svg "adding 50 cents to a pitch
 using the ratio block")

You can also use the ratio block for cents, although the math is a bit
more complicated. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733425512725578&run=True)

![register](./transform18.svg "The Register block")

The _Register_ block provides an easy way to modify the register
(octave) of the notes that follow it. In the example above it is first
used to bump the `Mi 4` note up by one octave and then to bump the
`Sol 4` note down by one octave. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733426232664999&run=True)

#### <a name="PITCH-MOVEMENT">3.2.4 Summary of Pitch Movements</a>

| Representation | Pitch Movement | Properties                                                                                                     |
| -------------- | -------------- | -------------------------------------------------------------------------------------------------------------- |
| Scalar Step    | scalar         | 0=no change                                                                                                    |
|                |                | 1=next scalar pitch in current key and mode                                                                    |
|                |                | -1=previous scalar pitch in current key and mode                                                               |
|                |                | If the argument to scalar step is positive, it moves up the scale; if it is negative, it moves down the scale. |

| Music Blocks Code for Scalar Step                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![scalar](./pitchmovement1.svg "scalar")                                                                                                                                                                                                                          |
| The example above demonstrates traveling up and down the major scale by moving an octave up from the starting note, do, one note at a time and then back down the same way. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733440581953078&run=True) |

| Standard Notation with Scalar Step                                         |
| -------------------------------------------------------------------------- |
| ![scalar step up and down](./pitchmovement1.png "scalar step up and down") |

| Representation | Pitch Movement | Properties                                                                                                                    |
| -------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Transposition  | semitone       | Creates shifts in pitch by half-steps                                                                                         |
|                |                | If the argument to transpose is positive, it will shift upwards in pitch; if it is negative, there will be a downwards shift. |
|                |                | There are 12 half-steps shifts per octave.                                                                                    |
|                |                | An argument of -12 will shift down one octave.                                                                                |
|                |                | An argument of zero will not change the pitch.                                                                                |

| Music Blocks Code with Scalar Transpose                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Scalar transpose Block](./pitchmovement2.svg "Scalar transpose Block") <br> [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733441522669991&run=True) |

| Standard Notation for Scalar Transpose                                   |
| ------------------------------------------------------------------------ |
| ![semitone transposition](./pitchmovement2.png "semitone transposition") |

| Representation | Pitch Movement | Properties                                                                                                |
| -------------- | -------------- | --------------------------------------------------------------------------------------------------------- |
| Transposition  | Scalar         | Shifts the pitch based on the current key and mode                                                        |
|                |                | Each number represents a scalar step.                                                                     |
|                |                | Scalar transposition can transform your original key to a new key by counting the notes between the keys. |
|                |                | For example: Transposing C-D-E-F by 4 (fifth) will give us G-A-B-C                                        |
|                |                | To transpose an octave: shift by the mode length (7 in major scales) up or down.                          |

#### <a name="SET-KEY">3.2.5 Set Key</a>

The _Set key_ block is used to change both the mode and key of the
current scale. (The current scale is used to define the mapping of
Solfege [when set Movable Do = True] to notes and also the number of half steps take by the the
_Scalar step_ block.) For example, by setting the key to C Major, the
scale is defined by starting at C (or Do) and applying the pattern of half
steps defined by a Major mode. In this case, the pattern of steps
skips past all of the sharps and flats. (On a piano, C Major is just
the white keys).

When using the _Set key_ block, the mode argument is used to define
the pattern of half steps and the key argument is used to define the
starting position of the pattern. For example, when mode = "major" and
key = "C", the pattern of half steps is 2 2 1 2 2 2 1 and the first
note in the scale from which the pattern is applied is "C".

| Set Key Example                             |
| ------------------------------------------- |
| ![set key](./setkey1.svg "set key example") |

Using the example above, one can modify the arguments to _Set key_ in
order to move up and down one octave in a scale. The example shows G
Major scale, which has an F#, but it could be used for any combination
of key and mode. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1662103714150464&run=True)

| Standard Notation for Set Key Example                          |
| -------------------------------------------------------------- |
| ![set key notation](./setkey2.png "Standard Notation Set Key") |

Various examples for Major modes are shown in the following table.

| Key | Mode  | Mode Pattern in Half Steps | Pitch Pattern             |
| --- | ----- | -------------------------- | ------------------------- |
| C   | Major | 2 2 1 2 2 2 1              | C, D, E, F, G, A, B, C    |
| G   | Major | 2 2 1 2 2 2 1              | G, A, B, C, D, E, F#, G   |
| D   | Major | 2 2 1 2 2 2 1              | D, E, F#, G, A, B, C#, D  |
| F   | Major | 2 2 1 2 2 2 1              | F, G, A, B♭, C, D, E, F   |
| B♭  | Major | 2 2 1 2 2 2 1              | B♭, C, D, E♭, F, G, A, B♭ |

The next table is the same sets of various keys (starting pitches),
but the mode is set to "Dorian" instead of Major.

| Key | Mode   | Mode Pattern in Half Steps | Pitch Pattern               |
| --- | ------ | -------------------------- | --------------------------- |
| C   | Dorian | 2 1 2 2 2 1 2              | C, D, E♭, F, G, A, B♭, C    |
| G   | Dorian | 2 1 2 2 2 1 2              | G, A, B♭, C, D, E, F, G     |
| D   | Dorian | 2 1 2 2 2 1 2              | D, E, F, G, A, B, C, D      |
| F   | Dorian | 2 1 2 2 2 1 2              | F, G, A♭, B♭, C, D, E♭, F   |
| B♭  | Dorian | 2 1 2 2 2 1 2              | B♭, C, D♭, E♭, F, G, A♭, B♭ |

This last table is the same set of keys as the above two tables, but
the mode is set to "Phrygian".

| Key | Mode     | Mode Pattern in Half Steps | Pitch Pattern                 |
| --- | -------- | -------------------------- | ----------------------------- |
| C   | Phrygian | 1 2 2 2 1 2 2              | C, D♭, E♭, F, G, A♭, B♭, C    |
| G   | Phrygian | 1 2 2 2 1 2 2              | G, A♭, B♭, C, D, E♭, F, G     |
| D   | Phrygian | 1 2 2 2 1 2 2              | D, E♭, F, G, A, B♭, C, D      |
| F   | Phrygian | 1 2 2 2 1 2 2              | F, G♭, A♭, B♭, C, D♭, E♭, F   |
| B♭  | Phrygian | 1 2 2 2 1 2 2              | B♭, C♭, D♭, E♭, F, G♭, A♭, B♭ |

Notice how in all the examples, the sets with the same mode results in
the same "Mode Pattern of Half Steps", but the resultant "Pitch
Pattern" is different. Also, notice how G Dorian and F Major have the
same set of pitches in "Pitch Pattern" (they both have B♭ and no other
sharps or flats). C Dorian, D Phrygian, and B♭ Major all have the same
set of pitches as well (all three have B♭ and E♭).

If these lists were expanded further, there would be many more such
examples. These are because these modes (Major, Dorian, and Phrygian)
all have essentially the same modal pattern; the starting point is
just shifted slightly for each: Dorian could be thought of starting
from the second scale degree of Major and Phrygian from the third, for
example. Not all modes have this relationship to Major. The ones that
do are: Ionian (Major), Dorian, Phrygian, Lydian, Myxolydian, Aeolian
(Minor), and Locrian.

**Set Key & Scalar Step**

The _Set key_ block is used to select a subset of notes in the given
temperament. (By default, Music Blocks uses equal temperament of 12
equal divisions of the octave. The key and mode determine which of
these notes will be used.)

**Set Key & Movable Do**

The _Set Key_ block will change the key and mode of the mapping
between solfege, e.g., `Do`, `Re`, `Mi`, to note names, e.g., `F#`,
`G#`, `A#`, when in F# Major. It only impacts the mapping of solfege
when the _movable Do_ block is set to True.

You can find the _Set key_ block on the _Intervals_ palette.

| Music Blocks for Set Key and Movable Do                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![scalar transposition](./pitchmovement3.svg "scalar transposition") <br> [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733441522669991&run=True) |

| Standard Notation for Set Key and Movable Do                         |
| -------------------------------------------------------------------- |
| ![scalar transposition](./pitchmovement3.png "scalar transposition") |

| Representation | Pitch Movement | Properties                                                                                                                        |
| -------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Scale Degree   | Scalar         | The key block sets the key and mode.                                                                                              |
|                |                | The scale degree blocks indicate which position the pitch is taking in the scale relative to the tonic which is "scale degree 1". |

| Music Blocks Code with Scale Degrees 1-5                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------- |
| ![scale degree](./pitchmovement4.svg "scale degree") <br> [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733480662614787&run=True) |

| Standard Notation for Scale Degrees 1-5              |
| ---------------------------------------------------- |
| ![scale degree](./pitchmovement4.png "scale degree") |

| Representation | Pitch Movement                 | Properties                                                                                              |
| -------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Movable “Do”   | Advanced transposition by mode | Movable Do in combination with the Scale/Mode blocks will transpose sections of music in a nuanced way. |
|                |                                | The Set-key block allows you to change both the mode and key of how solfege is mapped to the notes.     |
|                |                                | For example, in C major - Do is C, Re is D, Mi is E, etc.                                               |
|                |                                | In F major - Do is F, Re is G, Mi is A                                                                  |

| Music Blocks Code with Set Key and Movable Do                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------- |
| ![movable do](./pitchmovement5.svg "movable do") <br> [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733481433887068&run=True) |

| Standard Notation Code for Set Key and Movable Do |
| ------------------------------------------------- |
| ![movable do](./pitchmovement5.png "movable do")  |

| Representation | Pitch Movement                 | Properties                                                                                                                                           |
| -------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Movable “Do”   | Advanced transposition by mode | You also have the option of changing the mode to Minor, Major, Chromatic, and many other exotic modes like hirajoshi, as shown in the example below. |

| Music Blocks for Set Key and Scalar Step                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------- |
| ![movable do](./pitchmovement6.svg "movable do") <br> [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733487475028348&run=True) |

| Standard Notation with Set Key and Scalar Step   |
| ------------------------------------------------ |
| ![movable do](./pitchmovement6.png "movable do") |

#### <a name="FIXED-AND-MOVABLE-PITCH-SYSTEMS">3.2.6 Fixed and Movable Pitch Systems</a>

Music Blocks allows users to express and explore musical ideas in a
variety of different systems. The main systems of expression are fixed
and movable.

**Fixed and Movable Systems**

Fixed pitch systems represent pitches in an absolute way. Pitches in a
fixed system do not change, regardless of a tonal context (such as key
or mode). Movable systems, on the other hand, represent pitches in a
relative way based on their tonal context.

An example of a fixed system is Alphabet Notation. Pitches are
expressed as `A`, `B`, `C`, `D`, `E`, `F`, and `G`. Regardless of
whether the key is C major or G minor, the pitch of `G` is the
same. In Alphabet Notation, pitches are the same ("fixed") regardless
of the context.

![Alphabet Fixed
 System](./systems-alphabet.svg "Alphabet (Fixed) System")

An example of a movable system is Scale Degree. Pitches are expressed
as `1`, `2`, `3`, `4`, `5`, `6`, and `7`. For C major, these pitches
are `C`, `D`, `E`, `F`, `G`, `A`, and `B`. For G (natural) minor,
these pitches are `G`, `A`, `B♭`, `C`, `D`, `E♭`, and `F`. For D
dorian, these pitches are `D`, `E`, `F`, `G`, `A`, `B`, and `C`. In
all three examples, the pitches are determined by the tonal context.

![Scale Degree Movable
 System](./systems-scale-degree.svg "Scale Degree (Movable) System")

Solfege is an example of a system that can be either fixed or movable;
it can either be a fixed system (Fixed Solfege) or a movable system
(Movable Solfege).

Fixed Solfege works like the alphabet system; `La` is `A`, `Ti` is
`B`, `Do` is `C`, etc. Context does not affect the sounding
pitch. Movable Solfege works like the Scale Degree system; for any
major, `Do` is 1st scale degree, `Re` is 2nd, `Mi` is 3rd, `Fa` is
4th, etc. Hence, in Movable Solfege in the key of G (natural) minor,
`Do` is `G`, `Re` is `A`, et al.

![Movable Solfege
 System](./systems-movable-solfege.svg "Movable Solfege System")

Music Blocks users can create and preview code in both Fixed Solfege
and Movable Solfege. Teachers and learners may use either system (or
both) to express their musical ideas as well as deepen their
understanding of music.

**Using Tonal Context with Movable Systems**

For movable systems an important point of context is its key and
mode. For "C Major", the key is "C" and the mode is "Major" (also
called Ionian). Key and mode are important as they define the tonal
framework, i.e., which pitches are "in" and which are "out". It also
defines the function of the pitches within the framework. This is why
for scale degrees `1`, `2`, `3`, `4`, and `5`, the expected result for
C major is `C`, `D`, `E`, `F`, and `G` (skipping any sharps/flats),
while those same scale degrees for D major are `D`, `E`, `F#`, `G`,
and `A`. The set of pitches that make up C major have no sharps or
flats, so they are skipped. D major has two sharps, `F#` and `C#`. The
`F#` is the 3rd scale degree for D major.

Scale Degree with _Set Key_ is a very powerful tool for expression. It
is also very common in music pedagogy. However, because the number
values 1-7 are hard wired into this system, it is a tool that works
best to express seven-pitch tonal frameworks (e.g. major, minor, and
other common seven pitch scales). For musical ideas where a more
purely mathematical form of expression is required, Music Blocks
offers the user the _nth Modal Pitch_ block.

_nth Modal Pitch_ is similar to _Scale Degree_ in that it is a movable
system that uses numbers to express pitches. However, unlike _Scale
Degree_, _nth Modal Pitch_ starts at `0`, allows for negative
numbers, and is not restricted to a seven-pitch tonal framework. `0`
is the first pitch of the mode, `1` is the next pitch, `2` is the
pitch above that, etc. `-1` is the pitch before the first pitch of
the mode. This tool is especially helpful for expressing a musical
idea that requires computation as you can run computations directly
on the number value. It is also helpful if you are, for example,
creating music in a whole tone (six note) pitch space. In the case of
_Set Key_ set to "whole tone", `6` would be the octave above.

**Pitch Number, MIDI, and Set Pitch Number Offset**

_Pitch Number_ is similar to _nth Modal Pitch_ in that it is a
zero-based, mathematical system to express pitches. However, unlike
_nth Modal Pitch_, _Pitch Number_ disregards any tonal framework. It
is also chromatic by default, meaning that its pitch space includes
the sharp/flat pitches (black keys on piano) as well as the natural
pitches (white keys on piano). By default, middle C (C_4) is `0`. The
C major scale in the 4th octave is `0`, `2`, `4`, `5`, `7`, `9`, and
`11`. `12` is the C an octave above middle C (C_5). This system is
useful mathematically, but because it disregards key, it is difficult
to control when creating music. That being said, fretted instruments
such as ukulele and guitar use this system to express pitch, so it is
a good system for expressing how these instruments work.

MIDI also uses a similar system to _Pitch Number_ to express pitches,
but the 0 is offset from Music Blocks' default. In order to change the
sounding pitch of `0` for _Pitch Number_, use _set pitch number
offset_. This makes _Pitch Number_ blocks behave as a relative system
as it transposes the pitches up or down accordingly (but has no effect
on key).

**Two Subsystems for Movable**

For Movable Do, there exists yet two more systems. One system, which
we call `Movable=Do`, allows the user to express solfege syllables in
relation to the Major mode. Therefore, if a user were to specify A
minor, then La would be A, the first scale degree in A Minor. The
other system, which we call `Movable=La` allows the user to express
solfege in relation to the particular mode specified. Therefore, if a
user were to specify A Minor, then Do would be A. _Scale Degree_ works
like `Movable=La` by default such that `1` is always the first pitch
of a given mode.

Because some users may want to explicitly spell out all of the pitches
regardless of the chosen key, we allow them to use Scale Degree with
the _Movable Do_ block (remember, Scale Degree works like Movable=La
by default). Please see [this
code](https://rawgithub.com/sugarlabs/musicblocks/master/examples/2-spelling-systems-for-Scale-Degree.html)
as an example.

The following chart describes the behavior of different blocks
depending on whether or not a _Movable Do_ block is present.

| Block(s)                    | Fixed or Movable? (Do or La?)           | Set Key Transformation?                                                                 |
| --------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------- |
| Alphabet Pitch              | Fixed                                   | No effect.                                                                              |
| Solfege                     | Fixed by default                        | No effect.                                                                              |
| Solfege and Movable=Do      | Specified via "movable" block set to Do | Yes.                                                                                    |
| Solfege and Movable=La      | Specified via "movable" block set to La | Yes. Works like Scale Degree.                                                           |
| n^th modal pitch            | Movable                                 | Yes. Good for modes of any length.                                                      |
| Scale Degree                | Movable                                 | Yes. Most useful for 7 note systems. Works just like Movable=La for Solfege by default. |
| Scale Degree and Movable=Do | Movable                                 | Yes. When preceded by Movable=Do, the user can be explicit in their spelling.           |
| Scalar Step                 | Movable                                 | Yes. Navigates up/down within _nth modal pitch_ space.                                  |
| Scalar Interval             | Movable                                 | Yes. Adds above/under within _nth modal pitch_ space.                                   |
| Scalar Inversion            | Movable                                 | Yes. Inversion around a specified axis within _nth modal pitch_ space.                  |
| Pitch Number                | Movable                                 | No effect. Pitches can be transformed via Set Pitch Number Offset.                      |

**Illustrative example:**

The following example demonstrates how the Scale Degree functionality
combines math and musical modifiers. When combining numbers and
accidentals, it recreates the same functionality as the _Scale Degree_
block.

![Scale Degree Improv Example](./scale-degree-improv.svg "Scale Degree Improv")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1675577999425474&run=True)

#### <a name="INTERVALS">3.2.7 Intervals</a>

![interval](./transform9.svg "Scalar interval block")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1726142617030713&run=True)

The _Scalar interval_ block calculates a relative interval based on
the current mode, skipping all notes outside of the mode. For example,
a _fifth_, and adds the additional pitches to a note's playback. In
the figure, we add `La` to `Re` and `Ti` to `Mi`.

As a convenience, a number of standard scalar intervals are provided
on the _Intervals_ palette: _Unison_, _Second_, _Third_, ...,
_Seventh_, _Down third_, and _Down sixth_.

The _Scalar interval measure_ block can be used to measure the number
of scalar steps between two pitched.

#### <a name= "ABSOLUTE-INTERVALS">3.2.7.1 Absolute Intervals</a>

Absolute (or semitone) intervals are based on half-steps.

![intervals](./transform14.svg "Using absolute intervals")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1726143428513328&run=True)

The _Augmented_ block calculates an absolute interval (in half-steps),
e.g., an augmented fifth, and adds the additional pitches to a
note. Similarly, the _Minor_ block calculates an absolute interval,
e.g., a minor third. Other absolute intervals include _Perfect_,
_Diminished_, and _Major_.

In the augmented fifth example above, a chord of `D5` and `A5` are
played, followed by a chord of `E5` and `C5`. In the minor third
example, which includes a shift of one octave, first a chord of `D5`
and `F5` is played, followed by chord of `E5` and `G6`.

As a convenience, a number of standard absolute intervals are provided
on the _Intervals_ palette: _Major 2_, _Minor 3_, _Perfect 4_,
_Augmented 6_, _Diminished 8_, et al.

The _Doubly_ block can be used to create a double augmentation or
double diminishment.

The _semitone interval measure_ block can be used to measure the
number of half-steps between two pitches.

#### <a name= "RATIO-INTERVALS">3.2.7.2 Ratio Intervals</a>

Another way to think about intervals is in terms of ratios. For
example, a ratio of 2:1 would be an octave shift up; 1:2 would be an
octave shift down; 3/2 would be a fifth.

![ratio interval](../documentation/ratiointerval_block.svg "Ratio Interval example")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1726144197873608&run=True)

The _Ratio Interval_ block lets you generate an interval based on a
ratio.

#### <a name= "CHORDS">3.2.8 Chords</a>

A chord is a group of notes that are played together (often used for
harmony in music). There are triads (three notes), tetrachords (four
notes), and even five-, six-, and seven-note chords.

The _Chord_ block builds a chord from a base note. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733533569615271&run=True)

![chord](../documentation/chordinterval_block.svg "Chord Block")

We support many basic chords:

|   chord    | intervals |        example        |
| :--------: | :-------: | :-------------------: |
|   major    |   1 4 7   |   C major C - E - G   |
|   minor    |   1 3 7   |  C minor C - E♭ - G   |
| dominant 7 | 1 4 7 10  |   C7 C - E - G - B♭   |
|  minor 7   | 1 3 7 10  | Cmin7 C - E♭ - G - B♭ |
|  major 7   | 1 4 7 11  |  Cmaj7 C - E - G - B  |

The _Arpeggio_ block also builds a chord from a base note, but rather
than playing all of the pitches at once, each pitch is played in
sequence.

![arpeggio](../documentation/arpeggio_block.svg "Arpeggio Block")

In the example above, since the Major chord intervals are 1 4 7, the
notes played are do, mi, sol, sol, ti, mi. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733828377963278&run=True)

#### <a name= "INVERSION">3.2.9 Inversion</a>

The _Invert_ block will rotate a series of notes around a target
note. There are three different modes of the _Invert_ block: _even_,
_odd_, and _scalar_. In _even_ and _odd_ modes, the rotation is based
on half-steps. In _even_ and _scalar_ mode, the point of rotation is
the given note. In _odd_ mode, the point of rotation is shifted up by
a `1/4` step, enabling rotation around a point between two notes. In
"scalar" mode, the scalar interval is preserved around the point of
rotation.

![inversion](./transform13.svg "inversion")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1726144415115588&run=True)

NOTE: The initial `C5` pitch (as a half note) remains unchanged (in
all of the examples) as it is outside of the invert block.

The above example code has an _even_ inversion for two notes `F5` and
`D5` around the reference pitch of `C5`. We would expect the following
results:

**Even inversion**

| Starting pitch |  Distance from `C5`  | Inverse distance from `C5` | Ending pitch |
| :------------: | :------------------: | :------------------------: | :----------: |
|      `F5`      | 5 half steps _above_ |    5 half steps _below_    |     `G4`     |
|      `D5`      | 2 half steps _above_ |    2 half steps _below_    |    `B♭4`     |

This operation can also be visualized on a pitch clock. The arrows on
the following diagram point from the starting pitch, around the axis
of the reference pitch, to its destination ending pitch.

![even invert](./even-invert-chart.svg "even invert chart")

In standard notation the result of this _even_ inversion operation is
depicted in the second measure of the following example. The first
measure is the original reference.

![even invert](./invert-even.png "even invert example")

Underneath the _even_ inversion in the example code is an _odd_
inversion for the same two notes of `F5` and `D5` around the same
reference pitch of `C5`. We would expect the following results:

**Odd inversion**

| Starting pitch | Distance from midway-point between `C5` and `C♯5` | Inverse distance from midway-point between `C5` and `C♯5` | Ending pitch |
| :------------: | :-----------------------------------------------: | :-------------------------------------------------------: | :----------: |
|      `F5`      |              4.5 half steps _above_               |                  4.5 half steps _below_                   |    `A♭4`     |
|      `D5`      |              1.5 half steps _below_               |                  1.5 half steps _above_                   |     `B4`     |

This operation can be visualized on a pitch clock similar to _even_
inversion except offset in-between `C5` and `C♯5` (i.e. quarter step
_above_ `C5`).

![odd invert](./odd-invert-chart.svg "odd invert chart")

In standard notation the result of this _odd_ inversion operation is
depicted in second measure of the following example. The first measure
is the original reference. NOTE: The `C5` pitch remains unchanged as
it is not operated upon in the example block code (above). If it were
contained in the operation it would be changed to `C♯5` (i.e. `C5` is
0.5 half steps _below_ the axis of rotation, so the result of an
inversion around `C5` and `odd` would be 0.5 half steps _above_ the
axis of rotation).

![odd invert](./invert-odd.png "odd invert example")

**Scalar inversion**

Underneath the _even_ and _odd_ inversion blocks in the example code
is an inversion block set to _scalar_. We would expect the following
results:

| Starting pitch | Scalar distance from `C5` (in steps) | Inverse scalar distance from `C5` (in steps) | Ending pitch |
| :------------: | :----------------------------------: | :------------------------------------------: | :----------: |
|      `F5`      |  3 above (C5 --> D5 --> E5 --> F5)   |      3 below (C5 --> B4 --> A4 --> G4)       |     `G4`     |
|      `D5`      |         1 above (C5 --> D5)          |             1 below (C5 --> B4)              |     `B4`     |

This operation can be visualized on a pitch clock similar to _odd_ and
_even_ except that all non-scalar pitches (i.e. pitches outside the
chosen key) are skipped. NOTE: The scalar pitches are shown in bold in
the following pitch clock diagram.

![scalar invert](./scalar-invert-chart.svg "scalar invert chart")

In standard notation the result of _scalar_ inversion operation is
depicted in the second measure of the following example. The first
measure is the original reference.

![scalar invert](./invert-scalar.png "scalar invert example")

In the _invert (even)_ example above, notes are inverted around `C5`.
In the _invert (odd)_ example, notes are inverted around a point
midway between `C5` and `C♯5`. In the _invert (scalar)_ example,
notes are inverted around `C5`, by scalar steps rather than
half-steps.

#### <a name="CONVERTERS">3.2.10 Converters</a>

Converters are used to transform one form of inputs into other, more
usable form of outputs. This section of the guide will talk about the
various conversion options Music Blocks has to offer.

Generalized shape of a converter is:

![converter](../documentation/number2pitch_block.svg "Generalized converter")

where the right argument is converted accordingly, and output is
received on the left side.

**Note:** Before an introduction of the different types of converters,
a little introduction on Y staff in Music Blocks. Staff is a set of
horizontal lines and spaces and different positions along Y axis
represents different notes. [C, D, E, F, G, A, B]

![staff](treble.svg "Treble clef staff")

#### <a name="y-to-pitch">3.2.10.1 Y to Pitch</a>

![y pos](../documentation/ytopitch_block.svg "Y to Pitch converter")

This converter takes input in the form of a number that represents
Staff Y position in pixels, and processes the value such that it can
be used with certain pitch blocks (pitch number, nth modal pitch,
pitch) to produce notes corresponding to given Staff Y position as an
argument.

Additionally, the block can be plugged into a print block to view the
converted note value.

#### <a name="pitch-converter">3.2.10.2 Pitch converter</a>

![pitch converter](../documentation/outputtools_block.svg "Pitch converter block")

Pitch converter offers a range of options through a pie-menu based
interface and it can potentially convert or extract info out of the
current playing pitch using the current pitch block as an input. It
can also take custom input in form or solfege, hertz, pitch number
etc.

All these options are provided in the form of a pie-menu which can be
accessed simply by clicking on the converter.

![pitch converter](./pitchconverter.svg "Pitch converter block")

Below explained is the utility of every conversion option:

#### **0. Alphabet:**

Prints the alphabet data of the note being played e.g A, B, C, D, E,
F, G, including accidentals.

#### **1. Alphabet Class:**

Prints the alphabet data of the note being played e.g A, B, C, D, E,
F, G. It doesn't print any info regarding accidentals.

#### **2. Solfege Syllable:**

Similar to Alphabet class, returns the data in form of solfege e.g do,
re, mi. It too, gives no info regarding accidentals.

#### **3. Pitch Class:**

Returns a number between 0 to 11, corresponding to the note played,
where C is 0 and B is 11. Each increase in the number signifies an
increase by one semitone.

#### **4. Pitch Number:**

Value of the pitch of the note currently being played. It is different
from Pitch class in the way that it can go below 0 and above 11
depending upon the octave.

#### **5. Pitch in Hertz:**

Returns the value in hertz of the pitch of the note being currently
played.

#### **6. Scalar Class:**

Returns a number between 1-7 corresponding to the scale degree of the
note being played, with reference to the chosen mode. Provides no info
regarding accidentals.

#### **7. Scale Degree:**

Intuitively, returns the scale degree of the note being played with
reference to the chosen mode. It can also be thought of as Scalar
class with accidentals.

#### **8. N^th Degree:**

Zero-based index of the degree of note being played in the chosen
mode.

#### **9. Staff Y:**

Returns the Y staff position of the note being played according to
staff dimensions. It takes into account only the alphabet class, no
accidental info is processed.

#### <a name="number-2-octave">3.2.10.3 Number to Octave </a>

![pitch converter](../documentation/number2octave_block.svg "Y to Pitch converter")

This converter takes a numeric value which denotes pitch number and
returns the octave corresponding to that pitch number.

#### <a name="number-2-pitch">3.2.10.4 Number to Pitch</a>

![pitch converter](../documentation/number2pitch_block.svg "Y to Pitch converter")

This converter takes a numeric value which denotes pitch number and
returns the pitch name corresponding to that pitch number. No octave
is inferred.

| Converter Name   | Description                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| alphabet         | Converts pitch to letter (as defined above). G maps to G. G♯ maps to G#.                        |
| alphabet class   | Converts pitch to letter (as defined above). G maps to G. G♯ also maps to G.                    |
| solfege syllable | Converts pitch to solfege (as defined above). G maps to sol.                                    |
| solfege class    | Converts pitch to solfege class (as defined above). G maps to sol. G♯ maps to sol.              |
| pitch class      | Converts pitch to pitch class (as defined above). G maps to 7.                                  |
| scalar class     | Converts pitch to scalar class (as defined above). G maps to 5.                                 |
| scale degree     | Converts pitch to scale degree (as defined above). G maps to 5.                                 |
| nth degree       | Converts pitch to nth degree (as defined above). G maps to 4.                                   |
| staff y          | Maps the current pitch to a y value that corresponds to a position on the staff. G4 maps to 50. |
| pitch number     | Converts pitch to pitch number (as defined above). G maps to 7.                                 |
| pitch in hertz   | Converts pitch to hertz. G4 maps to 392Hz.                                                      |
| pitch to color   | Converts pitch to a color value (0-100). C maps to 0, G maps to 58.3, etc.                      |
| pitch to shade   | Converts the octave value of the current pitch to a shade. Octave 4 maps to 50.                 |

### <a name="NOTE-VALUE-TRANSFORMATION">3.3 Note Value Transformations</a>

#### <a name="DOTTED">3.3.1 Dotted Notes</a>

![dot](./transform4.svg "Creating dotted notes using the Dot block")

You can "dot" notes using the _Dot_ block. A dotted note extends the
rhythmic duration of a note by 50%. E.g., a dotted quarter note will
play for `3/8` `(i.e. 1/4 + 1/8)` of a beat. A dotted eighth note will
play for `3/16` `(i.e. 1/8 + 1/16)` of a beat. A double dot extends
the duration by `75%` `(i.e. 50% + [50% of 50%])`. For example, a
double-dotted quarter note will play for `7/16` `(i.e. 1/4 + 1/8 +
1/16)` of a beat (which is the same as `4/16 + 2/16 + 1/16 =
7/16`).
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733856425527606&run=True)

The dot block is useful as an expression of musical rhythm--it is
convenient and helps to organize musical ideas (e.g. many melodies use
dots as the basis of their rhythmic motifs), however you can achieve
the same rhythmic result as dot by putting the calculation directly
into note value as well. For example, indicating `3/8` instead of
`1/4` will result in a dotted quarter note.

The chart below shows two common examples, dotted quarter and dotted
eighth, and how to achieve them with either the dot block or by direct
calculation into a note's note value.

![dotted note](../charts/DotsChart.svg "using dotted notes")

#### <a name="MULTIPLY-AND-DIVIDE">3.3.2 Speeding Up and Slowing Down Notes via Mathematical Operations</a>

![duration](./transform5.svg "Changing note duration for a note or notes")

You can also multiply (or divide) the note value, which will change
the duration of the notes by changing their note values. Multiplying
the note value of an `1/8` note by `1/2` is the equivalent of playing
a `1/16` note (i.e. `1/2 * 1/8 = 1/16`) . Multiplying the note value
of an `1/8` note by `2/1` (which has the effect of dividing by `1/2`)
will result in the equivalent of a `1/4` note.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1733894227395433&run=True)

![drums](./drum4.svg "speeding up drum beats over time")

In the above example, the sequence of [drum](#25-drums) note values is
decreased over time, at each repetition.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1523106271018484&run=True)

#### <a name="REPETITION">3.3.3 Repeating Notes</a>

![repeat](./transform6.svg "repeating notes")

There are several ways to repeat notes. The _Repeat_ block will play a
sequence of notes multiple times; the _Duplicate_ block will repeat each
note in a sequence.

In the example, on the left, the result would be `Sol, Re, Sol, Sol,
Re, Sol, Sol, Re, Sol, Sol, Re, Sol`; on the right the result would be
`Sol, Sol, Sol, Sol, Re, Re, Re, Re, Sol, Sol, Sol, Sol`.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725794018017026&run=True)

#### <a name="SWINGING">3.3.4 Swinging Notes and Tied Notes</a>

![swing](./transform7.svg "swinging notes and tied notes")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725867425283695&run=True)

The _Swing_ block works on pairs of notes (specified by note value),
adding some duration (specified by swing value) to the first note and
taking the same amount from the second note. Notes that do not match
note value are unchanged.

In the example, `fa4` would be played as a `1/6` note and `sol4` would
be played as a `1/12` note (`1/8 + 1/24 === 1/6` and `1/8 - 1/24 ===
1/12`). Observe that the total duration of the pair of notes is
unchanged.

Tie also works on pairs of notes, combining them into one note. (The
notes must be identical in pitch, but can vary in rhythm.)

![ties](../charts/TiesChart.svg "using notes with ties")

#### <a name="BEAT">3.3.5 Beat</a>

The beat of the music is determined by the _Meter_ block (by default,
it is set to 4:4).

The _Pickup_ block can be used to accommodate any notes that come in
before the beat.

![meter](./beat1.svg "meter and pickup")

The Beat count block is the number of the current beat, eg 1, 2, 3, or 4.
In the figure, it is used to take an action on the first beat of each measure.

![beat count](../documentation/beatvalue_block.svg "beat count")

The Measure count block returns the current measure.

![measure count](../documentation/measurevalue_block.svg "measure count")

Specifying beat is useful in that you can have the character of a note
vary depending upon the beat. In the example below, the volume of
notes on Beat `1` and Beat `3` are increased, while the volume of off
beats is decreased.

![on beat](./beat2.svg "on-beat-do")

The _On-Beat-Do_ and _Off-Beat-Do_ blocks let you specify actions to
take on specific beats. (Note that the action is run before any blocks
inside the note block associated with the beat are run.)

More examples can be found in the [Graphics](#36-adding-graphics)
section below.

#### <a name="BEAT-TRANSFORMATIONS">3.3.6 Staccato and Slur</a>

![slur](./transform17.svg "Staccato, and Slur blocks")

The _Staccato_ block shortens the length of the actual
note&mdash;making them tighter bursts&mdash;while maintaining the
specified rhythmic value of the notes.

The _Slur_ block lengthens the sustain of notes&mdash;running longer than
the noted duration and blending it into the next note&mdash;while
maintaining the specified rhythmic value of the notes.

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725868210212676&run=True)

#### <a name="BACKWARDS">3.3.7 Backwards</a>

![backwards](./transform11.svg "Backward block")

The _Backward_ block will play the contained notes in reverse order
(retrograde). In the example above, the notes in `chunk` are played as
`Sol`, `Ti`, `La`, `Sol`, i.e., from the bottom to the top of the
stack.

An example from Bach is provided. In the example, there are two
voices, one which plays the composition forward and one that plays the
same composition backward.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1522885752309944&run=True)

Note that all of the blocks inside a _Backward_ block are reverse, so
use this feature with caution if you include logic intermixed with
notes.

### <a name="OTHER-TRANSFORMATION">3.4 Other Transformations</a>

#### <a name="VOLUME-TRANSFORMATIONS">3.4.1 Set Volume and Crescendo</a>

![volume](./transform8.svg "Set master volume, set synth volume, set relative volume, crescendo")

The _Set master volume_ block will change the master volume. The
default is `50`; the range is `0` (silence) to `100` (full volume).

The _Set synth volume_ block will change the volume of a particular
synth, e.g., `violin`, `snare drum`, etc. The default volume is `50`;
the range is `0` (silence) to `100` (full volume). In the example, the
_synth name_ block is used to select the current synth.

As a convenience, a number of standard volume blocks are provided:
from loudest to quietest, there is _fff_, _ff_ _f_, _mf_, _mp_, _p_,
_pp_, and _ppp_. In musical terms "f" means "forte" or loud, "p" means
"piano" or soft, and "m" means "mezzo" or middle.

The _Set Relative Volume_ block modifies the clamped note's volume
according to the input value of the block in an added (or subtracted
when negative) percentage with respect to the original volume. For
example, `100` would mean doubling the current volume.

The _Crescendo_ block will increase (or decrease) the volume of the
contained notes by a specified amount for every note played. For
example, if you have 3 notes in sequence contained in a _Crescendo_
block with a value of `5`, the final note will be at 15% more
than the original value for volume.

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725868641106995&run=True)

NOTE: The _Crescendo_ block does not alter the volume of a note as it
is being played. Music Blocks does not yet have this functionality.

#### <a name= "SETTINGVOICE">3.4.2 Setting Instrument</a>

![set voice](./transform12.svg "setting voice and keys using Set Voice block")

The default instrument is an electronic synthesizer, so by default,
that is the instrument used when playing notes. You can override this
default for a group of notes by using the _Set Instrument_ block. It
will select an [instrument](#342-setting-instrument) for the
synthesizer for any contained blocks, e.g., violin.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725869548034418&run=True)

![default voice](../documentation/setdefaultinstrument_block.svg "Set Default Instrument")

You can also override the default using the _Set default instrument_
block. In the example above, the default instrument is set to piano,
so any note that is not inside of a _Set instrument_ block will be
played using the piano synthesizer. The first note in this example is
piano; the second note is guitar; and the third is piano.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1734599929166507&run=True)

#### <a name= "SETTINGKEY"></a>3.4.3 Setting Key and Mode

![set key](./transform10.svg "Set Key block")

The _Set Key_ block will change the key and mode of the mapping
between solfege, e.g., `Do`, `Re`, `Mi`, to note names, e.g., `C`,
`D`, `E`, when in C Major. Modes include Major and Minor, Chromatic,
and a number of more exotic modes, such as Bebop, Geez, Maqam, etc.
This block allows users to access "movable Do" within Music Blocks,
where the mapping of solfege to particular pitch changes depending on
the user's specified tonality.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725870361330836&run=True)

![mode](./transform19.svg "Define mode block")

The _Define mode_ block can be used to define a custom mode by
defining the number and size of the steps within an octave. You can
use your custom mode with the _Set key_ block.

#### <a name="VIBRATO"></a>3.4.4 Vibrato, Tremelo, et al.

![effects](./transform15.svg "Vibrato, tremelo, chorus, distortion, neighbor, and phaser blocks")

The _Vibrato_ Block adds a rapid variation in pitch to any contained
notes. The intensity of the variation ranges from `1` to `100` (cents),
e.g. plus or minus up to one half step. The rate argument determines
the rate of the variation.

The other effects blocks also modulate pitch over time. Give them a try.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725870963978517&run=True)

### <a name="VOICES">3.5 Voices</a>

Each _Start_ block runs as a separate voice in Music Blocks. (When
you click on the Run button, all of the _Start_ blocks are run
concurrently.)

![voices](./voices1.svg "use of voices")

If we put our song into an action...

![voices](./voices2.svg "running the song using multiple Start blocks")

...we can run it from multiple _Start_ blocks.

![octaves](./voices3.svg "shifting the octaves up and down")

It gets more interesting if we shift up and down octaves.

![voices](./voices4.svg "playing the various voices offset in time")

And even more interesting if we bring the various voices offset in time
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1523026536194324&run=True)

![events](./voices5.svg "queuing the various voices using events")

An alternative to use a preprogrammed delay is to use the _Broadcast_
block to bring in multiple voices. In the example above, after each
section of the song is played, a new event is broadcasted, bringing in
a new voice. Note the use of the _Mouse Sync_ block. This ensures that
the multiple voices are synced to the same master clock.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1734439833660485&run=True)

![drum](./drum3.svg "usage of kick drum")

A special _Start drum_ version of the _Start_ block is available for
laying down a drum track. Any _Pitch_ blocks encountered while starting
from a drum will be played as `C2` with the default drum sample. In
the example above, all of the notes in `chunk` will be played with a
kick drum.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1734456316657915&run=True)

### <a name="GRAPHICS">3.6 Adding graphics</a>

![graphics](./graphics1.svg "adding graphics")

![graphics](./graphics2.svg "color range")

Turtle graphics can be combined with the music blocks. By placing
graphics blocks, e.g., _Forward_ and _Right_, inside of _Note value_
blocks, the graphics stay in sync with the music. In this example, the
turtle moves forward each time a quarter note is played. It turns
right during the eighth note. The pitch is decreased by one half step,
the pen size decreases, and the pen color increases at each step in
the inner repeat loop.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1523494709674021&run=True)

![graphics](./graphics3.svg "synchronizing graphics and music")

Another example of graphics synchronized to the music by placing the
graphics commands inside of _Note value_ blocks. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1734456316657915&run=True)

![graphics](./graphics5.svg "using beat to synchronize graphics")

Another approach to graphics is to use modulate them based on the
[beat](#335-beat). In the example above, we call the same graphics
action for each note, but the parameters associated with the action,
such as pen width, are dependent upon which beat we are on. On Beat 1,
the pen size is set to `50` and the volume to `75`. On Beat `3`, the
pen size is set to `25` and the volume to `50`. On off beats, the pen
size is set to `5` and the volume to `5`. The resultant graphic is
shown below. [RUN LIVE]()

![graphics](./graphics6.svg "graphics modulated by beat")

The _On-Every-Note-Do_ block lets you specify an action to take
whenever a note is played. In the example above, the note value is
used to determine the portion of an arc to draw, i.e., a 1/4 note
draws a 1/4 circle, a 1/2 note draw 1/2 circle, and a whole note draws
a full circle.

![on-every-note-do](../documentation/arc_block.svg)

The _On-Every-Note-Do_ block is found in the Crab Canon project on the
Planet to "plot the music". The mouse moves up and down based on the
change in pich between notes and to the right in proportion to the
note value.

![crab-canon](./crab-canon.svg)

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1522885323588493)

Music Blocks has an internal "conductor" maintaining the beat. When
the Run button is clicked, the program begins and an internal master
(or "conductor") clock starts up. All of the music tries to stay
synced to that clock.

![no clock](../documentation/drift_block.svg "No-clock block")

For example, if you have multiple voices (mice), they all share the
same conductor in order to keep on the same beat. If a voice (mouse)
is falling behind, Music Blocks tries to catch up on the next note by
truncating it. If it is an 1/8 note behind and the next note is a 1/2
note, then only an 3/8 note would be played, so as to catch up. That
is a somewhat extreme example—usually the timing errors are only
very very small differences.

But in some situations, the timing errors can be very large. This is
when the _No-clock_ block is used.

A typical problem is when the music is not played
continuously. Imagine an interactive game where a hero is battling a
monster. Our hero plays theme music whenever the monster is
defeated. But that might occur at any time, hence it is not going to
be in sync with the conductor. The offset could be tens of
seconds. This would mean that all of the notes in the theme music
might be consumed by trying to catch up with the conductor. The
_No-clock_ block essentially says, do your own thing and don't worry
about the conductor.

![math](./fibonacci3.svg "usage of No-clock block")

In this example, because the computation and graphics are more
complex, a _No-clock_ block is used to decouple the graphics from the
master clock. The "No-clock\* block prioritizes the sequence of
actions over the specified rhythm.

![graphics](./graphics4.png "rhythm sequence")

![tree](./tree-example.svg "another example of the No-clock block")

Another example of embedding graphics into notes: in case, a recursive
tree drawing, where the pitch goes up as the branches ascend.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1523029986215035&run=True)

![tree](./tree.svg "tree graphic")

### <a name="INTERACTIONS">3.7 Interactions</a>

There are many ways to be interactive with Music Blocks, including
tracking the mouse position to impact some aspect of the music.

![interactivity](./interactive.svg "interactions")

For example, we can launch the phrases (chunks) interactively. We use
the mouse position to generate a suffix: `0`, `1`, `2`, or `3`,
depending on the quadrant. When the mouse is in the lower-left
quadrant, `chunk0` is played; lower-right quadrant, `chunk1`;
upper-left quadrant, `chunk2`; and upper-right quadrant, `chunk3`.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1523028011868930&run=True)

![piano](./interactive2.svg "creation of a two-key piano")

In the example above, a simple two-key piano is created by associating
_click_ events on two different turtles with individual notes. Can you
make an 8-key piano?
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1734501444456205&run=True)

![random](./interactive3.svg "adding randomness to your music")

You can also add a bit of randomness to your music. In the top example
above, the _One-of_ block is used to randomly assign either `Do` or
`Re` each time the _Note value_ block is played. In the bottom example
above, the _One-of_ block is used to randomly select between `chunk1`
and `chunk2`.

Musical Paint has been a popular activity dating back to programs such
as Dan Franzblau's _Vidsizer_ (1979) or Morwaread Farbood's
_Hyperscore_ (2002). Music Blocks can be used to create musical paint
as well. In the somewhat ambitious example below, we go a step further
than the typical paint program in that you can not only paint music (a
la Vidsizer) and playback your painting as a composition (a la
Hyperscore), but also generate _Note_ blocks from your composition.

![paint](./hyperscore.svg "musical paint")

The program works by first creating an array from the heap that
corresponds to a 20x12 grid of notes on the screen: 20 columns,
representing time from left to right; and 12 rows, corresponding to
scalar pitch values, which increase in value from the bottom to the
top.

The _record_ action repeatedly calls the _paint_ action until the
_playback_ button is clicked.

The _paint_ action tracks the mouse (_Set XY_ to _cursor x_ and
_cursor y_) and, if the mouse button is pressed, marks an entry in the
array corresponding to that note, plays the note, and leaves behind a
"drop of paint".

The _playback_ action is invoked by clicking on the _play_ mouse,
which sets _recording_ to `0`, thus breaking out of the paint "while
loop". Playback scans each column in the array from left to right for
pitches to play and generates a chord of pitches for each column.

Once the _playback_ action is complete, the _save_ action is
invoked. Again each column in the array is scanned, but this time,
instead of playing notes, the _Make Block_ block is called in order to
generate a stack of notes that correspond to the composition. This
stack can be copied and pasted into another composition.

While a bit fanciful, this example, which can be run by clicking on
the link below, takes musical paint in a novel direction.

[RUN LIVE](https://sugarlabs.github.io/musicblocks/index.html?id=1523896294964170&run=True&run=True)

## <a name="ENSEMBLE">3.8 Ensemble</a>

Much of music involves multiple instruments (voices or "mice" in Music
Blocks) playing together. There are a number of special blocks that
can be used to coordinate the actions of an ensemble of mice.

This section will guide about different ensemble blocks, which
communicate the status of mice by name, including notes played,
current pen color, pitch number, etc.

To use the ensemble blocks, you must assign a name to each mouse, as
we will reference each mouse by its name.

![mouse name](../documentation/turtlenameonly_block.svg "mouse name")

Use the _Mouse count_ block in combination with the _Nth mouse name_
block to iterate through all of the mice.

![iterate](../documentation/turtleiteration.svg "mouse iteration")

The _Mouse sync_ block aligns the beat count between mice.

![sync](../documentation/turtlesync_block.svg "mouse sync")

The _Mouse index heap_ block returns a value in the heap at a specified
location for a specified mouse.

![heap](../documentation/turtleheap_block.svg "mouse heap index")

You can use the dictionary entries to data between mice. The _Get
value_ block lets you specify a mouse name and the value you want to
access. For example, you can access a mouse's pen attributes, such as
color, shade, and grey values.

![pen](./dictionary-pen.svg "mouse pen attributes")

You can also access the mouse's graphics attributes, such as x, y, and
heading. You can also set attributes of a mouse using the _Set value_
block. In the example, a mouse's heading is set to 90.

![graphics](./dictionary-graphics.svg "mouse graphics attributes")

Some music status is also available through the dictionary. You can
access a mouse's "current pitch", "pitch number", "note value", the
number of "notes played".

![music](./dictionary-music.svg "mouse music attributes")

The dictionary can be used to share other things too. Just set a
_key/value_ pair with one mouse and access it from another.

![dictionary](./dictionary-key.svg "sharing key/value pairs")

Other Ensemble blocks include:

The _Found mouse_ block will return true if the specified mouse can be found.

![found](../documentation/foundturtle_block.svg "found mouse")

The _Set mouse_ block sends a stack of blocks to be run by the specified mouse.

![set](../documentation/setturtle_block.svg "set mouse")

## <a name="WIDGETS">4. Widgets</a>

[Previous Section (3. Programming with Music)](#3-programming-with-music) | [Back to Table of Contents](#table-of-contents) | [Next Section (5. Beyond Music Blocks)](#5-beyond-music-blocks)

This section of the guide will talk about the various Widgets that can
be used within Music Blocks to enhance your experience.

Every widget has a menu with at least two buttons.

![widget](../header-icons/close-button.svg "close button")

You can hide the widget by clicking on the _Close_ button.

You can move the widget by dragging its containing the window.

### <a name="status">4.1 Monitoring Status</a>

![widget](../images/Status_widget_debuggingMd.svg "given Music block")

![widget](./status2.svg "status in tabular form")

The _Status widget_ is a tool for inspecting the status of Music
Blocks as it is running. By default, the key, BPM, and volume are
displayed. Also, each note is displayed as it is played. There is one
row per voice in the status table.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732541757152077&run=True)

Additional _Print_ blocks can be added to the _Status_ widget to
display additional music factors, e.g., duplicate, transposition,
skip, [staccato and slur](#336-staccato-and-slur), and
[graphics](#36-adding-graphics) factors, e.g., x, y, heading, color,
shade, grey, and pensize.

![widget](../images/Status_Widget_additional_programming_DebuggingMd.svg "additional programming within the Status
 block")

You can do additional programming within the status block. In the
example above, `whole notes played` is multiplied by `4` (to calculate
quarter notes played) before being displayed.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732553086132345&run=True)

### <a name="GENERATION"></a>4.2 Generating Chunks of Notes

Using the Phrase Maker, it is possible to generate chunks of
notes at a much faster speed.

#### <a name="pitch-time">4.2.1 The Phrase Maker</a>

![widget](./matrix1.svg "phrase maker")

Music Blocks provides a widget, the _Phrase maker_, as a scaffold
for getting started.

Once you've launched Music Blocks in your browser, start by clicking
on the _Phrase maker_ stack that appears in the middle of the
screen. (For the moment, ignore the _Start_ block.) You'll see a grid
organized vertically by pitch and horizontally by rhythm.

![widget](./matrix2.svg "Pitch and Rhythm block matrix")

The matrix in the figure above has three _Pitch_ blocks and one
_Rhythm_ block, which is used to create a 3 x 3 grid of pitch and
time.

Note that the default matrix has five _Pitch_ blocks, one _Drum_
block, and two _Mouse_ (movement) blocks. Hence, you will see eight
rows, one for each pitch, drum, and mouse (movement). (A ninth row at
the bottom is used for specifying the rhythms associated with each
note.) Also by default, there are two _Rhythm_ blocks, which specifies
six quarter `(1/4)` notes followed by one half `(1/2)` note.

![widget](./matrix3.svg "matrix")

By clicking on individual cells in the grid, you should hear
individual notes (or chords if you click on more than one cell in a
column). In the figure, three quarter notes are selected (black
cells). First `Re 4`, followed by `Mi 4`, followed by `Sol 4`.

![widget](../header-icons/play-button.svg "play button")

If you click on the _Play_ button (found in the top row of the grid),
you will hear a sequence of notes played (from left to right): `Re 4`,
`Mi 4`, `Sol 4`.

![widget](../header-icons/export-chunk.svg "save button")

Once you have a group of notes (a "chunk") that you like, click on the
_Save_ button (just to the right of the _Play_ button). This will
create a stack of blocks that can used to play these same notes
programmatically. (More on that below.)

You can rearrange the selected notes in the grid and save other chunks
as well.

![widget](../header-icons/sort.svg "sort button")

The _Sort_ button will reorder the pitches in the matrix from highest
to lowest and eliminate any duplicate _Pitch_ blocks.

![widget](../header-icons/erase-button.svg "erase button")

There is also an Erase button that will clear the grid.

Don't worry. You can reopen the matrix at anytime (it will remember
its previous state) and since you can define as many chunks as you
want, feel free to experiment.

Tip: You can put a chunk inside a _Phrase maker_ block to generate
the matrix to corresponds to that chunk.

![widget](./matrix4.svg "usage of octave for a pitch")

The chunk created when you click on the matrix is a stack of
blocks. The blocks are nested: an _Action_ block contains three _Note
value_ blocks, each of which contains a _Pitch_ block. The _Action_
block has a name automatically generated by the matrix, in this case,
chunk. (You can rename the action by clicking on the name.). Each note
has a duration (in this case 4, which represents a quarter note). Try
putting different numbers in and see (hear) what happens. Each note
block also has a pitch block (if it were a chord, there would be
multiple _Pitch_ blocks nested inside the Note block's clamp). Each
pitch block has a pitch name (`Re`, `Mi`, and `Sol`), and a pitch
octave; in this example, the octave is 4 for each pitch. (Try changing
the pitch names and the pitch octaves.)

To play the chuck, simply click on the action block (on the word
action). You should hear the notes play, ordered from top to bottom.

#### <a name="THE-RHYTHM-BLOCK">4.2.2 The Rhythm Block</a>

![widget](./matrix6.svg "the Rhythm block")

_Rhythm_ blocks are used to generate rhythm patterns in the
_Phrase maker_ block. The top argument to the _Rhythm_ block
is the number of notes. The bottom argument is the duration of the
note. In the top example above, three columns for quarter notes
would be generated in the matrix. In the middle example, one column
for an eighth note would be generated. In the bottom example, seven
columns for 16th notes would be generated.

![widget](./matrix7.svg "usage of Rhythm block")

![widget](./matrix8.svg "resulting notes in tabular format")

You can use as many _Rhythm_ blocks as you'd like inside the
_Phrase maker_ block. In the above example, two _Rhythm_
blocks are used, resulting in three quarter notes and six eighth
notes.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725873372253840&run=True)

#### <a name="CREATING-TUPLETS">4.2.3 Creating Tuplets</a>

![widget](./matrix9.svg "simple tuplet")

![widget](./matrix10.svg "tuplet and rhythmic note values")

Tuplets are a collection of notes that get scaled to a specific
duration. Using tuplets makes it easy to create groups of notes that
are not based on a power of 2.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725874435939635&run=True).

In the example above, three quarter notes&mdash;defined in the _Simple
Tuplet_ block&mdash;are played in the time of a single quarter
note. The result is three twelfth notes. (This form, which is quite
common in music, is called a _triplet_. Other common tuplets include a
_quintuplet_ and a _septuplet_.)

![widget](./matrix11.svg "usage of tuplet")

In the example above, the three quarter notes are defined in the
_Rhythm_ block embedded in the _Tuplet_ block. As with the _Simple
Tuplet_ example, they are played in the time of a single quarter
note. The result is three twelfth notes. This more complex form allows
for intermixing multiple rhythms within single tuplet.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1735745904945622&run=True)

![widget](./matrix12.svg "embedding rhythm and Tuplet block")

![widget](./matrix13.svg "tuplet and rhythmic note values")

In the example above, the two _Rhythm_ blocks are embedded in the
_Tuplet_ block, resulting in a more complex rhythm.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725874743559698&run=True)

Note: You can mix and match _Rhythm_ blocks and _Tuplet_ blocks when
defining your matrix.

#### <a name="WHAT-IS-TUPLET">4.2.4 What is a Tuplet?</a>

![tuplet](../charts/TupletChart.svg "tuplet chart")

![tuplet](../charts/TripletChart.svg "triplet chart")

#### <a name="INDIVIDUAL-NOTES">4.2.5 Using Individual Notes</a>

![widget](./matrix14.svg)

You can also use individual notes when defining the grid. These blocks
will expand into _Rhythm_ blocks with the corresponding values.

#### <a name="USING-A-SCALE">4.2.6 Using a Scale of Pitches</a>

![widget](./matrix15.svg)

You can use the _Scalar step_ block to generate a scale of pitches in
the matrix. In the example above, the pitches comprising the G major
scale in the 4th octave are added to the grid. Note that in order to
put the highest note on top, the first pitch is the `Sol` in `Octave
5`. From there, we use `-1` as the argument to the _Scalar step_ block
inside the _Repeat_, working our way down to `Sol` in `Octave
4`. Another detail to note is the use of the _Mode length_ block.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1735824170382853&run=True)

### <a name="rhythms">4.3 Generating Rhythms</a>

The _Rhythm Maker_ block is used to launch a widget similar to the
_Phrase maker_ block. The widget can be used to generate rhythmic
patterns.

![widget](./rhythm1.svg "generating rhythms")

The argument to the _Rhythm Maker_ block specifies the duration that
will be subdivided to generate a rhythmic pattern. By default, it is 1
/ 1, e.g., a whole note.

The _Set Drum_ blocks contained in the clamp of the _Rhythm Maker_
block indicates the number of rhythms to be defined simultaneously. By
default, two rhythm "rulers" are defined. The embedded _Rhythm_ blocks
define the initial subdivision of each rhythm ruler.

![widget](./rhythm2.svg "rhythm maker")

When the _Rhythm Maker_ block is clicked, the _Rhythm Maker_ widget is
opened. It contains a row for each rhythm ruler. An input in the top
row of the widget is used to specify how many subdivisions will be
created within a cell when it is clicked. By default, 2 subdivisions
are created.

![widget](./rhythm3.svg "usage of rhythm maker")

As shown in the above figure, the top rhythm ruler has been divided
into two half-notes and the bottom rhythm ruler has been divided into
three third-notes. Clicking on the _Play_ button to the left of each row
will playback the rhythm using a drum for each beat. The _Play-all_
button on the upper-left of the widget will play back all rhythms
simultaneously.

![widget](./rhythm4.svg "divide cells in rhythm maker")

The rhythm can be further subdivided by clicking in individual
cells. In the example above, two quarter-notes have been created by
clicking on one of the half-notes.

![widget](./rhythm8.svg "tie cells in Rhythm Maker")

By dragging across multiple cells, they become tied. In the example
above, two third-notes have been tied into one two-thirds-note.

![widget](./rhythm5.svg "save stack button")

The _Save stack_ button will export rhythm stacks.

![widget](./rhythm6.svg "stacks of rhythms")

These stacks of rhythms can be used to define rhythmic patterns used
with the _Phrase maker_ block.

![widget](./rhythm7.svg "save drum machine button")

The _Save drum machine_ button will export _Start_ stacks that will
play the rhythms as drum machines.

Another feature of the _Rhythm Maker_ widget is the ability to tap out
a rhythm. By clicking on the _Tap_ button and then clicking on a cell
inside one of the rhythm rulers, you will be prompted (by four tones)
to begin tapping the mouse button to divide the cell into
sub-cells. Once the fourth tone has sounded, a progress bar will run
from left to right across the screen. Each click of the mouse will
define another beat within the cell. If you don't like your rhythm,
use the _Undo_ button and try again.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725875683911786&run=True)

### <a name="modes">4.4 Musical Modes</a>

Musical modes are used to specify the relationship between
[intervals](#327-intervals) (or steps) in a scale. Since
Western music is based on 12 half-steps per octave, modes specify how
many half steps there are between each note in a scale.

By default, Music Blocks uses the _Major_ mode, which, in the
[Key](#343-setting-key-and-mode) of C, maps to the white keys on a
piano. The intervals in the _Major_ mode are `2, 2, 1, 2, 2, 2,
1`. Many other common modes are built into Music Blocks, including, of
course, _Minor_ mode, which uses `2, 1, 2, 2, 1, 2, 2` as its
intervals.

Note that not every mode uses 7 intervals per octave. For example, the
_Chromatic_ mode uses 11 intervals: `1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1`. The _Japanese_ mode uses only 5 intervals: `1, 4,
2, 3, 2`. What is important is that the sum of the intervals
in an octave is 12 half-steps.

The _Mode length_ block will return the number of intervals (scalar
steps) in the current mode.

![widget](./mode1.svg "mode widget")

The _Mode_ widget lets you explore modes and generate custom
modes. You invoke the widget with the _Custom mode_ block. The mode
specified in the _Set key_ block will be the default mode when the
widget launches.

![widget](./mode2.svg "launching widget with Major mode")

In the above example, the widget has been launched with _Major_ mode
(the default). Note that the notes included in the mode are indicated
by the protruding sectors with 'X's, which are arrayed in a circular
pattern of twelve half-steps to complete the octave.

Since the intervals in the _Major_ mode are `2, 2, 1, 2, 2, 2, 1`, the
notes are `0`, `2`, `4`, `5`, `7`, `9`,`11`, and `12` (one octave
above `0`).

The widget controls run along the toolbar at the top. From left to
right are:

_Play all_, which will play a scale using the current mode;

_Save_, which will save the current mode as the _Custom_ mode and save
a stack of _Pitch_ blocks that can be used with the _Phrase Maker_ block;

_Rotate counter-clockwise_, which will rotate the mode
counter-clockwise (See the example below);

_Rotate clockwise_, which will rotate the mode clockwise (See the
example below);

_Invert_, which will invert the mode (See the example below);

_Undo_, which will restore the mode to the previous version; and

_Close_, which will close the widget.

You can also click on individual notes to activate or deactivate them.

Note that the mode inside the _Custom mode_ block is updated whenever
the mode is changed inside the widget.

![widget](./mode3.svg "creating Dorian mode")

In the above example, the _Major_ mode has been rotated counter-clockwise,
transforming it into _Dorian_.

![widget](./mode4.svg "creating Locrian mode")

In the above example, the _Major_ mode has been rotated
clockwise, transforming it into _Locrian_.

![widget](./mode5.svg "creating Phrygian mode")

In the above example, the _Major_ mode has been inverted, transforming
it into _Phrygian_.

Note: The build-in modes in Music Blocks can be found in
[musicutils.js](https://github.com/sugarlabs/musicblocks/blob/master/js/utils/musicutils.js#L68).

![widget](./mode6.svg "phrase maker block")

The _Save_ button exports a stack of blocks representing the mode that
can be used inside the _Phrase maker_ block.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725877046734200&run=True)

### <a name="meters">4.5 Meters</a>

![widget](./meter1.svg "meter widget block")

The _Meter Widget_ block is used to explore strong and weak
beats. Launch the widget with the meter you want to explore. (In the
example, the meter is 4 beats per measure, where each beat is one
quarter note.)

![widget](./meter2.svg "Meter Widget")

Inside the widget, you can click on a sector to indicate a strong
beat. (Clicking on the _X_ will revert the beat to a weak beat.) In
the figure, the first and third beats are strong.

The _Play_ button will play the beat, using a snare drum for strong
beats and a kick drum for weak beats.

![widget](./meter3.svg "on strong beat do blocks")

The _Save_ button will export _On strong beat do_ blocks for each strong beat.

### <a name="pitch-drum">4.6 The Pitch-Drum Matrix</a>

![alt 
 tag](./drum2.svg "Pitch-drum matrix")

The _Set Drum_ block is used to map the enclosed pitches into drum
sounds. Drum sounds are played in a monopitch using the specified drum
sample. In the example above, a `kick drum` will be substituted for
each occurrence of a `sol` `4`.

![widget](./drum5a.svg "pitch-drum matrix 1")

![widget](./drum5.svg "table for pitch-drum matrix")

![widget](./drum6.svg "table for pitch-drum matrix")

![widget](./drum7.svg "pitch-drum matrix 1")

As an experience for creating mapping with the _Set Drum_ block, we
provide the _Drum-Pitch_ Matrix. You use it to map between pitches and
drums. The output is a stack of _Set Drum_ blocks.

### <a name="stairs">4.7 Exploring Musical Proportions</a>

The _Pitch Staircase_ block is used to launch a widget similar to the
_Phrase maker_, which can be used to generate different pitches
using a given pitch and musical proportion.

The _Pitch_ blocks contained in the clamp of the _Pitch Staircase_
block define the pitches to be initialized simultaneously. By default,
one pitch is defined and it have default note "sol" and octave "3".

![widget](./pitchstaircase0.svg "generating arbitrary pitches")

When _Pitch Staircase_ block is clicked, the _Pitch Staircase_ widget is
initialized. The widget contains row for every _Pitch_ block contained
in the clamp of the _Pitch Staircase_ block. The input fields in the top
row of the widget specify the musical proportions used to create new
pitches in the staircase. The inputs correspond to the numerator and
denominator in the proportion respectively. By default the proportion
is 3:2.

![widget](./pitchstaircase1.svg "notes associated with the step in
 the stairs")

![widget](./pitchstaircase2.svg "notes associated with the step in
 the stairs")

![widget](./pitchstaircase3.svg "notes associated with the step in
 the stairs")

Clicking on the _Play_ button to the left of each row will playback
the notes associated with that step in the stairs. The _Play-all_
button on the upper-left of the widget will play back all the pitch
steps simultaneously. A second _Play-all_ button to the right of the
stair plays in increasing order of frequency first, then in
decreasing order of frequency as well, completing a scale.

Clicking the wave icon shown in the widget will subdivide the pitch
stacks according to the musical proportions defined in the widget's
input fields. The _Save stack_ button will export pitch stacks. For
example, in the above configuration, the output from pressing the
_Save stack_ button is shown below:

![widget](./pitchstaircase4.svg "Pitch Stair block")

These stacks can be used with the _Phrase maker_ block to define
the rows in the matrix.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1736204720563059&run=True)

![widget](./pitchstaircase5.svg "Pitch Stair block")

### <a name="slider">4.8 Generating Arbitrary Pitches</a>

The _Pitch Slider_ block is used to launch a widget that is used to
generate arbitrary pitches. It differs from the _Pitch Staircase_
widget in that it is used to create frequencies that vary continuously
within the range of a specified octave.

Each _Sine_ block contained within the clamp of the _Pitch Slider_
block defines the initial pitch for an octave.

![widget](./pitchslider0.svg "Pitch Slider")

![widget](./pitchslider1.svg "Pitch Slider-One Column")

When the _Pitch Slider_ block is clicked, the _Pitch Slider_ widget is
initialized. The widget will have one column for each _Sine_ block in
the clamp. Every column has a slider that can be used to move up or
down in frequency, continuously or in intervals of 1/12th of the
starting frequency. The mouse is used to move the frequency up and
down continuously. Buttons are used for intervals. Arrow keys can also
be used to move up and down, or between columns.

![widget](./pitchslider0a.svg "Pitch Slider Block")

![widget](./pitchslider2.svg "Pitch Slider-Two Column")

Clicking in a column will extract the corresponding _Note_ blocks, for
example:

![widget](./pitchslider3.svg "Pitch Slider-Two Columns Adjusting")

![widget](./pitchslider4.svg " Pitch Slider block")

![widget](./pitchslider5.svg " Pitch Slider block")

### <a name="tempo">4.9 Changing Tempo</a>

The _Tempo_ block is used to launch a widget that enables the user to
visualize Tempo, defined in beats per minute (BPM). When the _Tempo_ block
is clicked, the _Tempo_ widget is initialized.

The _Master Beats per Minute_ block contained in the clamp of the
_Tempo_ block sets the initial tempo used by the widget. This
determines the speed at which the ball in the widget moves back and
forth. If BPM is `60`, then it will take one second for the ball to move
across the widget. A round-trip would take two seconds.

![widget](./tempo0.svg "changing tempo")

The top row of the widget holds the _Play/pause_ button, the _Speed
up_ and _Slow down_ buttons, and an input field for updating the
Tempo.

![widget](./tempo1.svg "changing tempo")

You can also update the tempo by clicking twice in spaced succession
in the widget: the new beats per minute (BPM) is determined as the
time between the two clicks. For example, if there is `1/2` second
between clicks, the new BPM will be set as `120`.

### <a name="timbre">4.10 Custom Timbres</a>

While Music Blocks comes with many built-in instruments, it is also
possible to create custom timbres with unique sound qualities.

![widget](./timbre1.svg "the Timbre widget")

The _Timbre_ block can be used to launch the _Timbre_ widget, which
lets you add synthesizers, oscillators, effects, and filters to create
a custom timbre, which can be used in your Music Blocks programs.

The name of the custom timbre is defined by the argument passed to the
block (by default, `custom`). This name is passed to the _Set timbre_
block in order to use your custom timbre.

![widget](./timbre2.svg "the Timbre widget toolbar")

The _Timbre_ widget has a number of different panels, each of which is
used to set the parameters of the components that define your custom
timbre.

- The _Play_ button, which lets you test the sound quality of your
  custom timbre. By default, it will play `Sol`, `Mi`, `Sol` using the
  combination of filters you define.

![widget](./timbre1a.svg "the notes inside Timbre block")

You can also put notes in the _Timbre_ block to use for testing your
sound. In the example above, a scale will be used for the test.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1736280874343528&run=True)

- The _Save_ button, which will save your custom timbre for use in
  your program.

![widget](./timbre3.svg "select synth")

- The _Synth_ button, which lets you choose between an AM synth, a FM
  synth, or a Duo synth.

![widget](./timbre4.svg "select osc")

- The _Oscillator_ button, which lets you choose between a sine wave,
  square wave, triangle wave, or sawtooth wave. You can also change
  the number of partials.

![widget](./timbre5.svg "set envelope")

- The _Envelope_ button, which lets you change the shape of the sound
  envelope, with controls for attack, decay, sustain, and release.

![widget](./timbre6.svg "select effect")

![widget](./timbre6a.svg "tremolo")

- The _Effects_ button, which lets you add effects to your custom
  timbre: tremelo, vibrato, chorus, phaser, and distortion. When an
  effect is selected, additional controls will appear in the widget.

![widget](./timbre7.svg "select filter")

- The _Filter_ button, which lets you choose between a number of
  different filter types.

- The _Add filter_ button, which lets you add addition filters to your
  custom timbre.

- The _Undo_ button.

As you add synthesizers, effects, and filters with the widget, blocks
corresponding to your choices are added to the _Timbre_ block. This
lets you reopen the widget to fine-tune your custom timbre.

### <a name="keyboard">4.11 The Music Keyboard</a>

The Music Keyboard is used to generate notes by pressing keys of a virtual
keyboard.

When there are no _Pitch_ blocks inside the widget clamp, a keyboard with
all keys between C4 and G5 is created.

![widget](./keyboard1.svg "keyboard block without clamp")

![widget](./keyboard2.svg "keyboard widget without clamp")

When there are _Pitch_ blocks inside the widget clamp, a keyboard with
only those pitches is created.

Click on the keys to hear sounds. Click on the Play button to playback
all of the notes played. Click on the Save button to output code (a
series of _Note_ blocks). The Clear button is used to delete all keys
pressed previously in order to start new.

The MIDI input allows for a using a MIDI device to generate notes.

The metronome feature will generate a beat to enable candence.

### <a name="temperament">4.12 Changing Temperament</a>

_Tempering_ is the process of altering the size of an interval by
making it narrower or wider than pure. It is also possible to change
and create different tuning systems.

![widget](./temperament1.svg "the Temperament block")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725879922065766&run=True)

The _Temperament_ block is used to launch a widget that enables the
user to visualize and edit notes within an octave.

You can select a temperament system from the pie menu which is passed
as an argument to the block. This name is passed to the _Set
temperament_ block in order to play the notes in selected temperament
system. _Starting Pitch_ is the argument of pitch block inside
temperament block. In the above example, starting pitch is `C4`.

![widget](./temperament2.svg "the Temperament widget")

In the above example, selected temperament is _Just Intonation_. Notes
within an octave can be viewed in the form of circle. These circles
represent _pitch numbers_. Note that the pitches that are closer
together in selected temperament system are visually closer and
pitches that are farther apart looks farther.

The information regarding any note can be viewed by clicking on the
respective circle. In the above example, circle (pitch number) `2` is
`D4`. The frequency of note can be changed through edit button (left
hand side corner of note information popup).

![widget](./temperament3.svg "the Temperament widget")

Information regarding notes can also be viewed in the form of a
_table_ as shown in the above example. The table will show all the
information about pitches that lie within an octave. This information
includes _pitch number_, _interval_, _ratio_, _note_, _frequency_ and
_mode_.

The frequency of any note is calculated by `Starting Pitch Frequency`
x `Ratio`.

The widget controls are as follows:

The _Clear_ button at the bottom of the widget will clear all pitches
except for a single `0` from which the user may add pitches.

The _Play all_ button will play through all the pitches in an octave
and then it will play backwards down the pitches.

The _Save_ button will save custom temperament for use in your
program. It will create a _set temperament_ block. This block will
tune the notes attached to it according to the selected temperament.

The _Table_ button is used to toggle between circular and tabular
representation of notes.

The _Add_ button is used to edit notes through different tools:

![widget](./temperament4.svg "Equal Edit tool")

![widget](./temperament4a.svg "Temperament widget with new element")

The `Equal` edit tool is used to make _equal divisions_ between two
pitch numbers. In the above example, two equal divisions are made
between pitch numbers `0` and `1` and the resultant number of notes
within an octave are changed from 12 to 13.

![widget](./temperament5.svg "Ratio Edit tool")

![widget](./temperament5a.svg "Temperament widget with new element")

The `Ratio` tool is used to add notes of specified ratios in such a
way that the resultant pitches wrap inside a single octave. Recursion
represents the number of times notes ratio calculation is repeated. In
the above example, 2 notes are added in pitch space and the resultant
number of notes within an octave are changed from 12 to 14. Frequency
of first pitch is (Starting Pitch Frequency) _ (16/13) and second
pitch is (Starting Pitch Frequency) _ (16/13)².

![widget](./temperament6.svg "Arbitrary Edit tool")

The `Arbitrary` edit tool is used to add a note in an arbitrary
position. In this panel, whenever the user hovers over the outer
circle, a frequency-slider window pops up, allowing the user to add a
note according to a chosen frequency. In the above example, a new note
will be added somewhere between pitch numbers `2` and `3` by adjusting
the frequency slider.

![widget](./temperament7.svg "Octave Space Edit tool")

The `Octave Space` tool is used to edit the octave ratio. The standard
octave space is 2:1. In the above example, octave space will be
changed to 3:1 after clicking on `Done`.

The _Drag_ button will drag the widget.

The _Close_ button will close the widget.

### <a name="oscilloscope">4.13 The Oscilloscope</a>

Music Blocks has an Oscilloscope Widget to visualize the music as it
plays.

![widget](./oscilloscope1.svg "Oscilloscope")

![widget](./oscilloscope2.svg "Oscilloscope")

A separate wave will be displayed for each mouse.
[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725883406989554&run=True)

### <a name="sampler">4.14 The Sampler</a>

![widget](../documentation/sampler_block.svg "Sampler")

You can import sound samples (.WAV files) and use them with the *Set
Instrument" block. The *Sampler\* widget lets you set the center pitch
of your sample so that it can be tuned.

### How to import sound samples ?

By clicking the upload samples icon or by perfoming a drag and drop to sample canvas.

![widget](./sampler1.svg "Sampler Widget")

You can then use the _Sample_ block as you would any input to the _Set
Instrument_ block.

![widget](./sampler2.svg "Sampler Widget")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725883527894966&run=True)

### <a name="arpeggio">4.15 Arpeggio</a>

![widget](../documentation/arpeggiomatrix_block.svg "Arpeggio Widget")

You can design custom sequences to use with the _Arpeggio_ block using
the _Arpeggio_ widget. The widget lets you "paint" intervals that are
then saved to a "custom" chord, which can be used with the _Arpeggio_
block.

The numeric argument to the widget block, `12` in the figure
above, designates the number of columns. The widget always provides a
range of half-steps (one octave in the default a [12-step
equal-temperament tuning](#412-changing-temperament)). (If you are in
a temperament with more notes per ocatve, the grid will expand.) The
rows that represent notes in the current mode are highlighted.

![widget](./arpeggio_widget.svg "Arpeggio_widget")

The horizonal axis is time and the verical axis is half-step offsets
from the base note.

The sequence in the pattern above is `do mi sol do do mi do sol mi
do do sol`.

![widget](../documentation/custom_arpeggio.svg "Custom Arpeggio")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725883915389933&run=True)

## <a name="BEYOND-MUSIC-BLOCKS">5. Beyond Music Blocks</a>

[Previous Section (4. Widgets)](#4-widgets) | [Back to Table of Contents](#table-of-contents) | [Next Section (6. Appendix)](#6-appendix)

Music Blocks is a waypoint, not a destination. One of the goals is to
point the learner towards other powerful tools.

## <a name="LILYPOND">5.1 Lilypond</a>

One such tool is [Lilypond](http://lilypond.org), a music engraving program.

![lilypond](./lilypond1.svg "adding Save as Lilypond block")

The _Save as Lilypond_ option from the Save menu will transcribe your
composition (Only available in Advanced Mode).

Note that if you use a _Print_ block inside of a note, Lilypond will
create a "markup" or annotation for that note. It is a simple way to
add lyrics to your score.

![lilypond](./lilypond2.svg "Save as Lilypond icon")

```
\version "2.18.2"

mouse = {
c'8 c'8 c'8 c'8 c'4 c'4 g'8 g'8 g'8 g'8 g'4 g'4 a'8 a'8 a'8 a'8 a'4
a'4 g'8 g'8 g'8 g'8 g'4 g'4 f'8 f'8 f'8 f'8 f'4 f'4 e'8 e'8 e'8 e'8
e'4 e'4 d'8 d'8 d'8 d'8 d'4 d'4 c'8 c'8 c'8 c'8 c'4 c'4
}

\score {
<<
\new Staff = "treble" {
\clef "treble"
\set Staff.instrumentName = #"mouse" \mouse
}
>>
\layout { }
}
```

![sheet music](./hotdog.png "sheet music")

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1523043053377623&run=True)

## <a name="EXPORTS">5.2 Other Exports</a>

In addition to Lilypond, there are several other export formats
supported, including ABC, MusicXML, WAV, SVG, and PNG.

**ABC** notation is a shorthand form of musical notation. In basic
form it uses the letters A through G, letter notation, to represent
the given notes, with other elements used to place added value on
these – sharp, flat, the length of the note, key, ornamentation (See
https://en.wikipedia.org/wiki/ABC_notation).

**MusicXML** is an XML-based file format for representing Western
musical notation. The format is open, fully documented, and can be
freely used under the W3C Community Final Specification Agreement
(See https://en.wikipedia.org/wiki/MusicXML).

**WAV** (Waveform Audio File Format) is an audio file format standard,
developed by IBM and Microsoft, for storing an audio bitstream on
PCs (See https://en.wikipedia.org/wiki/WAV).

**PNG** (Portable Network Graphics) is a raster-graphics file format
that supports lossless data compression (See
https://en.wikipedia.org/wiki/Portable_Network_Graphics). You can
save your artwork as PNG.

**SVG** (Scalable Vector Graphics) is an Extensible Markup Language
(XML)-based vector image format for two-dimensional graphics with
support for interactivity and animation (See
https://en.wikipedia.org/wiki/Scalable_Vector_Graphics). You can
also save your artwork as SVG.

Note that artwork saved as PNG or SVG can subsequently be imported
into Music Blocks to be used with either the _Show_ or _Avatar_
blocks.

**MIDI** (Musical Instrument Digital Interface) is a technical standard
for communicating musical performance data between electronic instruments,
computers, and other devices. It does not store actual sound but encodes
note, pitch, velocity, and instrument information, making it widely used
for digital music composition and playback (See <https://en.wikipedia.org/wiki/MIDI>).
Exported MIDI files can also be imported, allowing seamless editing and
reuse of musical data.

**Help artwork**

Note for translators: The artwork used by the help widget (and used in
this README file) can be created by typing _Alt-H_ into Music
Blocks. Artwork for each block will be generated and saved by the
browser.

## <a name="JAVASCRIPT">5.3 The JavaScript Editor</a>

There are practical limits to the size and complexity of Music Blocks
programs. At some point we expect Music Blocks programmers to move on
to text-based programming languages. To facilitate this transition,
there is a JavaScript widget that will convert your Music Blocks
program into JavaScript.

The JavaScript code is written and viewed on the **JavaScript Editor**
widget which can be opened by pressing on the "_Toggle JavaScript
Editor_" (`<>`) button in the auxilliary menu.

### Example code

For the block stacks (and mouse art generated after running),

![Example Project](../js/js-export/samples/mode-up-down.png)

[RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1725884337271676&run=True)

the following code is generated:

```
let action = async mouse => {
    await mouse.playNote(1 / 4, async () => {
        await mouse.playPitch("do", 4);
        console.log(mouse.NOTEVALUE);
        return mouse.ENDFLOW;
    });
    let box1 = 0;
    let box2 = 360 / mouse.MODELENGTH;
    for (let i0 = 0; i0 < mouse.MODELENGTH * 2; i0++) {
        await mouse.playNote(1 / 4, async () => {
            if (box1 < mouse.MODELENGTH) {
                await mouse.stepPitch(1);
                await mouse.turnRight(box2);
            } else {
                await mouse.stepPitch(-1);
                await mouse.turnLeft(box2);
            }
            await mouse.goForward(100);
            return mouse.ENDFLOW;
        });
        box1 = box1 + 1;
    }
    return mouse.ENDFLOW;
};
new Mouse(async mouse => {
    await mouse.clear();
    await mouse.setInstrument("guitar", async () => {
        await mouse.setColor(50);
        await action(mouse);
        return mouse.ENDFLOW;
    });
    return mouse.ENDMOUSE;
});
MusicBlocks.run();
```

Here's the complete [API](../js/js-export/samples/sample.js) of
methods, getters, setters.

## <a name="APPENDIX">6. Appendix</a>

[Previous Section (5. Beyond Music Blocks)](#5-beyond-music-blocks) | [Back to Table of Contents](#table-of-contents)

### <a name="BEGINNER_PALETTES">6.1 Beginner Palettes</a>

Looking for a block? The tables below (one for beginner mode and one for advanced mode) list the blocks by the palette where they are found.

### Beginner mode

|    Music     |                         |     | Programming |                     |     |   Graphics   |                 |
| :----------: | :---------------------: | :-: | :---------: | :-----------------: | :-: | :----------: | :-------------: |
|  _Palette_   |        _Blocks_         |     |  _Palette_  |      _Blocks_       |     |  _Palette_   |    _Blocks_     |
|  **Rhythm**  |          note           |     |  **Flow**   |       repeat        |     | **Graphics** |     forward     |
|              |     note value drum     |     |             |       forever       |     |              |      back       |
|              |         silence         |     |             |       if then       |     |              |      left       |
|              |           tie           |     |             |    if then else     |     |              |      right      |
|              |       note value        |     |             |      backward       |     |              |     set xy      |
|  **Meter**   |          meter          |     | **Action**  |       action        |     |              |   set heading   |
|              |    beats per second     |     |             |        start        |     |              |       arc       |
|              | master beats per second |     |             |      broadcast      |     |              |    scroll xy    |
|              |    on every note do     |     |             |     on event do     |     |              |        x        |
|              |      notes played       |     |             |         do          |     |              |        y        |
|              |       beat count        |     |  **Boxes**  |    store in box1    |     |              |     heading     |
|  **Pitch**   |          pitch          |     |             |        box1         |     |   **Pen**    |    set color    |
|              |        pitch G4         |     |             |    store in box2    |     |              |    set shade    |
|              |    scalar step (+/-)    |     |             |        box2         |     |              |  set pen size   |
|              |      pitch number       |     |             |      store in       |     |              |    pen down     |
|              |          hertz          |     |             |         box         |     |              |     pen up      |
|              |         fourth          |     |             |         add         |     |              |      fill       |
|              |          fifth          |     |             |      add 1 to       |     |              |   background    |
|              |     pitch in hertz      |     | **Number**  |       number        |     |              |      color      |
|              |      pitch number       |     |             |       random        |     |  **Media**   |      print      |
|              | scalar change in pitch  |     |             | one of this or that |     |              |      text       |
|              |     change in pitch     |     |             |          +          |     |              |      show       |
| **Interval** |         set key         |     |             |          -          |     |              |     avatar      |
|              |       mode length       |     |             |          x          |     |              |     height      |
|              |       movable do        |     |             |          /          |     |              |      width      |
|              |          third          |     | **Boolean** |          =          |     |              | bottom (screen) |
|              |          sixth          |     |             |          <          |     |              |  top (screen)   |
|              |         chord I         |     |             |          >          |     |              |  left (screen)  |
|              |        chord IV         |     |             |                     |     |              | right (screen)  |
|              |         chord V         |     |             |                     |     | **Sensors**  |  mouse button   |
|              |     set temperament     |     |             |                     |     |              |    cursor x     |
|   **Tone**   |     set instrument      |     |             |                     |     |              |    cursor y     |
|              |         vibrato         |     |             |                     |     |              |      click      |
|              |         chorus          |     |             |                     |     |              |    loudness     |
|              |         tremolo         |     |             |                     |     | **Ensemble** |    set name     |
| **Ornament** |        staccato         |     |             |                     |     |              |   mouse name    |
|              |          slur           |     |             |                     |
|              |     neighbor (+/-)      |     |             |                     |
|  **Volume**  |        crescendo        |     |             |                     |
|              |       decrescendo       |     |             |                     |
|              |    set master volume    |     |             |                     |
|              |    set synth volume     |     |             |                     |
|              |     set drum volume     |     |             |                     |
|   **Drum**   |          drum           |     |             |                     |
|              |      sound effect       |     |             |                     |
|              |        set drum         |     |             |                     |
|  **Widget**  |         status          |     |             |                     |
|              |      phrase maker       |
|              |      C major scale      |
|              |      G major scale      |
|              |      rhythm maker       |
|              |     music keyboard      |
|              |      pitch slider       |
|              |          tempo          |
|              |       custom mode       |
|              |         rhythm          |
|              |      simple tuplet      |

### <a name="ADVANCED_PALETTES">6.2 Advanced Palettes</a>

|     Music     |                            |     |  Programming   |                     |     |   Graphics   |                    |
| :-----------: | :------------------------: | :-: | :------------: | :-----------------: | :-: | :----------: | :----------------: |
|   _Palette_   |          _Blocks_          |     |   _Palette_    |      _Blocks_       |     |  _Palette_   |      _Blocks_      |
|  **Rhythm**   |      note value sol4       |     |    **Flow**    |       repeat        |     | **Graphics** |      forward       |
|               |       note value G4        |     |                |       forever       |     |              |        back        |
|               |       note value +1        |     |                |       if then       |     |              |        left        |
|               |       note value 5 4       |     |                |    if then else     |     |              |       right        |
|               |        note value 7        |     |                |        while        |     |              |       set xy       |
|               |    note value 392 hertz    |     |                |        until        |     |              |    set heading     |
|               |            dot             |     |                |      wait for       |     |              |        arc         |
|               |  multiplicity note value   |     |                |        stop         |     |              |       bezier       |
|               |         skipnotes          |     |                |       switch        |     |              |  control point 1   |
|               |           swings           |     |                |        case         |     |              |  control point 2   |
|               |        milliseconds        |     |                |       default       |     |              |       clear        |
|   **Meter**   |           pickup           |     |                |      duplicate      |     |              |     scroll xy      |
|               |       on strong beat       |     |                |      backward       |     |              |        wrap        |
|               |      on weak beat do       |     |   **Action**   |       action        |     |              |         x          |
|               |          no clock          |     |                |        start        |     |              |         y          |
|               |     whole notes played     |     |                |     start drum      |     |              |      heading       |
|               |        note counter        |     |                |      broadcast      |     |   **Pen**    |     set color      |
|               |       measure count        |     |                |     on event do     |     |              |      set grey      |
|               |        beat factor         |     |                |         do          |     |              |     set shade      |
|               |       current meter        |     |                |        arg1         |     |              |      set hue       |
|   **Pitch**   |        scale degree        |     |                |         arg         |     |              |  set translucency  |
|               |         sharp flat         |     |                |      calculate      |     |              |    set pen size    |
|               |         accidental         |     |                |         do          |     |              |      pen down      |
|               |           unison           |     |                |      calculate      |     |              |       pen up       |
|               |           second           |     |                |         do          |     |              |        fill        |
|               |           third            |     |                |       action        |     |              |    hollow line     |
|               |           sixth            |     |                |      calculate      |     |              |     background     |
|               |          seventh           |     |                |    return to URL    |     |              |      set font      |
|               |         down third         |     |                |       return        |     |              |      pen size      |
|               |         down sixth         |     |   **Boxes**    |    store in box1    |     |              |       color        |
|               |           octave           |     |                |        box1         |     |              |       shade        |
|               |    semi-tone transpose     |     |                |    store in box2    |     |              |        grey        |
|               |          register          |     |                |        box2         |     |              |       black        |
|               |           invert           |     |                |      store in       |     |              |       white        |
|               |            sol             |     |                |    store in box     |     |              |        red         |
|               |             G              |     |                |         box         |     |              |       orange       |
|               |           sargam           |     |                |         box         |     |              |       yellow       |
|               |         accidental         |     |                |         add         |     |              |       green        |
|               |      number of octave      |     |                |      add 1 to       |     |              |        blue        |
|               |      number of pitch       |     |   **Number**   |       number        |     |              |       purple       |
|               |  set pitch number offset   |     |                |       random        |     |  **Media**   |        text        |
|               |            MIDI            |     |                | one of this or that |     |              |        show        |
| **Intervals** |          set key           |     |                |          +          |     |              |       avatar       |
|               |        current key         |     |                |          -          |     |              | note to frequency  |
|               |        current mode        |     |                |          -          |     |              |       hertz        |
|               |        mode length         |     |                |          x          |     |              |     stop media     |
|               |         movable Do         |     |                |          /          |     |              |     open file      |
|               |        define mode         |     |                |         abs         |     |              |       height       |
|               |   scalar interval (+/-)    |     |                |        sqrt         |     |              |       width        |
|               |  semi tone interval (+/-)  |     |                |          ^          |     |              |  bottom (screen)   |
|               |          major 3           |     |                |         mod         |     |              |    top (screen)    |
|               |  scalar interval measure   |     |                |         int         |     |              |   left (screen)    |
|               | semi-tone interval measure |     |  **Boolean**   |        true         |     |              |   right (screen)   |
|               |       interval name        |     |                |          =          |     | **Sensors**  |      keyboard      |
|               |           doubly           |     |                |          <          |     |              |      to ASCII      |
|               |      set temperament       |     |                |          >          |     |              |    mouse bottom    |
|   **Tone**    |       set instrument       |     |                |         or          |     |              |      cursor x      |
|               |         voice name         |     |                |         and         |     |              |      cursor y      |
|               |        audio sample        |     |                |         not         |     |              |        time        |
|               |          vibrato           |     |    **Heap**    |        push         |     |              |    pixel color     |
|               |           chorus           |     |                |         pop         |     |              |        red         |
|               |           phaser           |     |                |      set heap       |     |              |       green        |
|               |          tremolo           |     |                |     index heap      |     |              |        blue        |
|               |         distortion         |     |                |    reverse heap     |     |              |       click        |
|               |          harmonic          |     |                |     empty heap      |     |              |      loudness      |
|               |     weighted partials      |     |                |     heap empty?     |     | **Ensemble** |      set name      |
|               |          partial           |     |                |     heap length     |     |              |     mouse name     |
|               |          FM synth          |     |                |      show heap      |     |              |     new mouse      |
|               |          AM synth          |     | **Dictionary** |      get value      |     |              |    found mouse     |
|               |         duo synth          |     |                |      set value      |     |              |     mouse sync     |
| **Ornament**  |          staccato          |     |                |  get value by name  |     |              |  mouse note value  |
|               |            slur            |     |                |  set value by name  |     |              | mouse pitch number |
|               |       neighbor (+/-)       |     |                |     dictionary      |     |              | mouse notes played |
|               |       neighbor (+/-)       |     |   **Extras**   |        print        |     |              |      mouse x       |
|  **Volume**   |         crescendo          |     |                |       comment       |     |              |      mouse y       |
|               |        decrescendo         |     |                |        wait         |     |              |     set mouse      |
|               |    set relative volume     |     |                |    open project     |     |              |   mouse heading    |
|               |     set master volume      |     |                |     hide blocks     |     |              |    mouse color     |
|               |      set synth volume      |     |                |     show blocks     |     |              |    start mouse     |
|               |      set drum volume       |     |                |    no background    |     |              |     stop mouse     |
|               |            fff             |     |  **Program**   |      set heap       |     |              |  mouse index heap  |
|               |             ff             |     |                |      load heap      |
|               |             f              |     |                |      save heap      |
|               |             mf             |     |                |   set dictionary    |
|               |             mp             |     |                |   load dictionary   |
|               |             p              |     |                |  save heap to App   |
|               |             pp             |     |                | load heap from App  |
|               |            ppp             |     |                |    open palette     |
|               |       master volume        |     |                |    open project     |
|   **Drum**    |            drum            |     |                |     make block      |
|               |        sound effect        |     |                |   connect blocks    |
|               |          set drum          |     |                |     run blocks      |
|               |     map pitch to drum      |     |                |     move block      |
|               |         snare drum         |     |                |    delete block     |
|               |         kick drum          |
|               |         floor tom          |
|               |          cup drum          |
|               |        darbuka drum        |
|               |           hi hat           |
|               |       triangle drum        |
|               |       finger cymbals       |
|               |         ride bell          |
|               |          cow bell          |
|               |           crash            |
|               |            slap            |
|               |            clap            |
|               |           clang            |
|               |           chime            |
|               |          bubbles           |
|               |           bottle           |
|               |            dog             |
|               |          cricket           |
|               |            cat             |
|               |            duck            |
|               |           noise            |
|               |           effect           |
|               |            drum            |
|               |         noisename          |
|               |          tom tom           |
|  **Widget**   |           status           |
|               |        phrase maker        |
|               |       C major scale        |
|               |       G major scale        |
|               |        rhythm maker        |
|               |      pitch staircase       |
|               |       music keyboard       |
|               |     chromatic keyboard     |
|               |        pitch slider        |
|               |      pitch-drum maker      |
|               |       audio sampler        |
|               |           tempo            |
|               |           meter            |
|               |           timbre           |
|               |        temperament         |
|               |           rhythm           |
|               |       simple tuplet        |
|               |          triplet           |
|               |         quintuplet         |
|               |         septuplet          |
|               |           tuplet           |
|               |         whole note         |
|               |         half note          |
|               |        quarter note        |
|               |        eighth note         |
|               |         1/16 note          |
|               |         1/32 note          |
|               |         1/64 note          |
|               |        custom mode         |

[Back to Table of Contents](#table-of-contents)

# Debugging in Music Blocks

_Learning is hard fun._&mdash;Marvin Minsky

_Make the complicated comprehensible_&mdash;Arthur Miller

_Debugging is the learning opportunity of the 21st Century._ &mdash;
Cynthia Solomon

_The important message that comes from ideas about debugging is that
we learn from our mistakes; that the intricate process of making
things work or learning new skills has to do with hypothesizing,
testing, revising, etc._&mdash;Cynthia Solomon

_Sometimes bugs are serendipitously adopted as features worth
perpetuating, sometimes procedures must be constructed to deal with
the phenomena caused by their appearance, and sometimes the bugs and
their side effects need to be removed. But in this pursuit, children
become creative researchers studying behavior, making up theories,
trying out ideas, etc._&mdash;Cynthia Solomon

_6 Stages of Debugging_&mdash;Anonymous

1. That can't happen.
2. That doesn't happen on my machine.
3. That shouldn't happen.
4. Why does that happen?
5. Oh, I see.
6. How did that ever work?

---

Programming is hard. Composing music is also hard. Both programming
and composing involve some trial and error and serendipity. Inevitably
you will make mistakes along the way. Music Blocks provides a number
of mechanisms, reviewed below, to help you explore ideas and find
mistakes.

## <a>TABLE OF CONTENTS</a>

1. [Clicking on an Individual Stack of Blocks](#1-clicking-on-an-individual-stack-of-blocks)
2. [Print and Comment Blocks](#2-print-and-comment-blocks)
3. [Status Widget](#3-status-widget)
4. [Playback Modes](#4-playback-modes)
5. [Show and Hide blocks](#5-show-and-hide-blocks)
6. [Browser Console](#6-browser-console)

## <a>1. Clicking on an Individual Stack of Blocks</a>

The _Play_ button (in top left corner) will run all of the _Start_
blocks simultaneously. (Every Music Blocks project has at least one
_Start_ block). But you can also run an individual stack of code by
clicking on a stack. This lets you test and debug small sections of
code, or, as in the example below, you can play a single voice by
clicking on one of the _Start_ blocks or single phase by clicking on
one of the _Action_ blocks. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732463245651983&run=True)

![alt tag](https://github.com/sugarlabs/musicblocks/blob/master/images/startblocks_debug_guide.png "Start Blocks")

## <a>2. Print and Comment Blocks</a>

[Back to Table of Contents](#table-of-contents)

The _Print_ block (found on the _Extras_ palette) can be used to print
a message while running a program. It is useful to determine if a
section of code is being executed when expected or if a box or
parameter contains an expected value.

![alt tag](https://github.com/sugarlabs/musicblocks/blob/master/images/print_example2_debug_guide.png "Print Block")

The _Print_ block is used to display the number of whole notes played,
in this case, `1/4 + 1/4 + 1/2`, which adds up to `1`, which is
displayed at the top of the browser window. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732474452574359&run=True)

The _Comment_ block (also found on the _Extras_ palette) is similar to
the _Print_ block, except it only prints a message when the program is
being run in _Playback Slow_ mode (See below). Comments are also
written to the browser console. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732825564345176&run=True)

![Comment Block](./images/Comment_block_DebuggingMd.svg "Comment Block")

## <a>3. Status Widget</a>

[Back to Table of Contents](#table-of-contents)

![Status Widget Block](./images/Status_widget_debuggingMd.svg "Status Widget Block")

![alt tag](https://github.com/sugarlabs/musicblocks/blob/master/images/status_example_debug_guide.png "Status in tabular form")

The _Status widget_ is a tool for inspecting the status of Music
Blocks as it is running. By default, the key, BPM, and volume are
displayed. Also, each note is displayed as it is played. There is one
row per voice in the status table. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732541757152077&run=True)

Additional _Print_ blocks can be added to the _Status_ widget to
display additional music factors, e.g., duplicate, transposition,
skip, [staccato](#MORE-TRANSFORMATIONS),
[slur](#MORE-TRANSFORMATIONS), and [graphics](#GRAPHICS) factors,
e.g., x, y, heading, color, shade, grey, and pensize.

![Additional Programming within the Status Widget Block](./images/Status_Widget_additional_programming_DebuggingMd.svg "Additional Programming within the Status Widget Block")

You can do additional programming within the status block. In the
example above, `whole notes played` is multiplied by `4` (e.g. quarter notes)
before being displayed. [RUN LIVE](https://musicblocks.sugarlabs.org/index.html?id=1732553086132345&run=True)

## <a>4. Playback Modes</a>

[Back to Table of Contents](#table-of-contents)

Clicking on the Play button will play your program at full speed.
(It will also hide the blocks while the program runs, which improves
performance.) But there are two other playback modes.

On the Secondary Menu, there are two other Play buttons.

During _Playback Slow_ mode the program will pause between the execution
of each block and the block being executed will be highlighted. This is
useful for following program flow, ensuring that the sequence of blocks
being executed is what you expect. In addition, the value stored in any
box or parameter is displayed on the block as the program runs, so you
can "inspect" program elements as the program runs.

_Run Step by Step_ advances one block per button press.

## <a>5. Show and Hide blocks</a>

[Back to Table of Contents](#table-of-contents)

The _Show_ and _Hide_ blocks (found on the _Extras_ palette) are
useful for setting
"[breakpoints](https://en.wikipedia.org/wiki/Breakpoint)" in your
program to debug a specific section of code. By putting a _Show_ block
at the start of a problematic section of code and a _Hide_ block at
the end of the section, your program can be run full speed until it
gets to the _Show_ block. Then the blocks are displayed and
run in _Playback Slow_ mode. When the _Hide_ block is encountered, the
blocks are hidden and the program resumes running at full speed.

## <a>6. Browser Console</a>

As Music Blocks runs, some debugging information is written to the
browser console, such as the notes being played and comments (See the
_Comment_ block above). The console can be accessed by typing
`Ctrl-Shift-J` on most web browsers.

![alt tag](https://github.com/sugarlabs/musicblocks/blob/master/images/browserconsole_debug_guide.png "Console blocks")

Shown above is the console output from three notes: `sol mi sol`.

[Back to Table of Contents](#table-of-contents)

# Guide to Programming with Turtle Art

Turtle Blocks expands upon what children can do with Logo and how it
can be used as the underlying motivator for “improving” programming
languages and programmable devices.

In this guide, we illustrate this point by both walking the reader
through numerous examples, but also by discussing some of our favorite
explorations of Turtle Blocks, including multi-media, the Internet
(both as a forum for collaboration and data collection), and a broad
collection of sensors.

## Getting Started

Turtle Blocks Javascript is designed to run in a browser. Most of the
development has been done in Chrome, but it should also work in
Firefox. You can run it from a [server maintained by Sugar
Labs](http://turtle.sugarlabs.org), from the [github
repo](http://sugarlabs.github.io/turtleblocksjs), or by setting up a
[local
server](https://github.com/sugarlabs/turtleblocksjs/blob/master/server.md).

You can also open it directly from `file://` with some browsers, e.g.,
FireFox.

Once you've launched it in your browser, start by clicking on (or
dragging) blocks from the _Turtle_ palette. Use multiple blocks to
create drawings; as the turtle moves under your control, colorful
lines are drawn.

You add blocks to your program by clicking on or dragging them from
the palette to the main area. You can delete a block by dragging it
back onto the palette. Click anywhere on a "stack" of blocks to start
executing that stack or by clicking in the _Rabbit_ (fast) or _Turtle_
(slow) on the Main Toolbar. The _Snail_ will step through your
program, one block per click.

For more details on how to use Turtle Blocks JS, see [Using Turtle
Blocks
JS](http://github.com/sugarlabs/turtleblocksjs/tree/master/documentation)
for more details.

## ABOUT THIS GUIDE

Many of the examples given in the guide have links to code you can
run. Look for RUN LIVE links that will take you to
http://turtle.sugarlabs.org.

## TO SQUARE

The traditional introduction to Logo has been to draw a square. Often
times when running a workshop, I have the learners form a circle
around one volunteer, the "turtle", and invite them to instruct the
turtle to draw a square. (I coach the volunteer beforehand to take
every command literally, as does our graphical turtle.) Eventually the
group converges on "go forward some number of steps", "turn right (or
left) 90 degrees", "go forward some number of steps", "turn right (or
left) 90 degrees", "go forward some number of steps", "turn right (or
left) 90 degrees", "go forward some number of steps". It is only on
rare occasions that the group includes a final "turn right (or left)
90 degrees" in order to return the turtle to its original
orientation. At this point I introduce the concept of "repeat" and
then we start in with programming with Turtle Blocks.

## I. Turtle Basics

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics1.svg' />

A single line of length 100 [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523359934621848&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics2.svg' />

Changing the line length to 200 [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523360071975585&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics3.svg' />

Adding a right turn of 90 degrees. Running this stack four times
produces a square. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523360268417654&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics4.svg' />

Forward, right, forward, right, ... [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523360327901636&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics5.svg' />

Using the _Repeat_ block from the _Flow_ palette [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523294074349148&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics6.svg' />

Using the _Arc_ block to make rounded corners [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523360547665676&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics7.svg' />

Using the _Fill_ blocks from the Pen palette to make a solid square
(what ever is drawn inside the _Fill_ clamp will be filled upon
exiting the clamp.) [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523360674936456&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics8.svg' />

Changing the color to 70 (blue) using the _Set Color_ block from the
_Pen_ palette [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523360821674406&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/basics9.svg' />

Using the _Random_ block from the _Numbers_ palette to select a random
color (0 to 100) [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523360917773878&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/background.svg' />

Use the _Background_ block to set the background color to the current
pen color. Note that if you do not subsequently change the pen color
after you set the background, you will not be able to see what you are
drawing as your "ink" will be the same color as your "paper". [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1581264197757866&run=True)

## A SHOEBOX

When explaining boxes in workshops, I often use a shoebox. I have
someone write a number on a piece of paper and put it in the
shoebox. I then ask repeatedly, "What is the number in the box?" Once
it is clear that we can reference the number in the shoebox, I have
someone put a different number in the shoebox. Again I ask, "What is
the number in the box?" The power of the box is that you can refer to
it multiple times from multiple places in your program.

## II. Boxes

Boxes let you store an object, e.g., a number, and then refer to the
object by using the name of the box. (Whenever you name a box, a new
block is created on the Boxes palette that lets you access the content
of the box.) This is used in a trivial way in the first example below:
putting 100 in the box and then referencing the box from the Forward
block. In the second example, we increase the value of the number
stored in the box so each time the box is referenced by the Forward
block, the value is larger.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/boxes1.svg' />

Putting a value in a _Box_ and then referring to the value in _Box_
[RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523361053378823&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/boxes2.svg' />

We can change the value in a _Box_ as the program runs. Here we add 10
to the value in the _Box_ with each iteration. The result in this case
is a spiral, since the turtle goes forward further with each
step. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523361248940557&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/boxes3.svg' />

If we want to make a more complex change, we can store in the _Box_ some
computed value based on the current content of the _Box_. Here we
multiply the content of the box by 1.2 and store the result in the
_Box_. The result in this case is also a spiral, but one that grows
geometrically instead of arithmetically.

In practice, the use of boxes is not unlike the use of keyword-value
pairs in text-based programming languages. The keyword is the name of
the _Box_ and the value associated with the keyword is the value
stored in the _Box_. You can have as many boxes as you'd like (until
you run out of memory) and treat the boxes as if they were a
dictionary. Note that the boxes are global, meaning all turtles and
all action stacks share the same collection of boxes. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523368886737682&run=True)

## III. Action Stacks

With Turtle Blocks there is an opportunity for the learner to expand
upon the language, taking the conversation in directions unanticipated
by the Turtle Block developers.

_Action_ stacks let you extend the Turtle Blocks language by defining
new blocks. For example, if you draw lots of squares, you may want a
block to draw squares. In the examples below, we define an action
that draws a square (repeat 4 forward 100 right 90), which in turn
results in a new block on the _Actions_ palette that we can use whenever
we want to draw a square. Every new _Action_ stack results in a new
block.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/actions1.svg' />

Defining an action to create a new block, "_Square_" [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523369101107025&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/actions2.svg' />

Using the "_Square_" block [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523369182696942&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/actions3.svg' />

The _Do_ block lets you specify an action by name. In this example, we
choose "one of" two names, "_Square_" and "_Triangle_" to determine which
action to take. [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523369272178072&run=True)

## IV. Parameters

Parameter blocks hold a value that represents the state of some turtle
attribute, e.g., the x or y position of the turtle, the heading of the
turtle, the color of the pen, the size of the pen, etc. You can use
parameter blocks interchangeably with number blocks. You can change
their values with the _Add_ block or with the corresponding set blocks.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/parameters1.svg' />

Using the _Heading_ parameter, which changes each time the turtle
changes direction, to change the color of a spiral [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523369515049913&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/parameters2.svg' />

"Squiral" by Brian Silverman uses the _Heading_ and _X_ parameter
blocks. [RUN
LIVE](https://walterbender.github.io/musicblocks/index.html?id=1523410445476847&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/parameters3.svg' />

Often you want to just increment a parameter by 1. For this, use the
_Add-1-to_ block. [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523369660208921&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/parameters4.svg' />

To increment (or decrement) a parameter by an arbitrary value, use the
_Add-to_ block. [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523370184642548&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/parameters5.svg' />

To make other changes to a parameter based on the current value, use
the parameter's _Set_ block. In this example, the pen size is doubled
with each step in the iteration. [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523370273985275&run=True)

## V. Conditionals

Conditionals are a powerful tool in computing. They let your program
behave differently under differing circumstances. The basic idea is
that if a condition is true, then take some action. Variants include
if-then-else, while, until, and forever. Turtle Blocks provides
logical constructs such as equal, greater than, less than, and, or,
and not.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/conditionals1.svg' />

Using a conditional to select a color: Once the heading > 179, the
color changes. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523370501577900&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/conditionals2.svg' />

Conditionals along with the _Random_ block can be used to simulate a
coin toss. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523370743897698&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/conditionals3.svg' />

A coin toss is such a common operation that we added the _One-of_ block
as a convenience. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523370862902481&run=True)

## VI. Multimedia

Turtle Blocks provides rich-media tools that enable the incorporation
of sound, typography, images, and video.

At the heart of the multimedia extensions is the _Show_ block. It can be
used to show text, image data from the web or the local file system,
or a web camera. Other extensions include blocks for synthetic speech,
tone generation, and video playback.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/media1.svg' />

Using the _Show_ block to display text; the orientation of the text
matches the orientation of the turtle. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523370990567304&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/media2.svg' />

You can also use the _Show_ block to show images. Clicking on the Image
block (left) will open a file browser. After selecting an image file
(PNG, JPG, SVG, etc.) a thumbnail will appear on the _Image_ block
(right).

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/media3.svg' />

The _Show_ block in combination with the _Camera_ block will capture and
display an image from a webcam. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523371139976408&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/media4.svg' />

The _Show_ block can also be used in conjunction with a URL that
points to media. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523371406381048&run=True)

## VII. Sensors

Seymour Papert’s idea of learning through making is well supported in
Turtle Blocks. According to Papert, “learning happens especially
felicitously in a context where the learner is consciously engaged in
constructing a public entity, whether it’s a sand castle on the beach
or a theory of the universe”. Research and development that supports
and demonstrates the children’s learning benefits as they interact
with the physical world continues to grow. In similar ways, children
can communicate with the physical world using a variety of sensors in
Turtle Blocks. Sensor blocks include keyboard input, sound, time,
camera, mouse location, color that the turtle sees. For example,
children may want to build a burglar alarm and save photos of the
thief to a file. Turtle Blocks also makes it possible to save and
restore sensor data from a file. Children may use a “URL” block to
import data from a web page.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/sensors1.svg' />

Using sensors. The _Loudness_ block is used to determine if there is an
intruder. A loud sound triggers the alarm action: the turtle shouts
“intruder” and takes a picture of the intruder.

Teachers from the Sugar community have developed extensive collection
of examples using Turtle Block sensors. Guzmán Trinidad, a physics
teacher from Uruguay, wrote a book, _Physics of the XO_, which includes
a wide variety of sensors and experiments. Tony Forster, an engineer
from Australia, has also made remarkable contributions to the
community by documenting examples using Turtle Blocks. In one example,
Tony uses the series of switches to measure gravitational
acceleration; a ball rolling down a ramp trips the switches in
sequence. Examining the time between switch events can be used to
determine the gravitational constant.

One of the typical challenges of using sensors is calibration. This is
true as well in Turtle Blocks. The typical project life-cycle
includes: (1) reading values; (2) plotting values as they change over
time; (3) finding minimum and maximum values; and finally (4)
incorporating the sensor block in a Turtle program.

## Example: Paint

As described in the Sensors section, Turtle Blocks enables the
programmer/artist to incorporate sensors into their work. Among the
sensors available are the mouse button and mouse x and y
position. These can be used to create a simple paint program, as
illustrated below. Writing your own paint program is empowering: it
demystifies a commonly used tool. At the same time, it places the
burden of responsibility on the programmer: once we write it, it
belongs to us, and we are responsible for making it cool. Some
variations of paint are also shown below, including using microphone
levels to vary the pen size as ambient sound-levels change. Once
learners realize that they can make changes to the behavior of their
paint program, they become deeply engaged. How will you modify paint?

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/paint1.svg' />

In its simplest form, paint is just a matter of moving the turtle to
wherever the mouse is positioned. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523371509276932&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/paint2.svg' />

Adding a test for the mouse button lets us move the turtle without
leaving a trail of ink. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523371673939089&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/paint3.svg' />

In this example, we change the pen size based on the volume of
microphone input. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523371754657228&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/paint4.svg' />

In another example, inspired by a student in a workshop in Colombia,
we use time to change both the pen color and the pen size. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523371935195761&run=True)

## Example: Slide Show

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/slideshow1.svg' />

Why use Powerpoint when you can write Powerpoint? In this example, an
Action stack is used to detect keyboard input: if the keyboard value
is zero, then no key has been pressed, so we call the action again. If
a key is pressed, the keyboard value is greater than zero, so we
return from the action and show the next image.

## Example: Keyboard

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/keyboard.svg' />

In order to grab keycodes from the keyboard, you need to use a _While_
block. In the above example, we store the keyboard value in a box,
test it, and if it is > 0, return the value. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523376704342158&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/keyboard2.svg' />

If you want to convert the keycode to a alphanumeric character, you
need to use the _To ASCII_ block. E.g., _toASCII(65) = A_ [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523377042822413&run=True)

## VIII. Turtles, Sprites, Buttons, and Events

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/turtles1.svg' />

A separate turtle is created for each _Start_ block. The turtles run
their code in parallel with each other whenever the _Run_ button is
clicked. Each turtle maintains its own set of parameters for position,
color, pen size, pen state, etc. In this example, three different
turtles draw three different shapes. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523377203344616&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/turtles2.svg' />

Custom graphics can be applied to the turtles, using the _Shell_ block
on the _Media_ palette. Thus you can treat turtles as sprites that can
be moved around the screen. In this example, the sprite changes back
and forth between two states as it moves across the screen. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523377357693679&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/turtles3.svg' />

Turtles can be programmed to respond to a "click" event, so they can
be used as buttons. In this example, each time the turtle is clicked,
the action is run, which move the turtle to a random location on the
screen. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523377513682595&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/turtles4.svg' />

Events can be broadcast as well. In this example, another variant on
Paint, turtle "buttons", which listen for "click" events, are used to
broadcast change-color events. The turtle used as the paintbrush is
listening for these events. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523378142359724&run=True)

## IX. Advanced Actions

Sometime you might want an action to not just run a stack of blocks
but also to return a value. This is the role of the return block. If
you put a return block into a stack, then the action stack becomes a
calculate stack.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/actions4.svg' />

In this example, a _Calculate_ stack is used to return the current
distance of the turtle from the center of the screen. Renaming an
action stack that has a _Return_ block will cause the creation of a new
block in the _Actions_ palette that can be used to reference the return
value: in this case, a _Distance_ block is created. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523383380320451&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/actions6.svg' />

You can also pass arguments to an _Action_ stack. In this example, we
calculate the distance between the turtle and an arbitrary point on
the screen by passing x and y coordinates in the _Calculate_
block. You add additional arguments by dragging them into the "clamp".

Note that args are local to _Action_ stacks, but boxes are not. If you
planned to use an action in a recursive function, you had best avoid
boxes. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523382801625028&run=True)

## Example: Fibonacci

Calculating the Fibonacci sequence is often done using a recursive
method. In the example below, we pass an argument to the _Fib_ action,
which returns a value if the argument is &lt; 2; otherwise it returns
the sum of the result of calling the _Fib_ action with argument - 1 and
argument - 2.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/fibonacci1.svg' />

Calculating Fibonacci [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523388667520324&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/fibonacci2.svg' />

In the second example, we use a _Repeat_ loop to generate the first six
Fibonacci numbers and use them to draw a nautilus.

Draw a nautilus [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523388775236172&run=True)

## Example: Reflection Paint

By combining multiple turtles and passing arguments to actions, we can
have some more fun with paint. In the example below, the _Paint Action_
uses _Arg 1_ and _Arg 2_ to reflect the mouse coordinates about the y and
x axes. The result is that the painting is reflected into all four
quadrants.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/turtles5.svg' />

Reflection Paint [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523389168734406&run=True)

## X. Advanced Boxes

Sometimes it is more convenient to compute the name of a _Box_ than to
specify it explicitly. (Note that the _Do_ block affords a similar
mechanism for computing the names of actions.)

In the following examples, we use this to accumulate the results of
toss a pair of dice 1600 times (example inspired by Tony Forster).

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/boxes4.svg' />

Rather than specifying a box to hold each possible result (2 through
12), we use a _Box_ as a counter (index) and create a box with the name
of the current value in the counter and store in that box a value of 0.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/boxes5.svg' />

Next we add an _Action_ to toss the dice 1600 times. To simulate tossing
a pair of dice, we sum two random numbers between 1 and 6. We use the
result as the name of the box we want to increment. So for example, if
we throw a 7, we add one to the _Box_ named 7. In this way we increment
the value in the appropriate _Box_.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/boxes6.svg' />

Finally, we plot the results. Again, we use a _Box_ as a counter ("index")
and call the _Plot Action_ in a loop. In the _Bar Action_, we draw a
rectangle of length value stored in the _Box_ with the name of the
current value of the index. E.g., when the value in the index _Box_ equals
2, the turtle goes forward by the value in _Box 2_, which is the
accumulated number of times that the dice toss resulted in a 2; when
the value in the _Index Box_ is 3, the turtle goes forward by the value
in _Box 3_, which is the accumulated number of times that the dice toss
resulted in a 3; etc. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523299313972510&run=True)

## XI. The Heap

Sometimes you need a place to temporarily store data. One way to do it
is with boxes (as mentioned at the end of the Boxes section of this
guide, they can be used as a dictionary or individual keyword-value
pairs). However, sometimes it is nice to simply use a heap.

A heap is a essential a pile. The first thing you put on the heap is
on the bottom. The last thing you put on the heap is on the top. You
put things onto the heap using the _Push_ block. You take things off of
the heap using the _Pop_ block. In Turtle Blocks, the heap is first-in
last-out (FILO), so you pop things off of the heap in the reverse
order in which you put them onto the heap.

There is also an _Index_ block that lets you refer to an item in the
heap by an index. This essentially lets you treat the heap as an
array. Some other useful blocks include a block to empty the heap, a
block that returns the length of the heap, a block that saves the heap
to a file, and a block that loads the heap from a file.

In the examples below we use the heap to store a drawing made with a
paint program similar to the previous examples and then to playback
the drawing by popping points off of the heap.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/heap1.svg' />

In the first example, we simply push the turtle position whenever we
draw, along with the pen state. Note since we pop in the reverse order
that we push, we push y, then x, then the mouse state.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/heap2.svg' />

In the second example, we pop pen state, x, and y off of the heap and
playback our drawing. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523389420306919&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/heap3.svg' />

Use the _Save Heap_ block to save the state of the heap to a file. In
this example, we save our drawing to a file for playback later. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523390553182986&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/heap4.svg' />

Use the _Load Heap_ block to load the heap from data saved in a
file. In this example, we playback the drawing from data stored in a
file. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523389601597904&run=True)

## XII. Extras

The _Extras_ palette is full of utilities that help you use your
project's output in different ways.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/extras1.svg' />

The _Save as SVG_ block will save your drawing as simple vector graphics
(SVG), a format compatible with HTML5 and many image manipulation
programs, e.g., Inkscape. In the example above, we use it to save a
design in a from that can be converted to STL, a common file format
used by 3D printers. A few things to take note of: (1) the _No
Background_ block is used to suppress the inclusion of the background
fill in the SVG output; (2) _Hollow lines_ are used to make graphic have
dimension; and (3) the _Save as SVG_ block writes to the Downloads
directory on your computer. (Josh Burker introduced me to Tinkercad, a
website that can be used to convert SVG to STL.) [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523390883477748&run=True)

The _New Turtle_ block is used to create new turtles on the fly. The
_Set Turtle_ block is used to run blocks by a selected turtle. In the
example below, 10 turtles are created on the fly and each turtle is
then set on a random walk across the screen. Note that the _Found
Turtle_ block is used to ensure that the each new turtle is _ready_
before issuing commands. (Creating a turtle is not instantaneous and
the _New Turtle_ block does not block program flow waiting for the
turtle to be created.) [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1525211505767290&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/extras2.svg' />

An alternative to using the _Found Turtle_ block is to use the _Event_ block. When a new turtle is created, an event with the name of the turtle is broadcast (See the example below).

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/extras3.svg' />

## XIII. Debugging Aids

Probably the most oft-used debugging aid in any language is the print
statement. In Turtle Blocks, it is also quite useful. You can use it
to examine the value of parameters and variables (boxes) and to
monitor progress through a program.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/debugging1.svg' />

In this example, we use the addition operator to concatinate strings
in a print statement. The mouse x + ", " + mouse y are printed in the
inner loop. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523391206069261&run=True)

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/status1.svg' />

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/status2.svg' />

There is also a _Status_ widget that can be programmed to show various
paramters as per the figures above. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1528388082677564&run=True)

Parameter blocks, boxes, arithmetic and boolean operators, and many
sensor blocks will print their current value as the program runs when
running in "slow" or "step-by-step" mode, obviating the need to use
the Print block in many situations.

The _Wait_ block will pause program execution for some number (or
fractions) of seconds.

The _Hide_ and _Show_ blocks can be used to set "break points". When a
_Hide_ block is encountered, the blocks are hidden and the program
proceeds at full speed. When a _Show_ block is encountered, the program
proceeds at a slower pace an the block values are shown.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/debugging2.svg' />

A _Show_ block is used to slow down execution of the code in an _Action_
stack in order to facilitate debugging. In this case, we slow down
during playback in order to watch the values popped off the heap. [RUN
LIVE](https://turtle.sugarlabs.org/index.html?id=1523391034295213&run=True)

## XIV. Advanced Color

The internal representation of color in Turtle Blocks is based on the
[Munsell color
system](http://en.wikipedia.org/wiki/Munsell_color_system). It is a
three-dimensional system: (1) hue (red, yellow, green, blue, and
purple), (2) value (black to white), and (3) chroma (gray to vivid).

There are parameters for each color dimension and corresponding
"setters". All three dimensions have been normalized to run from 0 to 100. For Hue, 0 maps to Munsell 0R. For Value, 0 maps to Munsell value
0 (black) and 100 maps to Munsell value 10 (white). For chroma, 0 maps
to Munsell chroma 0 (gray) and 100 maps to Munsell chroma 26 (spectral
color).

A note about Chroma: In the Munsell system, the maximum chroma of
each hue varies with value. To simplify the model, if the chroma
specified is greater than the maximum chroma available for a hue/value
pair, the maximum chroma available is used.

The _Set Color_ block maps the three dimensions of the Munsell color
space into one dimension. It always returns the maximum value/chroma
pair for a given hue, ensuring vivid colors. If you want to more
subtle colors, be sure to use the _Set Hue_ block rather than the _Set
Color_ block.

<img src='https://rawgithub.com/sugarlabs/turtleblocksjs/master/guide/color1.svg' />

Color vs. hue example [RUN LIVE](https://turtle.sugarlabs.org/index.html?id=1523391601724568&run=True)

To set the background color, use the _Background_ block. It will set the
background to the current hue/value/chroma triplet.

## XV. Plugins

There are a growing number of extensions to Turtle Blocks in the from
of plugins. See
[Plugins](http://github.com/sugarlabs/turtleblocksjs/tree/master/plugins)
for more details.

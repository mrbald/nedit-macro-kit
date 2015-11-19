[NEdit](http://www.nedit.org/) Macro for programmers, basically turning the NEdit text editor into a full-featured IDE. Multi-language, Multi platform, easy to configure, featuring functionalities like the "expander", completion, ctags dialog, comment/uncomment, build and jump to error, multiple files search&replace...

Note for Windows user: NEdit requires Cygwin.

Any comment/feedback/bug:
  * use the Wiki
  * or send me ([Frank Perbet](http://www.frank.perbet.org/)) an email at _frank.perbet@laposte.net_



&lt;hr&gt;


# Briefly #
<a href='http://evasion.inrialpes.fr/Membres/Frank.Perbet/nedit/english_presentation.html'>old web page</a>

To use those macros you'll need NEdit version 5.4 or higher (to obtain the version number, use: nedit -V).

These macros are dedicated to all software developpers. Personally, I use them to write C++, python and LaTeX, but you can use them to code in any programming langages (Java, Perl, Html,...). Here is the feature list:
<li>completion (which can use dictionary, or tags file).<br>
<li>expander... This is my favorite!</li>
<li>IDE features like compilation and jump to error line.</li>
<li>a powerful search and replace tool using the "grep" command.</li>

<br>
<br>
<hr><br>
<br>
<br>
<h1>Install</h1>

<ul>
<li>get the tarball and copy it on your home directory so that you can see the file ~/.nedit/nedit.rc</li>
<li>you need set the NEDIT_HOME environment variable to $HOME/.nedit</li>
</ul>

<br>
<br>
<hr><br>
<br>
<br>
<h1>General issue</h1>

<h2>NEdit server</h2>

<p>This Nedit Macro-Kit fully work with the nedit-server binary. It means that you must use nc (or ncl, or nedit-nc, depending on your OS) instead of NEdit.</p>

<h2>Working directory</h2>

<p>Some macros have to know the directory in which they must be executed (for compilation by example). These working directory can be handle in three different ways:</p>
<p><em>Local mode</em>: theworking directory is always the directory of the current file.<em></em></p>
<p><em>Global mode</em>: In this mode, the working directory is always the same, and do not depends on the current file.</p>
<p><em>Multi-mode</em>: in this mode, there are several global working directories. When NEdit doesn't recognize any of them, it chooses the current directory. NEdit recognize one of the working directories when the current file path is in its sub-hierarchy</p>
<ul>
<li><strong>macro_paramaters.nm file</strong></li>
</ul>
<p>It's a very good idea to have a look at the file macro_paramaters.nm. It contains a lot of deflaut parameters which can be modify or extend. To open that file, use the window background menu : "Customize -&gt; change macro parameters".</p>

<h2>Shorcuts</h2>

<p>Almost all the Nedit Macro-Kit macros are associated with a shortcut. Unfortunately, the X-server often use all of them by default. To solve this problem, it can be a good idea to remove all the X-server shortcuts that you never use.</p>


<br>
<br>
<hr><br>
<br>
<br>
<h1>Documentation</h1>

<h2>MACRO MENU:</h2>
<ul>
<li><strong>Edit (Mk) :</strong></li>
</ul>
<p>copy line (Ctrl+Alt+C) : Copy the current line.<br />cut line (Ctrl+Alt+X) : Cut the current line. If the current line is empty, the clipboard is not modified.<br />paste line (Ctrl+Alt+V) : Paste (idem CTRL+V).<br />Duplicate block (Alt+D) : Duplicate the selection. If there is no selection, duplicate the current line.<br />Duplicate and comment block (Ctrl+Alt+D) : Duplicate and comment the selection. If there is no selection, duplicate and comment the current line.<br />Fill selection (Ctrl+Alt+F) : Fill selection with a given string.<br />replace in rectangular selection (Alt+J) : Replace each line of a rectangular selection with a given string.<br />replace by selection (Ctrl+B) : Replace the selection with the clipboard.<br />enumeration : Enumerate selection (insert a number at the beginning of each line).<br />get regex : get all the match in a document for the given regular expression.<br />get file list (Shift+Ctrl+Alt+L) : copy a file list into clipboard</p>
<ul>
<li><strong>Edit (Mk)&gt;Structural characters :</strong></li>
</ul>
<p>Add block {} (Alt+B) : Insert two curly braces. If a selection exist, put this selection into curly braces.<br />Add (...) (Shift+Alt+0) : Put the selection in parentheses (or add empty parentheses if no selection).<br />Add {...} (Shift+Alt+Bracketright) : Put the selection in curly braces (or add empty curly braces if no selection).<br />Add [...] (Alt+Bracketright) : Put the selection in square brackets (or add empty square brackets if no selection).<br />Add " " (Shift+Alt+Apostrophe) : Put the selection in guillemets (or add empty guillemets if no selection).<br />Add ' ' (Alt+Apostrophe) : Put the selection in apostrophes (or add empty apostrophes if no selection).<br />Add <code> </code> (Shift+Ctrl+Grave) : Put the selection in grave accents (or add empty grave accents if no selection).<br />Add &lt;.. (Shift+Alt+Period) : Put the selection in inferior/superior (or add empty inferior/superior if no selection).<br />Add <code>` (Alt+Grave) : Put the selection in</code><code> (or add empty </code>` if no selection).<br />Add $ (Shift+Alt+4) : Put the selection in $ (or add empty $ if no selection).<br />Add  (Shift+Alt+8) : Put the selection in  (or add empty  if no selection).<br />Add \\\\ (Alt+Backslash) : Put the selection in \\\\ (or add empty \\\\ if no selection).</p>
<ul>
<li><strong>Move (Mk) :</strong></li>
</ul>
<p>discrete scroll up (Alt+Prior) : Scroll up without moving the cursor.<br />discrete scroll down (Alt+Next) : Scroll down without moving the cursor.<br />begin of selection (Alt+Home) : Move the cursor at the beginning of the selection.<br />end of selection (Alt+End) : Move the cursor at the end of the selection.<br />Move among file group (Alt+Z) : swap between header and source files.<br />next modified win (Ctrl+Alt+Up) : Look for next modified windows (useful after using macro "replace grep lines").<br />previous modified win (Ctrl+Alt+Down) : Look for next modified windows (useful after using macro "replace grep lines").<br />next windows (Ctrl+Alt+Right) : open next windows.<br />previous windows (Ctrl+Alt+Left) : open previous windows.<br />next action path (Shift+Ctrl+Alt+Up) : open a windows in the next working directory<br />previous action path (Shift+Ctrl+Alt+Down) : open a windows in the next working directory<br />open local file (Alt+O) : Open local files<br />open file with mask (Shift+Alt+O) : Apply a regex filter on allready-open files<br />open file with predefined mask (Shift+Ctrl+Alt+O) : Apply a regex filter on allready-open files<br />goto main file (F4) : Open the local project file.<br />goto global main file (Shift+F4) : Open the global project file.<br />Flags dialog (Shift+Ctrl+Alt+F) : choose among existing flags.</p>
<ul>
<li><strong>Move (Mk)&gt;Flags :</strong></li>
</ul>
<p>insert flag 1 (Ctrl+Alt+1) : Insert flag 1. A flag memorize the file name and the line number. To go to flag i, use ALT+i.<br />insert flag 2 (Ctrl+Alt+2) : Insert flag 2.<br />insert flag 3 (Ctrl+Alt+3) : Insert flag 3.<br />insert flag 4 (Ctrl+Alt+4) : Insert flag 4.<br />insert flag 5 (Ctrl+Alt+5) : Insert flag 5.<br />insert flag 6 (Ctrl+Alt+6) : Insert flag 6.<br />insert flag 7 (Ctrl+Alt+7) : Insert flag 7.<br />insert flag 8 (Ctrl+Alt+8) : Insert flag 8.<br />insert flag 9 (Ctrl+Alt+9) : Insert flag 9.<br />insert flag 0 (Ctrl+Alt+0) : Insert flag 0.<br />goto flag 1 (Alt+1) : Go to flag 1.<br />goto flag 2 (Alt+2) : Go to flag 2.<br />goto flag 3 (Alt+3) : Go to flag 3.<br />goto flag 4 (Alt+4) : Go to flag 4.<br />goto flag 5 (Alt+5) : Go to flag 5.<br />goto flag 6 (Alt+6) : Go to flag 6.<br />goto flag 7 (Alt+7) : Go to flag 7.<br />goto flag 8 (Alt+8) : Go to flag 8.<br />goto flag 9 (Alt+9) : Go to flag 9.<br />goto flag 0 (Alt+0) : Go to flag 0.</p>
<ul>
<li><strong>Comment (Mk) :</strong></li>
</ul>
<p>swap comment 1 (Alt+Q) : comment or uncomment the selection with the first comment characters. The choice is made by testing wether the first line of the selection is commented or not. If no selection, the current line is commented or uncommented. The comment characters are set in the file : macro_parameters.nm.<br />swap comment 2 (Shift+Alt+Q) : Comment or uncomment the selection with the second comment characters. The choice is made by testing wether the first line of the selection is commented or not. If no selection, the current line is commented or uncommented. The comment characters are set in the file : macro_parameters.nm.<br />comment (Alt+Period) : Comment the selection with the first comment characters. If no selection, the current line is commented or uncommented. The comment characters are set in the file : macro_parameters.nm.<br />uncomment (Alt+Comma) : Uncomment the selection with the first comment characters. If no selection, the current line is commented or uncommented. The comment characters are set in the file : macro_parameters.nm.<br />nice line comment (Shift+Ctrl+Alt+Slash) : Put some nice comments around the selection.</p>
<ul>
<li><strong>Advanced (Mk)&gt;ctags :</strong></li>
</ul>
<p>local definitions (Shift+Ctrl+Alt+G) : Open a windows which list all the functions declared in a file (using ctags). You can change the parameters in macro_parameters.nm ($ctags_parameters) PS: use Exuberant Ctags.<br />global definitions (Ctrl+Alt+G) : Open a windows which list all the symbols declared in working directory (using ctags). You can change the parameters in macro_parameters.nm ($ctags_parameters) PS: use Exuberant Ctags.<br />find_definition dialog (Shift+Ctrl+D) : If nothing selected, a dialog box pop up asking for which tag to use.<br />reload tags file (Ctrl+Alt+T) : Reload tags file.<br />create tags file (Shift+Ctrl+Alt+T) : create and load a new tags file.</p>
<ul>
<li><strong>Advanced (Mk)&gt;Search :</strong></li>
</ul>
<p>find file (F5) : Recursive search of files.<br />grep (F6) : Look for an expression in the working directory (eventually recursively).<br />grep regex (Shift+F6) : Look for an expression in the working directory (eventually recursively).<br />replace grep lines (Alt+F6) : After having changed the result of the "grep" macro, you can send back the modification using this macro.<br />grep settings (Shift+Alt+F6) : Change the parameters of the "grep" macro: the file masks and regex/literal. The default values can be change in the macro_parameters.nm.</p>
<p>&nbsp;</p>
<ul>
<li><strong>Advanced (Mk)&gt;Expander </strong>:</li>
</ul>
<p>expand (Ctrl+Return) : Expand a shorcut. For instance, "\\un" is extended to "using namespace". Try to open and modify the file "expander.data".<br />expand with selection (Ctrl+Alt+E) : todo<br />expand with selection (dialog) (Shift+Ctrl+Alt+E) : todo<br />template file (Alt+Return) : create a new template file.<br />open expander.data (Shift+Ctrl+Alt+E) : Open the file "expander.data".</p>
<ul>
<li><strong>Advanced (Mk)&gt;Completion :</strong></li>
</ul>
<p>completion (Alt+Space) : completion. Can also use dictionnary.<br />completion (backward) (Shift+Alt+Space) : backward completion.<br />special completion (Ctrl+Space) : Special completion with tags name.<br />special completion (backward) (Shift+Ctrl+Space) : Backward special completion.<br />file completion (Ctrl+Alt+Space) : Completion with file names.<br />file completion (backward) (Shift+Ctrl+Alt+Space) : Completion with file names.</p>
<ul>
<li><strong>Buffer (Mk) :</strong></li>
</ul>
<p>Find interesting line (F1) : Find an interesting line (ie: with a file name and eventually a line number). You can add or modify the interested lines in the macro_parameters.nm file.<br />Find interesting line (backward) (Shift+F1) : idem, backward.<br />Find interesting line priority (Shift+Alt+F1) : set new find-interesting-line priority.<br />Highlight interesting (Alt+F1) : hightlight interesting lines.<br />Process interesting line (F2) : Look for an interesting line and apply the corresponding action<br />Process interesting line (auto) (Shift+F2) : Look for an interesting line and apply the corresponding special action<br />Goto buffer (F3) : Open the NEdit temporary file.<br />Goto last file (Alt+F3) : Set NEdit temporary file parameters.<br />New buffer (Shift+F3) : New buffer.<br />Goto Makefile (Alt+F4) : Open Makefile.<br />Next interesting line (Alt+F2) : find the next intersting line and jump goto it.</p>
<ul>
<li><strong>Buffer (Mk)&gt;shortcut :</strong></li>
</ul>
<p>show unix command (Alt+U) : Show the unix commands bind to the (ALT+)F9-F12. You can permantly change those command in the macro_parameters.nm.<br />kill current buffer (Ctrl+Alt+K) : kill current execution<br />execute command dialog (Alt+F8) : Enter a unix command to execute in the NEdit temporary file.<br />execute command list (Shift+Alt+F8) : open a list dialog box with unix command (define in macro_parameters.nm) .<br />execute last command (F8) : Execute last command.<br />execute unix file (Alt+F7) : Execute one of the executable files present in the local directory.<br />execute last unix file (F7) : Execute last executable files.<br />execute F9 (F9) : Execute the unix command bind to F9.<br />execute F10 (F10) : Execute the unix command bind to F10.<br />execute F11 (F11) : Execute the unix command bind to F11.<br />execute F12 (F12) : Execute the unix command bind to F12.<br />execute ALT F9 (Alt+F9) : Execute the unix command bind to ALT+F9.<br />execute ALT F10 (Alt+F10) : Execute the unix command bind to ALT+F10.<br />execute ALT F11 (Alt+F11) : Execute the unix command bind to ALT+F11.<br />execute ALT F12 (Alt+F12) : Execute the unix command bind to ALT+F12.</p>
<ul>
<li><strong>c++ (Mk) :</strong></li>
</ul>
<p>create constructor (Shift+Alt+C) (C++) : Create a constructor with the selected parameters.<br />Add stderr (Shift+Ctrl+Alt+C) (C++) : Create a constructor with the selected parameters.</p>
<ul>
<li><strong>Work settings (Mk) :</strong></li>
</ul>
<p>choose host (Shift+Alt+H) : Choose a new host (among those listed in the macro_parameters.nm file).<br />new path (Ctrl+Alt+P) : Set a new Working directory.<br />new host (Ctrl+Alt+H) : Enter a new host.<br />local path (Shift+Ctrl+Alt+P) : Set the Working directory to the local path.<br />local host (Shift+Ctrl+Alt+H) : Set the host to the local host.<br />Change macros parameters (Ctrl+Alt+M) : Open the macro_parameters.nm file.<br />reload macros parameters (Shift+Ctrl+Alt+M) : Reload the macro_parameters.nm file.<br />switch global/local working directory (Ctrl+Alt+S) : Some macros have to know the directory into which they must be executed (for compilation by example). These working directory can be handle in two different ways:<br />- local mode : the working directory is always the directory of the current file,<br />- global mode : the working directory does not depend on the current file.<br />To change mode, use this macro.</p>
<ul>
<li><strong>Misc (Mk) :</strong></li>
</ul>
<p>Reload actual macro file (Ctrl+Alt+R) (NEdit Macro) : Reload actual nedit macro file.<br />Show shell command : Show (and eventually check) if the shell commands defined in macro_parameters.nm are valid.<br />Save all (Shift+Ctrl+S) : Save all open files.<br />Clean rangeset (Shift+Ctrl+Alt+R) : destroy all rangesets<br />Help : About this macros...</p>


<h2>WINDOWS BACKGROUND MENU:</h2>

<p>ctags local (Mk) : Open a windows which list all the functions declared in a file (using ctags). You can change the parameters in macro_parameters.nm ($ctags_parameters) PS: use Exuberant Ctags.<br />new template file (Mk) : create a new template file.<br />save all (Mk) : Save all open files.</p>
<ul>
<li><strong>Comment (Mk) :</strong></li>
</ul>
<p>comment // : add comments: //.<br />uncomment // : remove comments: //.<br />comment /<b>...</b>/ : add comments: /<b>...</b>/.<br />uncomment /<b>...</b>/ : remove comments: //.<br />comment # : add comments: #.<br />uncomment # : remove comments: #.<br />comment mail : add comments: &gt;.<br />uncomment mail : remove comments: &gt;.<br />comment % : add comments: &amp;.<br />uncomment % : remove comments: %.</p>
<ul>
<li><strong>Completion dialog (Mk) :</strong></li>
</ul>
<p>window completion : Open a dialog box with all completion matches in the windows.<br />dico completion : Open a dialog box with all completion matches in the dictionaries.<br />global ctags completion : Open a dialog box with all completion matches in the tags file.<br />local ctags completion : Open a dialog box with all completion matches in the tags file.<br />file name completion : Open a dialog box with all completion matches in file names of the current directory.</p>
<ul>
<li><strong>Customize (Mk) :</strong></li>
</ul>
<p>open expander.data : Open the expander.data file.<br />open language-specific dicos : open one of the dictionaries bind to the current langages.<br />open dicos : open a dictionary.</p>
<ul>
<li><strong>Work settings (Mk) :</strong></li>
</ul>
<p>choose host : Choose a new host (among those listed in the macro_parameters.nm file).<br />new path : Set a new Working directory.<br />new host : Enter a new host.<br />local path : Set the Working directory to the local path.<br />local host : Set the host to the local host.<br />Change macros parameters : Open the macro_parameters.nm file.<br />reload macros parameters : Reload the macro_parameters.nm file.<br />switch global/local working directory : Some macros have to know the directory into which they must be executed (for compilation by example). These working directory can be handle in two different ways:<br />- local mode : the working directory is always the directory of the current file,<br />- global mode : the working directory does not depend on the current file.<br />To change mode, use this macro.</p>


<br><br>
<a href='http://frank.perbet.org'>About me</a>

Unrelated but I like them so here we go: <a href='http://www.ubitouch-studio.com/'>Ubitouch power!</a>
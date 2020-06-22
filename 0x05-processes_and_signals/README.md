# 0x05. Processes and signals

## General
What is a PID
What is a process
How to find a process’ PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored

## Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

> ### 0. What is my PID mandatory
Write a Bash script that displays its own PID.
---

> ### 1. List your processes mandatory
Write a Bash script that displays a list of currently running processes.
---

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display in a user-oriented format
Show process hierarchy
---

> ### 2. Show your Bash PID mandatory
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
---


> ### 3. Show your Bash PID made easy mandatory
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
---

> ### 4. To infinity and beyond mandatory
Write a Bash script that displays To infinity and beyond indefinitely.
---

> ### We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that kills 4-to_infinity_and_beyond process.
---

> ### 6. Kill me now made easy mandatory
Write a Bash script that kills 4-to_infinity_and_beyond process.
---

> ### 7. Highlander mandatory
Write a Bash script that displays:
---

To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
---

> ### 8. Beheaded process mandatory
Write a Bash script that kills the process 7-highlander.
---

> Christian Nazareno
### | [twitter](https://twitter.com/Camilo06134257) | [linkedin](https://www.linkedin.com/in/christian-nazareno-8441b81a1/) | [mail](1464@holbertonschool.com) | [github](https://github.com/ch-canaza)  |
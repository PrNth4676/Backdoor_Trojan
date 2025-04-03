# Backdoor Trojan using Python

A backdoor is a type of specialized trojan which when executed on a system would allow the attacker to gain full control over the system. It establishes communication between the attacker and victim per which attacker can perform basic system command such as dir, ipconfig etc. for starters.

<div align="center">
  ![Backdoors](https://github.com/user-attachments/assets/41d6e525-f05f-41f5-9e57-7d9bfb35a60b)
</div>

## Establish Connection:
* We have the attacker machine and the victim machine, the backdoor gets executed in the victim’s machine.
* The program runs on the victim’s machine and once done, its going to establish a connection between them represented in the purple dashed line.
* The attacker then sends system commands over the line established on the victim’s machine, the result is then going to be send back to the hacker.
* We have the attacker machine and the victim machine, the backdoor gets executed in the victim’s machine.
* The program runs on the victim’s machine and once done, its going to establish a connection between them represented in the purple dashed line.
* The attacker then sends system commands over the line established on the victim’s machine, the result is then going to be send back to the hacker.

<div align="center">
  ![image](https://github.com/user-attachments/assets/26127af5-3b52-4306-b162-c12beb9559a7)
</div>

## Reverse Connection:
* In this case, when the back door is executed on the victim’s computer it will connect back to the attacker.
* The attacker will open a port in its own system and will listen actively for an incoming connection.
* In attacker’s system ,the firewall will as expected warn about the open port, but the attacker will simply ignore as it wants it to remain open so that it can be used for its own benefit.
* The backdoor is then executed in the victim’s computer and is going to connect back from its system to the attacker.
* This connection from the victim is very similar to any other connection that the victim does every day similar to opening a web site where a connection is established.	
* Hence, most firewalls will not trigger this as an suspicious activity as it looks like a normal connection request.






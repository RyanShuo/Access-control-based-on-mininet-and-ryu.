# Access-control-based-on-mininet-and-ryu.


experimental procedure:
Open a terminal ：ryu-manager simple_switch_13.py ofctl_restapi.py
Open a new terminal,Create a tree topology with a depth of 2 and a breadth of 2.
mn --topo=tree,2,2 --controller=remote --mac
Create folders in the home directory named site8080 and site9090 respectively
Edit the default web page file (index.html) in two separate folders
Test the connectivity and then open the terminals of h1, h2, h3 and h4 with xterm in mininet.
Run multi.server.py in h4's terminal to start the web service.
Try to access 10.0.0.4:8080 and 10.0.0.4:9090 at the terminal of h1, h2, and h3, respectively, to test the effect of access control.
Access Control Success

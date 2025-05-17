Manually:

To Run the base cluster
./build.sh

To run the port hopping script while the cluster is running:
./hop.sh

Automatic:

To run the sheduling port hopping (make sure cluster isn't running).
This will run forever, ctrl + c is the solution to exit this script.
./scheduler.sh


To access the local host from the client side
accessing local host with curl: 
./client.sh

accessing local host with firefox: 
./client.sh 1

accessing service IP (inside the cluster) through curl:
./client.sh 2

accessing service IP (inside the cluster) through firefox:
./client.sh 3 


Takedown:
To take down the cluster:
./takedown.sh

If microk8s is having issues getting the image running. This is a hard reset option that will take a while but will fix the issues.
./hardtakedown.sh

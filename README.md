probability-berkeley-trace
==========================

A collection of python scripts to parse through the UC Berkeley Home IP Web Traces.
This project is a collaboration between myself and Alex Thompson '13 for ELEC 471, Probability Appications in Electrical Engineering, at Bucknell University.
The scope of our project was to analyze web traffic information to determine if a better caching algorithm for Web Proxies could be determined from a probabilistic analysis of the traffic. We utilized the UC Berkeley Home IP Web Traces project (http://ita.ee.lbl.gov/html/contrib/UCB.home-IP-HTTP.html) which provided 18 days of logs of the traffic going through the UC Berekely Home web proxies back in '96.
TODO add description of Web Traces
TODO add description of Python scripts
TODO add modelling information
To use,
cat UCB-home-IP-848278026-848292426.tr | ./tools/showtrace  > traces.txt
python parse_traces.py traces.txt > first_trace.txt


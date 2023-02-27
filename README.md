# FFSSRF
### A script to fuzz for Server-Side Request Forgery
### Implementations:
This script includes support for authentication, automatically detecting parameters in the URL to fuzz, and generating payloads based on the parameter type. It also includes support for more complex exploitation techniques, such as chaining SSRF with other vulnerabilities.
### Description:
This script is a simple implementation of a Server-Side Request Forgery (SSRF) vulnerability scanner. The script is designed to test a given URL for possible SSRF vulnerabilities by sending requests with different payloads to the server and checking for responses. The payloads in the script represent different ways a user input can be manipulated to access resources that are otherwise not directly accessible by the user. If the response code is not 404, then the script assumes that a possible SSRF vulnerability exists and attempts to exploit it by replacing the payload with the attacker's server URL. If the exploit is successful, the script prints the response text, indicating that an SSRF attack was possible. The script also has a "Done!" message to indicate that the scan has completed.

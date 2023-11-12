# Challenge Writeup

## Hints

### Hint 1

<details> Why reinvent the wheel? Check if someone has cracked the MD5 hash before you... </details>

### Hint 2

<details> Think about how regex special characters are used. https://regex101.com/ is great to test ideas out. </details>

## Solution

<details> 
Google the MD5 hash stored in 'md5_admin_pwd' finds https://md5.gromweb.com/?md5=9cc2ae8a1ba7a93da39b46fc1019c481. 
This reveals the password is (including spaces):correct horse battery staple

Logging into the vault with this password reveals the dashboard with an onion domain lookup service.
However we need to bypass the '.onion' domain name in order to send a request to our own domain.
Regex treats the `.` character as any literal character, so we could set our domain as google.com/Aonion and it would still match.

Using http://requestrepo.com, we can enter our generated domain as 0gno3uxx.requestrepo.com/Aonion to receieve a GET request, leaking the IP address.
</details>

> I hope you enjoyed the little challenge - especially if completed in work hours!
> The main "exploit" it centered around is more common than you'd think, and I've seen it several times in the real world - commonly with Cross-Site Origin Policy misconfigurations. 











































































 <!-- Scrolling up will reveal spoilers if you're still working on the challenge <3 -->

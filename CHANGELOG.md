# Changelogs

 Based on version 0.23.4 (# try to keep up to date with latest version).

 Have this PR inside (that are not in the original lib):

- [feat(node): Onprem network remove white backgound #697] https://github.com/mingrammer/diagrams/pull/697
- [feat(provider): Replace IBM resources #655] https://github.com/mingrammer/diagrams/pull/655 /!\ This one will break for IBM user ☜(꒡⌓꒡) >= 0.21.1.1
- [feat(scripts): provide diagrams CLI #524] https://github.com/mingrammer/diagrams/pull/524 /!\ This one will break need to call with "diagrams build example1.py" Need to add build >= 0.21.1.4
- [Support attributes on custom node #529] https://github.com/mingrammer/diagrams/pull/529
- [docs(edge): Add @clayms examples #495] https://github.com/mingrammer/diagrams/pull/495
- [Node as cluster #438] https://github.com/mingrammer/diagrams/pull/438
- [Added icon for Pulumi #759] https://github.com/mingrammer/diagrams/pull/759 but with text less icon
- [adding https://identicons.dev/ icons licensed under the MIT license. #758 ] https://github.com/mingrammer/diagrams/pull/758 Renamed the files and put all under generic/auth


Disclaimer
*/!\* There's maybe some code changes from the original PR and unexpected bugs as I need to merge (sometime very old PR) and change the way I expected it to work which can defer from the original author!
Your python code should work if you generate from Original Diagrams lib, but will broke in the other way.
Sorry if you contribute and I copy paste your contribution and you lost the honor to be in the contributors list, I feel like a leech that copy your hard work. But you are welcome to join here and make more contribution.

Diagrams ---> Diagrams-xtd (Maybe OK)
Diagrams-xtd ---> Diagrams (Will not work)

# Changelogs

 Based on version 0.21.1  [commit 4c5cacdaba299f7d4a0cebf73e0f7fa7951fcd66] (# try to keep up to date with latest version).

 Have this PR inside:

- [feat(node): Onprem network remove white backgound #697] https://github.com/mingrammer/diagrams/pull/697
- [feat(provider): Replace IBM resources #655] https://github.com/mingrammer/diagrams/pull/655 /!\ This one will break for IBM user ☜(꒡⌓꒡) >= 0.21.1.1
- [feat(scripts): provide diagrams CLI #524] https://github.com/mingrammer/diagrams/pull/524
- [Support attributes on custom node #529] https://github.com/mingrammer/diagrams/pull/529
- [docs(edge): Add @clayms examples #495] https://github.com/mingrammer/diagrams/pull/495
- [Node as cluster #438] https://github.com/mingrammer/diagrams/pull/438
- [Add icons to docs #499] https://github.com/mingrammer/diagrams/pull/499

Disclaimer
*/!\* There's maybe some code changes from the original PR and unexpected bugs as I need to merge (sometime very old PR) and change the way I expected it to work which can defer from the original author!
Your python code should work if you generate from Original Diagrams lib, but will broke in the other way.

Diagrams ---> Diagrams-xtd (Maybe OK)
Diagrams-xtd ---> Diagrams (Will not work)

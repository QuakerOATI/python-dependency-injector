Flask + dependency-injector tutorial: Github Navigator
======================================================

Tool exposing basic search functionality for GitHub repos.

The supported browser-based workflow is:
  #. Point browser at server address
  #. Enter search query
  #. Navigator will then serve a page displaying all matching repositories.  For each repo, the following information is displayed:
    - repo name
    - owner
    - last commit
  #. Click on desired repo name; browser will be redirected to the GitHub repository

#!/usr/bin/env bash
# Push the workflow's commit, surviving concurrent pushes (GrokBot, Lilly, other runs).
# On rejection: rebase onto origin/main (our side wins conflicting hunks), rebuild every theme's index, amend, retry.
set -u
for i in 1 2 3 4 5; do
  git push origin HEAD:main && exit 0
  echo "push rejected (attempt $i); rebasing onto origin/main"
  git fetch origin main
  if ! git rebase -X theirs origin/main; then git rebase --abort; echo "rebase failed"; exit 1; fi
  for t in $(ls themes | grep -v '^_'); do python3 scripts/build_index.py --theme "$t" >/dev/null || true; done
  git add -A themes/*/index
  git diff --cached --quiet || git commit --amend --no-edit
  sleep $((i * 5))
done
echo "gave up after 5 attempts"; exit 1

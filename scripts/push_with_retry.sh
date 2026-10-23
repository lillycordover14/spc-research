#!/usr/bin/env bash
# Push the workflow's commit, surviving concurrent pushes (GrokBot, Lilly, other runs).
# On rejection: rebase onto origin/main. Conflicting hunks: the repo side wins (agent summaries beat bot refetches,
# which can be redone). A file deleted upstream stays deleted
# (an agent removed it as noise or a duplicate). Then rebuild every theme's index, amend, retry.
set -u
resolve_conflicts() {
  for f in $(git diff --name-only --diff-filter=U); do
    if git cat-file -e "origin/main:$f" 2>/dev/null; then git checkout --ours -- "$f" && git add -- "$f"
    else git rm -q -- "$f"; fi
  done
}
for i in 1 2 3 4 5; do
  git push origin HEAD:main && exit 0
  echo "push rejected (attempt $i); rebasing onto origin/main"
  git fetch origin main
  if ! git rebase -X ours origin/main; then
    for _ in 1 2 3; do
      resolve_conflicts
      GIT_EDITOR=true git rebase --continue && break
    done
    if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then git rebase --abort; echo "rebase failed"; exit 1; fi
  fi
  for t in $(ls themes | grep -v '^_'); do python3 scripts/build_index.py --theme "$t" >/dev/null || true; done
  git add -A themes/*/index
  git diff --cached --quiet || git commit --amend --no-edit
  sleep $((i * 5))
done
echo "gave up after 5 attempts"; exit 1

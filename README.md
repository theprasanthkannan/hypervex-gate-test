# hypervex-gate-test

A deliberately vulnerable fixture used to verify that the Hypervex merge gate
blocks a merge when branch protection requires its check.

Public because branch protection is unavailable on private repositories under a
free GitHub plan. Contains no real credentials — the only vulnerability is a
SQL injection, introduced on a branch, on purpose.

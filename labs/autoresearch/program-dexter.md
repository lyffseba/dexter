# Dexter Autoresearch: Continuous Swarm Improvement

This is a meta-experiment. The goal is to have the LLM agent autonomously improve the `dexter` ecosystem and the `dexter_cli.py` CLI game itself.

## Setup

To set up a new improvement cycle, work with the user to:

1. **Initialization**: Check if the agent is running in a fresh clone. If so, immediately read `CHEATSHEET.md` and `README.md` to understand the ecosystem.
2. **Agree on a feature**: Propose a new feature for `dexter_cli.py` or a new lab (e.g., adding an API call to check RunPod balance, adding ASCII art, adding a new RLHF training script).
3. **Read the in-scope files**: Read the files you are modifying (`dexter_cli.py`, `README.md`, or the `labs/` directory).
4. **Confirm and go**: Confirm the plan with the Director.

## Experimentation

The agent is allowed to execute Python scripts locally and interact with the CLI to test its changes.

**What you CAN do:**
- Modify `dexter_cli.py` to add new menu options, better animations, or real API integrations.
- Modify `README.md` to reflect new CLI features.
- Create new labs in the `labs/` directory.
- Run `python3 dexter_cli.py` (by piping inputs) to verify the UI hasn't crashed.

**What you CANNOT do:**
- You cannot spend RunPod credits without explicit permission. Any command that calls the `runpodctl` API must have a confirmation prompt.
- You cannot delete existing labs.

**The metric of success:** The CLI game must remain bug-free, visually appealing, and functionally useful to the Director.

## The Experiment Loop

1. Look at the current state of `dexter_cli.py`.
2. Propose a change or implement the agreed-upon feature.
3. Test the change locally using `bash`.
4. If it works and looks good, commit the changes to git.
5. If it crashes or has syntax errors, revert or fix.

**NEVER STOP**: Once the loop has begun, do not pause to ask the human if you should continue unless you need explicit permission to spend money or spin up a cloud resource. The goal is continuous, autonomous improvement of the Dexter OS.

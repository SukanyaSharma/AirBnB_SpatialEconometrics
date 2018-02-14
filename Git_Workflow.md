# This is documentation on how to use Git (Gitlab) commands to contribute code to the AirBnB Spatial Econometrics project.
Author: Vaibhav Karve
Last Modified: 2018-02-14

### Disclaimer: I am still a noob and there might be mistakes born due to my incorrect understanding of how git works. Let me know if you have any questions, or if things don't work out the way I say they would. -- Vaibhav Karve


## Requirements:
   - Terminal or Command-Prompt
   - Make sure git is installed on your computer.


## For setting up the repository on your local machine: (You need to do this only the first time)

1. In your local machine, navigate to a location where you wish to create a local copy of the repository.

2. Run the command: `git clone https://gitlab.engr.illinois.edu/r-sowers/TrafficPatterns.git`.
   - This will create a copy of the remote GitLab repository (called `origin`) into your local machine (in a folder called `TrafficPatterns`).
   - It will also create a hidden `.git` folder within `TrafficPatterns`.
   - You might have to enter your username and password here for authorization.
   - You now have a working copy of the repository including all its branches.
   - (To undo this step, simply delete the folder from your local machine.)


## Helpful commands that you can run at any time without it messing with your files:
   - `git fetch`
   - `git branch`
   - `git status` 
   - `git log --oneline --decorate --graph`


## If now you wish to change some part of the code: (You need to repeat these steps every time you start working on the code.)

3. Always start by running the command `git fetch`.
   - This updates your local repository with any new changes that anyone else might have pushed to GitLab since the last time you updates the repository.
   - This command is perfectly safe to run as it does not overwrite anything and causes no loss of data. It is just a way of syncing your git history with that of the remote repository.
   - Run this as often as you wish, even while in the middle of working on something. The more the better.

4. Before you start editing anything, create a new branch. This keeps any changes you make out of the master branch till you are ready to merge in the new changes.
   - Run the command `git branch dumbidea` to create a branch called `dumbidea`.
   - To check if this worked, run `git branch` to create a list of branch with an asterix next to the branch you are currently on.
   - Note that the default branch is called `master`.
   - (You can undo this step by running `git branch -d dumbidea`. This will delete the branch you just created.)
   
5. Switch to the branch you created in Step 4. by running `git checkout dumbidea`.
   - (You can undo this step and switch back to master by running `git checkout master`).
   - *Important:* every time you switch branches, the files on your local machine will change to reflect the state of the files in that particular branch.

6. Make the changes you wish to make to any files you want. Say you changed `A.txt`, `B.txt` and `C.txt`.
   - If at any point you wish to revisit or view the old file (beofe your changes), you can access the old version simply by switching back to master branch (`git checkout master`). Make sure you switch back to your `dumbidea` branch before making more changes.
   - You can review which files you have changed by running `git status`.
   - You can review which changes you made in a particular file by running say `git diff C.txt`.
   - If you are dissatisfied by the changes you made to say `C.txt`, simply run `git checkout C.txt` to revert back to the state of the file as it was during the previous commit. This will undo any changes. (You cannot undo this undo-ing. So be careful. Run the `git checkout C.txt` command only if you are sure you want to discard any changes you made.)

7. Stage the changes you do wish to keep. This is done by running `git add path/to/file`
   - Throughout the following steps, you can always run `git status` to keep track of which files have been modified, which have been staged, and which have been committed.
   - Staging the file is like saying "I am happy with the changes I have made and would like to start the process of creating a check-point for the files at this point."
   - (You can undo this step by running `git reset HEAD path/to/file`.
   - If you are done editing `A.txt` but are still working on `B.txt`, it is okay to stage only `A.txt`. Even if you edit `A.txt` after staging, you can always re-stage it by typing `git add A.txt`.

8. Once all files have been staged, we are ready to commit our changes by running `git commit dumbidea`:
   - This is a local commit! This will only commit on our local machine and will not affect what is present on GitLab. Think of this as an extra layer of security before your `dumbidea` start affecting everyone else.
   - You will be prompted with a message window where you should type out your commit message in as meaningful a way as possible.
   - Check that your commit was successful by running `git status`. You should now see a message that says `your branch is 1 commit ahead of origin/master`.
   - (If you wish to undo this commit, look at the next to steps depending on whether you wish to do a soft or hard undo).
   
9. If you decide that you committed the file too soon and would like to undo just the commit but keep all the edits you might have made to the file:
   - Run `git reset HEAD~1`
   - This takes you back to how things were at the end of Step 7. i.e. files are staged but not committed.
   - (To undo this undo-ing, simply repeat Step 8.)
   
10. If you decide that the commit you made in step 8. is complete rubbish and you want to erase all history of the edits that were made since the commit before that, you need a hard reset.
   - Run `git reset --hard HEAD~1`
   - (This undo-ing is hard to undo, but possible. Just be careful before doing a hard reset.)

11. I am happy with my commit and now I would like everyone to be able to see it on GitLab:
   - If you are done with Step 8. and haven't had the need to run Steps 9. and 10., then you can run `git push` to push your changes to the remote repository (i.e. this will update `origin`).
   - (If you wish to undo this, it is going to be difficult, but not impossible. First, inform everyone on your team to hold off and not work with your erroneous files. Next, start Googling for ways to undo the `git push` commands.)

12. Repeat Steps 6. to 11. as many times as you want in order to make further changes to your `dumbidea` branch.
   - Keep running `git fetch` in order to remain up-to-date with GitLab.

13. Once you are completely confident that `dumbidea` is actually not-so-dumb-afterall, you can decide to merge it into the `master` branch.
   - Switch to master branch by running `git checkout master`.
   - To merge your branch with master, run `git merge dumbidea`.
   - If this process works out smoothly without displaying any Conflict messages, then you can move to Step 15.
   
14. If some other user (or you yourself) have made changes to the master branch that are not compatible with changes that you have made to files in `dumbidea` then Git will automatically detect this as a conflict and not allow you to merge till you resolve all the conflict. If this happens, do the following:
   - Open the files that Git has indicated as having conflicts in them, say `A.txt`. In `A.txt`, Git will have marked the specific lines that are in conflict as follows:
    ```
    <<<<<<< HEAD:A.txt
    This is the line that was in the master branch.
    =======
    This is the line that is in the dumbidea branch.
    >>>>>>> dumbidea:A.txt
    ```
   - Replace the block of text specified above with either the version in `master` branch, the version in `dumbidea` branch, or a mixure of both versions.
   - Make sure to completely remove the <<<<<<<, ======= and >>>>>>> lines.
   - After resolving each section in each conflicted file, run `git add` on each file to mark it as resolved and to stage it.
   - Run `git commit` without any conflict messages.

15. Cleaning up after you are done using your branch.
   - After you have successfully merged a branch into `master`, you can get rid of the `dumbidea` branch by running `git branch -d dumbidea`.
   - This will clean up the branch history.
   - You can check that the branch has been deleted by running `git branch`.

16. Next time you want to edit something, start again at Step 4.

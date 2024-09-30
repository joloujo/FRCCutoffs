# Development Log

This is just a place for me to write some public notes and explain my development choices. This might get merged into the README at some point, but for now it's nice to have a place to write where I don't have to worry about things looking nice or making sense.

## Initial plan

So here's the deal. [FRC Locks](https://frclocks.com/) is a great website, but in my humble opinion, the metric it uses is misleading. In my experience, when people see a percentage symbol, they think it's a percent chance of making it to the district point cutoff. FRC Locks uses lock percentage, which is essentially how many points are needed by the teams below a given team to tie that given team and knock them out of qualifying, divided by the points remaining in the district. In other words, this metric measures the percentage of the way to guaranteeing a team qualifies, assuming that all of the remaining points in the district could be distributed in the worst way possible.

This has a couple areas I want to improve on. First of all, the way it assumes district points can be distributed is simple but incorrect. I want to create a system that knows where district points could go. I also want to take into account the skill of teams, as it should produce much better results.

This also gets into what metric I want this website to display. I don't really want to use percentage chances of getting the points needed to qualify, as these are just predictions, and I don't want teams to feel discouraged by low chances. I do, however, want to be realistic, to help teams plan. Because of this, I'll probably have everything be in units of district points. For example, I'll probably include 5%, 50%, and 95% district point numbers (numbers of points to have that chance of going). I also want to include a distribution of where the cutoff will fall.

## Entry 2: How is this actually going to calculate a cutoff?

The mail idea for this is to use a monte carlo simulation to try to find the distribution of the cutoff value. To get the cutoff value, we need to know each simulated team's number of district points at the end of a simulated season. To do this, we need to simulate every event. We might be able to just get away with that because we can probably get that from statbotics.
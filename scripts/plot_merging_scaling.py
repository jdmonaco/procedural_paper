import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plot_settings

# Import data
data = np.genfromtxt("merging_data.csv", delimiter=",", skip_header=1)
assert data.shape[1] == 11

fig, axes = plt.subplots(2, 2, sharex="col", frameon=False,
                         figsize=(8.5 * plot_settings.cm_to_inches, 
                                  5.0 * plot_settings.cm_to_inches))

# Plot compile time
plot_style = {"marker": "o"}
compile_time_axis = axes[0,0]
compile_time_axis.set_title("A", loc="left")
latest_actor = compile_time_axis.plot(data[:,0], data[:,2], **plot_style)[0]
release_actor = compile_time_axis.plot(data[:,0], data[:,7], **plot_style)[0]
#compile_time_axis.set_xlabel("Num populations")
compile_time_axis.set_ylabel("$T_{comp}$ [s]")
compile_time_axis.set_yticks([0, 1000, 2000])
compile_time_axis.xaxis.grid(False)
compile_time_axis.yaxis.grid(False)
sns.despine(ax=compile_time_axis)

# Plot simulation time
sim_time_axis = axes[0,1]
sim_time_axis.set_title("B", loc="left")
sim_time_axis.plot(data[:,0], data[:,1], **plot_style)
sim_time_axis.plot(data[:,0], data[:,6], **plot_style)
#sim_time_axis.set_xlabel("Num populations")
sim_time_axis.set_ylabel("$T_{sim}$ [s]")
sim_time_axis.xaxis.grid(False)
sim_time_axis.yaxis.grid(False)
sns.despine(ax=sim_time_axis)

# Plot SOL time
sol_time_axis = axes[1,0]
sol_time_axis.set_title("C", loc="left")
sol_time_axis.plot(data[:,0], data[:,3], **plot_style)
#axes[1,0].plot(data[:,0], data[:,4], color=pal[0], linestyle="--")
sol_time_axis.plot(data[:,0], data[:,8], **plot_style)
#[1,0].plot(data[:,0], data[:,9], color=pal[1], linestyle="--")
sol_time_axis.set_xlabel("$N_{pop}$")
sol_time_axis.set_ylabel("$K_{mem}$ [%]")
sol_time_axis.set_ylim((0, 100))
sol_time_axis.xaxis.grid(False)
sol_time_axis.yaxis.grid(False)
sns.despine(ax=sol_time_axis)

# Plot instruction stall count
stall_count_axis = axes[1,1]
stall_count_axis.set_title("D", loc="left")
stall_count_axis.plot(data[:,0], data[:,5], **plot_style)
stall_count_axis.plot(data[:,0], data[:,10], **plot_style)
stall_count_axis.set_xlabel("$N_{pop}$")
stall_count_axis.set_ylabel("$N_{stall}$")
stall_count_axis.xaxis.grid(False)
stall_count_axis.yaxis.grid(False)
stall_count_axis.set_yticks([0, 25, 50])
sns.despine(ax=stall_count_axis)

fig.legend([latest_actor, release_actor], ["Latest version", "GeNN 4.1.0"], 
           ncol=2, frameon=False, loc="lower center")
fig.align_ylabels()
fig.tight_layout(pad=0, rect= [0.0, 0.1, 1.0, 1.0])
if not plot_settings.presentation:
    fig.savefig("../figures/merging_scaling.pdf")
plt.show()
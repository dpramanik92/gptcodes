def create_custom_8_subplot_layout(figsize=(12, 8)):
    fig = plt.figure(figsize=figsize)
    outer_gs = gridspec.GridSpec(2, 3, figure=fig, width_ratios=[1, 1, 1])

    ax_list = []

    # Row 1 - Left and Middle
    ax_list.append(fig.add_subplot(outer_gs[0, 0]))  # ax[0]
    ax_list.append(fig.add_subplot(outer_gs[0, 1]))  # ax[1]

    # Row 1 - Right split into two
    right_top_1 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=outer_gs[0, 2])
    ax_list.append(fig.add_subplot(right_top_1[0]))  # ax[2]
    ax_list.append(fig.add_subplot(right_top_1[1]))  # ax[3]

    # Row 2 - Left and Middle
    ax_list.append(fig.add_subplot(outer_gs[1, 0]))  # ax[4]
    ax_list.append(fig.add_subplot(outer_gs[1, 1]))  # ax[5]

    # Row 2 - Right split into two
    right_top_2 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=outer_gs[1, 2])
    ax_list.append(fig.add_subplot(right_top_2[0]))  # ax[6]
    ax_list.append(fig.add_subplot(right_top_2[1]))  # ax[7]

    return fig, ax_list

import plotly.graph_objects as go

x_range = [-1,1]
y_range = [-1,1]
z_range = [-1,1]

# Create 3D scatter plot
fig = go.Figure()

# Create scatter plot for the first frame
scatter = go.Scatter3d(
    x=[],
    y=[],
    z=[],
    mode='markers',
)

# Add scatter plot to the figure
fig.add_trace(scatter)

# Update layout to set 3D aspect and axis range
fig.update_layout(
    scene=dict(aspectmode="cube", xaxis=dict(range=x_range), yaxis=dict(range=y_range), zaxis=dict(range=z_range))
)

# Update layout to include animation settings
fig.update_layout(
    updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                            method='animate', args=[None, dict(frame=dict(duration=10, redraw=True), fromcurrent=True)])])]
)


def create_frames(landmarks_list):
    frms = []
    for ldmark in landmarks_list:
        frms.append(go.Frame(data=[go.Scatter3d(x=[i.x for i in ldmark], y=[i.y for i in ldmark], z=[i.z for i in ldmark] )]))
    
    fig.frames = frms
    # fig.frames = [go.Frame(data=[go.Scatter3d(x=ldmark.x, y=ldmark.y, z=ldmark.z )]) for ldmark in landmarks_list]

def visualize():
    fig.show()

from nicegui import ui
import pandas as pd
# --- Sidebar (Left Drawer) ---
with ui.left_drawer(bottom_corner=True).style('background-color: #f3f4f6').props('width=150'):
    ui.image('https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg').style('width: 40px; margin: 10px auto; display: block;')
    ui.separator()
    with ui.column().classes('q-mt-md q-gutter-y-sm'):
        with ui.link(target='/').classes('no-underline text-black'):
            ui.icon('home', size='24px')
            ui.label('Home').style('margin-bottom: 0px')
        with ui.link(target='/profile').classes('no-underline text-black'):
            ui.icon('person', size='24px')
            ui.label('Profile').style('margin-bottom: 0px')
        with ui.link(target='/allappliedjobs').classes('no-underline text-black'):
            ui.icon('work', size='24px')
            ui.label('Applied').style('margin-bottom: 0px')
    ui.separator()
    ui.label('© 2025 JobJarvis').classes('text-caption q-mt-auto text-center')
# --- Header (optional, simplified) ---
with ui.header().classes('bg-white text-black shadow-1'):
    ui.label('Job Tracker Dashboard').classes('text-h6 q-ml-md')
# --- Main Content ---
with ui.column().classes('q-pa-md').style('width: 100%; max-width: 1200px;'):
    ui.label('All Applied Jobs').classes('text-h5 q-mb-md')
    df = pd.read_csv('data.csv')
    # Create column definitions for NiceGUI table
    columns = [{'name': col, 'label': col.replace('_', ' ').title(), 'field': col} for col in df.columns]
    # Convert DataFrame rows to list of dictionaries
    rows = df.to_dict(orient='records')
    # Build UI
    with ui.column().classes('q-pa-md').style('width: 100%; max-width: 1200px'):
        ui.label('All Applied Jobs').classes('text-h5 q-mb-md')
        ui.table(columns=columns, rows=rows).classes('q-mt-md w-full justify-centre').props('flat bordered dense')
    ui.run()

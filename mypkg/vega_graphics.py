#!/usr/bin/env python3
import altair as alt
import pandas
import selenium


def vegaGraphics(
        transformed_data,
        verbose,
        cmd_tag,
        sql,
        id1,
        id2,
        parameters):
    """Create interactive charts for specified data"""
    # making function more explicit
    transformed_data, verbose, cmd_tag, sql, id1, id2, parameters = \
        transformed_data, verbose, cmd_tag, sql, id1, id2, parameters
    if verbose >= 1:
        print("Creating Vega Graphics")
    transformed_data = transformed_data.rename(
        columns={
            id1 : 'id1',
            id2 : 'id2',
            sql : 'sql',
            cmd_tag : 'cmd_tag',
            parameters : 'parameters'})

    data_info = transformed_data.copy()
    data = transformed_data[['total_duration', 'cmd_tag', 'id1', 'id2', 'sql', 'parameters']].copy()
    
    data = data.sort_values(
        by=['total_duration'], ascending=True, inplace=False).dropna().reset_index(drop=True)
    data['length'] = data['sql'].str.len() + data['parameters'].str.len()

    alt.data_transformers.disable_max_rows()
    brush = alt.selection_interval()


# -----> create the scatter plot graph
    line = alt.Chart(data.reset_index()).mark_point().encode(
        x=alt.X('length:Q', axis=alt.Axis(title='Query Length')),
        y=alt.Y('total_duration:Q', axis=alt.Axis(title='Latency (ms)')),
        color=alt.condition(brush, 'cmd_tag:N', alt.value('lightgray')),
        shape='cmd_tag:N',
        tooltip=['index:O','total_duration:Q', 'length:Q', 'log_time_with_tz:N', 'sql:N', \
            'parameters:N', 'cmd_tag:N', 'id1:N', 'id2:N']
    ).properties(
        width=500,
        height=500,
        title='Einherjar Queries'
    ).add_selection(
        brush
    ).interactive()

# -----> display the mean via a line across our chart
    rule = alt.Chart(data).mark_rule(color='red').encode(
        y='median(total_duration):Q',
        size=alt.value(2)
    )

    alt.Chart(data).configure_title(
        fontSize=30
    )

# -----> display number of interations per table insert
    dog = data_info[['inserted_data', 'cmd_tag']].dropna()
    bars1 = alt.Chart(dog).mark_bar().encode(
        y = 'inserted_into:N',
        color = 'cmd_tag:N',
        x = 'count(inserted_into):Q'
    ).transform_filter(
        brush
    )
# -----> display number of interations per table select
    cat = data_info[['selected_from', 'cmd_tag']].dropna()
    bars2 = alt.Chart(cat).mark_bar().encode(
        y = 'selected_from:N',
        color = 'cmd_tag:N',
        x = 'count(selected_from):Q'
    ).transform_filter(
        brush
    )
# -----> add the line and rule charts to the base chart
    chart = line + rule
    chart = chart & bars1 & bars2
    
    chart.save('data.json')
    chart.save('data.html')
    if verbose >= 1:
        print("Vega Graphics have been completed")

#!/usr/bin/env python3
import altair as alt
import pandas
import selenium


def vegaGraphics(
        cmdTag,
        id1,
        id2,
        parameters,
        sql,
        transformedData,
        verbose,):
    """Create interactive charts for specified data"""
    # making function more explicit
    cmdTag = cmdTag
    id1 = id1
    id2 = id2
    parameters = parameters
    sql = sql
    transformedData = transformedData
    verbose = verbose
    
    if verbose >= 1:
        print(
            "Creating Vega Graphics"
        )
    transformedData = transformedData.rename(
        columns = {
            id1 : "id1",
            id2 : "id2",
            sql : "sql",
            cmdTag : "cmdTag",
            parameters : "parameters"})

    dataInfo = transformedData.copy()
    data = transformedData[["total_duration",
                            "cmdTag",
                            "id1",
                            "id2",
                            "sql",
                            "parameters"]].copy()
    
    data = data.sort_values(by = ["total_duration"],
                            ascending = True,
                            inplace = False).dropna().reset_index(drop = True)
    data["length"] = data["sql"].str.len() + data["parameters"].str.len()

    alt.data_transformers.disable_max_rows()
    brush = alt.selection_interval()


# -----> create the scatter plot graph
    line = alt.Chart(data.reset_index()).mark_point().encode(
        x = alt.X(
            "length:Q",
            axis = alt.Axis(title = "Query Length")),
        y=alt.Y(
            "total_duration:Q",
            axis = alt.Axis(title = "Latency (ms)")),
        color = alt.condition(
            brush,
            "cmdTag:N",
            alt.value("lightgray")),
        shape = "cmdTag:N",
        tooltip = ["index:O",
                   "total_duration:Q",
                   "length:Q",
                   "log_time_with_tz:N",
                   "sql:N",
                   "parameters:N",
                   "cmdTag:N",
                   "id1:N",
                   "id2:N"]
    ).properties(
        width = 500,
        height = 500,
        title = "Einherjar Queries"
    ).add_selection(
        brush
    ).interactive()

# -----> display the mean via a line across our chart
    rule = alt.Chart(data).mark_rule(color = "red").encode(
        y = "median(total_duration):Q",
        size = alt.value(2)
    )

    alt.Chart(data).configure_title(
        fontSize = 30
    )

# -----> display number of interations per table insert
    dog = dataInfo[["inserted_data", "cmdTag"]].dropna()
    bars1 = alt.Chart(dog).mark_bar().encode(
        y = "inserted_into:N",
        color = "cmdTag:N",
        x = "count(inserted_into):Q"
    ).transform_filter(
        brush
    )
# -----> display number of interations per table select
    cat = dataInfo[["selected_from", "cmdTag"]].dropna()
    bars2 = alt.Chart(cat).mark_bar().encode(
        y = "selected_from:N",
        color = "cmdTag:N",
        x = "count(selected_from):Q"
    ).transform_filter(
        brush
    )
# -----> add the line and rule charts to the base chart
    chart = line + rule
    chart = chart & bars1 & bars2
    
    chart.save("results/data.json")
    chart.save("results/data.html")
    if verbose >= 1:
        print(
            "Vega Graphics have been completed"
        )
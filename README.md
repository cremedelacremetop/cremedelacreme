# Crème de la crème
## Investigating Metadata and Survivability of Top Android Apps 

Mobile apps are distributed via online markets that allow developers to reach a large set of users in different geographic locations. With this online-market-based distribution model, developers have access to a high volume  of crowd-sourced requirements, comments, and ratings. In addition to crowd-sourced reviews, app markets contain valuable apps' metadata that have motivated a plethora of previous works  aimed at mining that information with different purposes. The online markets also operate as a board in which top apps are recognized in lists grouped by category and price, but also in curated lists as the editor choice list of Google Play. Despite the prolific amount of work on app store mining, to the best of our knowledge, the characteristics of the apps on those lists and other aspects such as the survivability in those top-notch lists have not been investigated. Thus in this paper we investigate metadata and survivability of apps in the tops lists of Google Play, from four different countries, and collected during 30 weeks. 

## Research questions and main highlights 
Here you can find the main highlights of each RQs, including some results for not imputed and imputed data.

### RQ1  
_What are the prevalent characteristics of top apps?_

The following table presents the variables we selected in order to determine their prevalent characteristics for top apps:   
  <table>
  <thead>
    <th>Type</th>
    <th>Variable</th>
  </thead>
  <tbody>
    <tr><td rowspan="3">Categorical</td><td>Content Rating</td></tr>
    <tr><td>Android Version</td></tr>
    <tr><td>What's New</td></tr>
    <tr><td rowspan="12">Numerical</td><td>Name Length</td></tr>
    <tr><td>Summary Length</td></tr>
    <tr><td>Description Length</td></tr>
    <tr><td>Rating</td></tr>
    <tr><td>1 Star</td></tr>
    <tr><td>2 Stars</td></tr>
    <tr><td>3 Stars</td></tr>
    <tr><td>4 Stars</td></tr>
    <tr><td>5 Stars</td></tr>
    <tr><td>Days since last update</td></tr>
    <tr><td>Price (USD)</td></tr>
    <td>Number of Installs</td></tr>
  </tbody>
</table>

#### Content Rating

To begin, we analyzed Content Rating. Following figure illustrates the possible values of Content Rating for the dataset without imputations:

![](/images/content_rating.png)  

However, we didn't find different predominant values for the dataset with imputations, as presented above:

 LOCF  | MFO 
:-------------------------:|:-------------------------:
![](/images/content_rating_locf.png) |![](/images/content_rating_mfo.png)

After analyzing the dataset in general, we grouped it by countries to found whether there were differences between Brazil, Colombia, Germany and USA. As presented in the following figure, we found predominant content rating was the suitable for all ages, but the corresponding one for each country:

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div id="dd797a7f-4647-44d8-bf1d-60544ffbb04a" class="plotly-graph-div" style="height:100%; width:100%;"></div>
<script type="text/javascript">
  window.PLOTLYENV=window.PLOTLYENV || {};
  if (document.getElementById("dd797a7f-4647-44d8-bf1d-60544ffbb04a")) {
  Plotly.newPlot(
  'dd797a7f-4647-44d8-bf1d-60544ffbb04a',
  [{"name": "br", "orientation": "h", "type": "bar", "x": [133118, 7079, 6333, 1516, 513, 126, 51], "y": ["All ages", "Rated 14+", "Rated 12+", "Rated 10+", "Rated 16+", "Rated 18+", "Unrated"]}, {"name": "co", "orientation": "h", "type": "bar", "x": [160332, 12807, 6672, 3018, 64, 34], "y": ["Everyone", "Teen", "Mature 17+", "Everyone 10+", "Unrated", "Adults only 18+"]}, {"name": "de", "orientation": "h", "type": "bar", "x": [146774, 8371, 5042, 3918, 1936, 51], "y": ["USK: All ages", "USK: Ages 12+", "USK: Ages 18+", "USK: Ages 6+", "USK: Ages 16+", "Unrated"]}, {"name": "us", "orientation": "h", "type": "bar", "x": [149275, 14338, 6508, 3007, 88, 70], "y": ["Everyone", "Teen", "Mature 17+", "Everyone 10+", "Adults only 18+", "Unrated"]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Content Rating"}, "updatemenus": [{"buttons": [{"args": [{"visible": [true, true, true, true]}], "label": "All", "method": "update"}, {"args": [{"visible": [true, false, false, false]}], "label": "br", "method": "update"}, {"args": [{"visible": [false, true, false, false]}], "label": "co", "method": "update"}, {"args": [{"visible": [false, false, true, false]}], "label": "de", "method": "update"}, {"args": [{"visible": [false, false, false, true]}], "label": "us", "method": "update"}], "direction": "down", "pad": {"r": 10, "t": 10}, "showactive": true, "x": 0.1, "xanchor": "left", "y": 1.1, "yanchor": "top"}]},
                        {"responsive": true}
                    )
                };                
</script>

- Content Rating, grouped by country, possible values for dataset with MFO imputation can be found here: [Content Rating MFO](https://htmlpreview.github.io/?https://github.com/cremedelacremetop/cremedelacreme/blob/gh-pages/htmls/MFO_content_rating_country.html)

- Content Rating, grouped by country, possible values for dataset with LOCF imputation can be found here: [Content Rating LOCF](https://htmlpreview.github.io/?https://github.com/cremedelacremetop/cremedelacreme/blob/gh-pages/htmls/LOCF_content_rating_country.html)

Similarly, when analyzing by tops, we analyzed if Top free, Top selling and the Editor choice had differences:

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div id="51b537f9-a62a-4aa3-9494-c23348ac90b1" class="plotly-graph-div" style="height:100%; width:100%;"></div>
<script type="text/javascript">
           window.PLOTLYENV=window.PLOTLYENV || {};
           if (document.getElementById("51b537f9-a62a-4aa3-9494-c23348ac90b1")) {
           Plotly.newPlot(
           '51b537f9-a62a-4aa3-9494-c23348ac90b1',
           [{"name": "editorChoice", "orientation": "h", "type": "bar", "x": [2153, 1099, 1047, 328, 152, 118, 90, 58, 29, 26], "y": ["Everyone", "All ages", "USK: All ages", "Teen", "USK: Ages 12+", "Rated 12+", "USK: Ages 16+", "Rated 14+", "Rated 16+", "Everyone 10+"]}, {"name": "topFree", "orientation": "h", "type": "bar", "x": [164394, 84768, 83459, 19080, 10067, 6370, 6056, 5180, 4312, 3644, 3009, 1536, 925, 341, 127, 116, 40], "y": ["Everyone", "All ages", "USK: All ages", "Teen", "Mature 17+", "USK: Ages 12+", "Rated 14+", "Rated 12+", "USK: Ages 18+", "Everyone 10+", "USK: Ages 6+", "USK: Ages 16+", "Rated 10+", "Rated 16+", "Unrated", "Adults only 18+", "Rated 18+"]}, {"name": "topSelling", "orientation": "h", "type": "bar", "x": [143060, 62268, 47251, 7737, 3113, 2355, 1849, 1035, 965, 909, 730, 591, 310, 143, 109, 86, 6], "y": ["Everyone", "USK: All ages", "All ages", "Teen", "Mature 17+", "Everyone 10+", "USK: Ages 12+", "Rated 12+", "Rated 14+", "USK: Ages 6+", "USK: Ages 18+", "Rated 10+", "USK: Ages 16+", "Rated 16+", "Unrated", "Rated 18+", "Adults only 18+"]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Content Rating"}, "updatemenus": [{"buttons": [{"args": [{"visible": [true, true, true]}], "label": "All", "method": "update"}, {"args": [{"visible": [true, false, false]}], "label": "editorChoice", "method": "update"}, {"args": [{"visible": [false, true, false]}], "label": "topFree", "method": "update"}, {"args": [{"visible": [false, false, true]}], "label": "topSelling", "method": "update"}], "direction": "down", "pad": {"r": 10, "t": 10}, "showactive": true, "x": 0.1, "xanchor": "left", "y": 1.1, "yanchor": "top"}]},
                        {"responsive": true}
                    )
                };                
</script>


- Content Rating, grouped by top, possible values for dataset with MFO imputation can be found here: [Content Rating MFO](https://htmlpreview.github.io/?https://github.com/cremedelacremetop/cremedelacreme/blob/gh-pages/htmls/MFO_content_rating_top.html)

- Content Rating, grouped by top, possible values for dataset with LOCF imputation can be found here: [Content Rating LOCF](https://htmlpreview.github.io/?https://github.com/cremedelacremetop/cremedelacreme/blob/gh-pages/htmls/LOCF_content_rating_top.html)

In conclusion, no matter if we are analyzing Top Free, Top selling of Editor choice, the predominant content rating is _Everyone_.

Finally, we grouped by country and top, as depicted in the following figure:

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div id="33e79995-a3f0-4756-8d03-2cbcf2ad3c4e" class="plotly-graph-div" style="height:100%; width:100%;"></div>
<script type="text/javascript">
  window.PLOTLYENV=window.PLOTLYENV || {};
  if (document.getElementById("33e79995-a3f0-4756-8d03-2cbcf2ad3c4e")) {
  Plotly.newPlot(
  '33e79995-a3f0-4756-8d03-2cbcf2ad3c4e',
  [{"name": "('editorChoice', 'br')", "orientation": "h", "type": "bar", "x": [1099, 118, 58, 29], "y": ["All ages", "Rated 12+", "Rated 14+", "Rated 16+"]}, {"name": "('editorChoice', 'co')", "orientation": "h", "type": "bar", "x": [976, 164, 13], "y": ["Everyone", "Teen", "Everyone 10+"]}, {"name": "('editorChoice', 'de')", "orientation": "h", "type": "bar", "x": [1047, 152, 90], "y": ["USK: All ages", "USK: Ages 12+", "USK: Ages 16+"]}, {"name": "('editorChoice', 'us')", "orientation": "h", "type": "bar", "x": [1177, 164, 13], "y": ["Everyone", "Teen", "Everyone 10+"]}, {"name": "('topFree', 'br')", "orientation": "h", "type": "bar", "x": [84768, 6056, 5180, 925, 341, 40, 32], "y": ["All ages", "Rated 14+", "Rated 12+", "Rated 10+", "Rated 16+", "Rated 18+", "Unrated"]}, {"name": "('topFree', 'co')", "orientation": "h", "type": "bar", "x": [83071, 8570, 5031, 1811, 29, 28], "y": ["Everyone", "Teen", "Mature 17+", "Everyone 10+", "Adults only 18+", "Unrated"]}, {"name": "('topFree', 'de')", "orientation": "h", "type": "bar", "x": [83459, 6370, 4312, 3009, 1536, 34], "y": ["USK: All ages", "USK: Ages 12+", "USK: Ages 18+", "USK: Ages 6+", "USK: Ages 16+", "Unrated"]}, {"name": "('topFree', 'us')", "orientation": "h", "type": "bar", "x": [81323, 10510, 5036, 1833, 87, 33], "y": ["Everyone", "Teen", "Mature 17+", "Everyone 10+", "Adults only 18+", "Unrated"]}, {"name": "('topSelling', 'br')", "orientation": "h", "type": "bar", "x": [47251, 1035, 965, 591, 143, 86, 19], "y": ["All ages", "Rated 12+", "Rated 14+", "Rated 10+", "Rated 16+", "Rated 18+", "Unrated"]}, {"name": "('topSelling', 'co')", "orientation": "h", "type": "bar", "x": [76285, 4073, 1641, 1194, 36, 5], "y": ["Everyone", "Teen", "Mature 17+", "Everyone 10+", "Unrated", "Adults only 18+"]}, {"name": "('topSelling', 'de')", "orientation": "h", "type": "bar", "x": [62268, 1849, 909, 730, 310, 17], "y": ["USK: All ages", "USK: Ages 12+", "USK: Ages 6+", "USK: Ages 18+", "USK: Ages 16+", "Unrated"]}, {"name": "('topSelling', 'us')", "orientation": "h", "type": "bar", "x": [66775, 3664, 1472, 1161, 37, 1], "y": ["Everyone", "Teen", "Mature 17+", "Everyone 10+", "Unrated", "Adults only 18+"]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Content Rating"}, "updatemenus": [{"buttons": [{"args": [{"visible": [true, true, true, true, true, true, true, true, true, true, true, true]}], "label": "All", "method": "update"}, {"args": [{"visible": [true, false, false, false, false, false, false, false, false, false, false, false]}], "label": "('editorChoice', 'br')", "method": "update"}, {"args": [{"visible": [false, true, false, false, false, false, false, false, false, false, false, false]}], "label": "('editorChoice', 'co')", "method": "update"}, {"args": [{"visible": [false, false, true, false, false, false, false, false, false, false, false, false]}], "label": "('editorChoice', 'de')", "method": "update"}, {"args": [{"visible": [false, false, false, true, false, false, false, false, false, false, false, false]}], "label": "('editorChoice', 'us')", "method": "update"}, {"args": [{"visible": [false, false, false, false, true, false, false, false, false, false, false, false]}], "label": "('topFree', 'br')", "method": "update"}, {"args": [{"visible": [false, false, false, false, false, true, false, false, false, false, false, false]}], "label": "('topFree', 'co')", "method": "update"}, {"args": [{"visible": [false, false, false, false, false, false, true, false, false, false, false, false]}], "label": "('topFree', 'de')", "method": "update"}, {"args": [{"visible": [false, false, false, false, false, false, false, true, false, false, false, false]}], "label": "('topFree', 'us')", "method": "update"}, {"args": [{"visible": [false, false, false, false, false, false, false, false, true, false, false, false]}], "label": "('topSelling', 'br')", "method": "update"}, {"args": [{"visible": [false, false, false, false, false, false, false, false, false, true, false, false]}], "label": "('topSelling', 'co')", "method": "update"}, {"args": [{"visible": [false, false, false, false, false, false, false, false, false, false, true, false]}], "label": "('topSelling', 'de')", "method": "update"}, {"args": [{"visible": [false, false, false, false, false, false, false, false, false, false, false, true]}], "label": "('topSelling', 'us')", "method": "update"}], "direction": "down", "pad": {"r": 10, "t": 10}, "showactive": true, "x": 0.1, "xanchor": "left", "y": 1.1, "yanchor": "top"}]},
                        {"responsive": true}
                    )
                };               
</script>

However, when grouping by country and top in the dataset with imputations, as presented here:

- Content Rating, grouped by country and top, possible values for dataset with MFO imputation can be found here: [Content Rating MFO](https://htmlpreview.github.io/?https://github.com/cremedelacremetop/cremedelacreme/blob/gh-pages/htmls/MFO_content_rating_group.html)

- Content Rating, grouped by country and top, possible values for dataset with LOCF imputation can be found here: [Content Rating LOCF](https://htmlpreview.github.io/?https://github.com/cremedelacremetop/cremedelacreme/blob/gh-pages/htmls/LOCF_content_rating_group.html)

Editor choice in Colombia dissapeared, because it had more than 4 missing weeks. Thus, even when the behavior is the same, predominant content rating is _Everyone_, the group for Colombia and Editor choice is missing, in consequence, we cannot conclude that _Everyone_ is the predominant for all groups.

#### Android Version

**Main highlights:** for categorical and some numerical variables, there are no differences across countries. Despite this, regarding rating, amount of stars, number of installs and price, differences are relevant. Predominant characteristics of categorical variables remain the same even if we analyze at top-list or country level, with the exception of _Android version_ for Editor Choice. However, predominant variables of numeric variables change mostly across top lists, in particular when dealing with editor choice, despite this, they also change across countries but at a minor rate. Besides, we can conclude that numerical variables related to _length_ do not show relevant differences, but variables related to _rating_ and _amount of stars_ showed large differences in all the cases, no matter the level (top,-list country or top-list-and-country level). In addition, _price_, _number of installs_ and _days since last update_ vary when different combinations across tops and countries are made. Then, when grouping tops and countries, prevailing characteristics differ.

### RQ2  
_Do top apps' predominant characteristics change over time?_

**Main highlights:** after analyzing the data at different time intervals, we conclude that _content rating_, _Android version_, _name length_, _description length_ and _days since last update_ remain consistent among time. However,  _what's new_, _summary length_ and _price_ tend to evolve mostly at the final weeks of the analysis period. _Number of install_ stabilizes at the end and, lastly, _rating_ changes values constantly.

### RQ3  
_What are the top-list survivability patterns exhibited by the analyzed apps?_

To answer this question for each app we analyzed some survivability events to understand survivability behavior patterns in the analyzed apps for some granularities (Country, top, category). 

#### TLO 
A TLO indicates the number of survivability events for an app.

##### Country 
_TLO(Country)_ distributions by country are all different, except USA and colombia, but all the differences were negligible. As it is possible to se in the next figures all the distributtions were similar between not imputed data and imputations
           
![](/images/TLO_country.png)  

*TLO distribution for each country for not imputed data*

 LOCF | MFO 
:-------------------------:|:-------------------------:
![](/images/TLO_country_LOCF.png) |![](/images/TLO_country_MFO.png)


For not imputed data and imputed data, we got these results:

  Comparision | H0 rejected | Cliff's delta size
:-----------------:|:-----------------:|:-----------------:
  BR vs CO |True | Negligible 
  BR vs DE |True | Negligible 
  BR vs US |True | Negligible 
  CO vs DE |True | Negligible 
  CO vs US |False|  --
  DE vs US |True | Negligible 

##### Top

_TLO(Top)_ distributions by top are all different and no difference was considerable. In the next figures you can it is possible to see the TLO distribution by top and for each dataset (not imputed and imputed dataset), as we pointed out, there is no significant differences  between each image,

![](/images/TLO_top.png)  
*TLO distribution by top-list for not imputed data*

 LOCF  | MFO 
:-------------------------:|:-------------------------:
![](/images/TLO_top_LOCF.png) |![](/images/TLO_top_MFO.png)

When we compared each pair of distributions with the respective comparisons, we found that all were different. These results are presented in the next table. It is worth mention that for the imputed data and not imputed data we obtain the same results. 


  Comparision | H0 rejected | Cliff's delta size
:-----------------:|:-----------------:|:-----------------:
  Top selling vs Top free |True | Small 
  Top selling vs Editor's choice |True | Medium 
 Top free vs Editor's choice |True | Small 
 
 

#### EST and  TBSE
A EST is the duration of each TLO event, while A TBSE is the time between two consecutive TLO events. In the next subsections it is possible to see the results for each aggregations and event. In addition, we present the result for the imputed and not imputed data. 

##### Country 
In the next figure it is possible to see EST and TBSE by country. For TSE its important to point out that some apps stayed 30 consecutive weeks in a top-list and in the opposite another apps only stayed for a single week. Conserning TBSE, some apps left the top for a single week (TBSE=1), while some apps had the opposite behavior and left a top for 28 weeks. 

![](/images/country_event.png)  
*EST and TBSE distribution by Country for not imputed data*

 LOCF  | MFO 
:-------------------------:|:-------------------------:
![](/images/country_event_LOCF.png) |![](/images/country_event_MFO.png)


##### Top
When analysing EST and TBSE events by top-list, we found that Editor's choice is a distributions that behaves way different than the other two. This behaviour was the same across the three approaches (imputed data). 

![](/images/top_events.png)  
*EST and TBSE distribution by top-list for not imputed data*

 LOCF  | MFO 
:-------------------------:|:-------------------------:
![](/images/top_events_LOCF.png) |![](/images/top_events_MFO.png)

This differences  also corroborated that these distributions were statistically significant and were not trivial, excepting _TBSE(Top selling)_ vs _TBSE(Top free)_. In fact the dissimilarities that involved Editor's choice were medium or large. 

  Event | Comparision | H0 rejected | Cliff's delta size
:-----------------:|:-----------------:|:-----------------:|:-----------------:
TSE|  Top selling vs Top free |True | Small 
TSE|   Top selling vs Editor's choice |True | Large 
TSE| Top free vs Editor's choice |True | Large 
TBSE|  Top selling vs Top free |True | Negligible 
TBSE|   Top selling vs Editor's choice |True | Medium 
TBSE| Top free vs Editor's choice |True | Medium 
 
##### Category
When analysing by category we found that for **_EST_** by category we dound that _Dating_ Category was the distribution that had the greatest number of non trivial differences with other categories a total of 25. For simplification we used a heatmap and we only ilustrated the first diagonal, because is redundant the other half. 


![](/images/EST_category.png)  
*EST distribution by category for not imputed data*

 LOCF  | MFO 
:-------------------------:|:-------------------------:
![](/images/EST_category_LOCF.png) |![](/images/EST_category_MFO.png)


**Main highlights:**  taking into account different survivability events can help us to understand some behaviors of the apps in the studied time. For instance, (i) Editor’s choice is the most stable and less diverse top list: it has the lowest number of apps being at the list and the highest survival times;  (ii) between the countries, the events’ distributions can differ but the effect size, in most cases, is trivial (delta<0.2); (iii) if an app returns after leaving a top list, it has a smaller time window for Editor’s choice than for the other tops to do it; (iv) analyzing these events by category show that the differences in the distribution events are, in majority, negligible

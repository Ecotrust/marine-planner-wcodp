// load layers from fixture or the server
app.viewModel.loadLayers = function(data) {
	var self = app.viewModel;
	// load layers
	$.each(data.layers, function(i, layer) {
		var layerViewModel = new layerModel(layer);

		self.layerIndex[layer.id] = layerViewModel;
		// add sublayers if they exist
		if (layer.subLayers) {
			$.each(layer.subLayers, function(i, layer_options) {
				var subLayer = new layerModel(layer_options, layerViewModel);
				app.viewModel.layerIndex[subLayer.id] = subLayer;
				layerViewModel.subLayers.push(subLayer);
			});
		}
	});

	// load themes
	$.each(data.themes, function(i, themeFixture) {
		var layers = [],
			theme = new themeModel(themeFixture);
		$.each(themeFixture.layers, function(j, layer_id) {
			// create a layerModel and add it to the list of layers
			var layer = self.layerIndex[layer_id],
				searchTerm = layer.name + ' (' + themeFixture.display_name + ')';
			layer.themes.push(theme);
			theme.layers.push(layer);
            
			if (!layer.subLayers.length) { //if the layer does not have sublayers
                self.layerSearchIndex[searchTerm] = {
                    layer: layer,
                    theme: theme
                };
            } else { //if the layer has sublayers
				$.each(layer.subLayers, function(i, subLayer) {
					//var searchTerm = subLayer.name + ' (' + themeFixture.display_name + ')';
                    var searchTerm = subLayer.name + ' (' + themeFixture.display_name + ' / ' + subLayer.parent.name + ')';
					if (subLayer.name !== 'Data Under Development') {
                        self.layerSearchIndex[searchTerm] = {
                            layer: subLayer,
                            theme: theme
                        };
                    }
                    if (subLayer.filterable) {
                    	if (self.filterTab) {
							self.filterTab.filterLayers.push(subLayer);
                    	}
					}
				});  
                layer.subLayers.sort( function(a,b) { return a.name.toUpperCase().localeCompare(b.name.toUpperCase()); } );
			} 
			// filterable layers
			if (layer.filterable) {
				self.filterTab.filterLayers.push(layer);
			}

		});
        //sort by name
        theme.layers.sort( function(a,b) { return a.name.toUpperCase().localeCompare(b.name.toUpperCase()); } );
        
		self.themes.push(theme);
	});

	app.typeAheadSource = (function () {
            var keys = [];
            for (var searchTerm in app.viewModel.layerSearchIndex) {
                if (app.viewModel.layerSearchIndex.hasOwnProperty(searchTerm)) {
                    keys.push(searchTerm);
                }
            }
            return keys;
    })();
    
    //re-initialise the legend scrollbar 
    //if ( ! app.embeddedMap ) {
    if ( $(window).width() > 767 && !app.embeddedMap ) {
        $('#legend-content').jScrollPane(); 
    }

};
app.viewModel.loadLayersFromFixture = function() {
	app.viewModel.loadLayers(app.fixture);
};


app.viewModel.loadLayersFromServer = function() {
    var pathname = window.location.pathname,
        slug_name = pathname.substring(1, pathname.indexOf('/planner'));
    if (slug_name === '/') {
        slug_name = pathname.substring(1, pathname.indexOf('/visualize'));
    }
	return $.getJSON('/data_manager/get_json/'+slug_name, function(data) {
		app.viewModel.loadLayers(data);
	});
};
//test comment